from __future__ import annotations
import importlib
import inspect
from typing import Any, Dict, Optional
from typing import Callable, Type, get_type_hints
from pydantic import BaseModel, parse_raw_as
from pydantic.tools import parse_obj_as

from workcell.core.components import Component
from workcell.core.spec import generate_json_schema
from workcell.core.utils import (
    format_workcell_entrypoint,
    name_to_title,
    gen_workcell_config,
    gen_provider_config,
)
from workcell.core.errors import CallableTypeError, WorkcellConfigFormatError


def is_compatible_type(type: Type) -> bool:
    """Returns `True` if the type is workcell-compatible."""
    try:
        if issubclass(type, BaseModel):
            return True
    except Exception:
        pass
    try:
        # valid list type
        if type.__origin__ is list and issubclass(type.__args__[0], BaseModel):
            return True
    except Exception:
        pass
    return False


def get_input_type(fn: Callable) -> Type | Component:
    """Returns the input type of a given function (callable).
    Args:
        fn: The function for which to get the input type.
    Raises:
        ValueError: If the function does not have a valid input type annotation.
    """
    type_hints = get_type_hints(fn)
    if "input" not in type_hints:
        raise ValueError(
            "The callable MUST have a parameter with the name `input` with typing annotation. "
            "For example: `def my_workcell(input: InputModel) -> OutputModel:`."
        )
    input_type = type_hints["input"]
    if not is_compatible_type(input_type):
        raise ValueError(
            "The `input` parameter MUST be a subclass of the Pydantic BaseModel or a list of Pydantic models."
        )
    # TODO: return warning if more than one input parameters
    return input_type


def get_output_type(fn: Callable) -> Type | Component:
    """Returns the output type of a given function (callable).
    Args:
        fn: The function for which to get the output type.
    Raises:
        ValueError: If the function does not have a valid output type annotation.
    """
    type_hints = get_type_hints(fn)
    if "return" not in type_hints:
        raise ValueError(
            "The return type of the callable MUST be annotated with type hints."
            "For example: `def my_workcell(input: InputModel) -> OutputModel:`."
        )
    output_type = type_hints["return"]
    if not is_compatible_type(output_type):
        raise ValueError(
            "The return value MUST be a subclass of the Pydantic BaseModel or a list of Pydantic models."
        )
    return output_type


def get_spec(fn: Callable) -> dict:
    """Get the spec of a given function (callable)."""
    input_type = get_input_type(fn)
    output_type = get_output_type(fn)
    # iterate ModelField to json serializable dict
    spec = {
        "name": fn.__name__,
        "input": generate_json_schema([input_type]),
        "output": generate_json_schema([output_type]),
    }
    return spec


def get_callable(import_string: str) -> Callable:
    """Import a callable from an string."""
    # e.g. import_string = "examples.hello_world.app:hello_workcell"
    workcell_path = format_workcell_entrypoint(import_string)
    loader_path, function_name = (
        workcell_path.split(":")[0],
        workcell_path.split(":")[-1],
    )
    try:
        mod = importlib.import_module(loader_path)
        fn = getattr(mod, function_name)
    except:
        raise ValueError(
            "The callable path import failed! Given import string: {}".format(
                import_string
            )
        )
    return fn


class Workcell:
    def __init__(
        self,
        fn: Callable | str | Dict,  # callable function, import string, workcell_config
        provider_name: Optional[str] = "huggingface",
        version: Optional[str] = "latest",
        runtime: Optional[str] = "python3.8",
        tags: Optional[Dict] = {},
        envs: Optional[Dict] = {},
        auth: Optional[Dict] = None,
        **kwargs,
    ):
        """Initializes a Workcell.
        Args:
            fn: The function to be wrapped, can be a callable, a import_string or workcell_config.
                e.g. fn = hello_workcell
                e.g. fn = "hello_workcell.app:hello_workcell"
                e.g. fn = {
                        "name": "hello_workcell",
                        "provider": "huggingface",
                     }
        Returns:
            A workcell instance.
        """
        # authentication
        self._auth = auth
        # extract from workcell config
        if isinstance(fn, Dict):
            if fn is None:
                raise WorkcellConfigFormatError(msg=fn)
            # workcell config
            self.name = fn.get("name")
            self.provider = fn.get("provider")  # a dict
            self.version = fn.get("version")
            self.runtime = fn.get("runtime")
            self.entrypoint = fn.get("entrypoint")
            self.tags = fn.get("tags")
            self.envs = fn.get("envs")
            # get callable
            self.function = get_callable(self.entrypoint)
            self.import_string = self.entrypoint
            # as-is config
            self.config = fn
        else:
            # get callable or import string
            if isinstance(fn, str):
                # Try to load the function from a string notion
                self.function = get_callable(fn)
                self.import_string = fn
            else:
                self.function = fn
                self.import_string = "app:" + str(self.function.__name__)
            # callable validation
            if not callable(self.function):
                raise CallableTypeError(str(self.function))
            if inspect.isclass(self.function):
                raise CallableTypeError(
                    "The provided callable is an uninitialized Class. This is not allowed."
                )
            # workcell config
            self.name = None
            self.provider = gen_provider_config(
                import_string=self.import_string, provider_name=provider_name
            )
            self.version = version
            self.runtime = runtime
            self.entrypoint = self.import_string
            self.tags = tags
            self.envs = envs
            # as-is config
            self.config = None

        # Properties: name, description, input_type, output_type,
        if inspect.isfunction(self.function):
            # The provided callable is a function
            self.input_type = get_input_type(self.function)
            self.output_type = get_output_type(self.function)
            self.name = self.function.__name__
            self.title = name_to_title(self.name)
            # Get description from function
            doc_string = inspect.getdoc(self.function)
            if doc_string:
                self.description = doc_string

        elif hasattr(self.function, "__call__"):
            # The provided callable is a function
            self.input_type = get_input_type(self.function.__call__)  # type: ignore
            self.output_type = get_output_type(self.function.__call__)  # type: ignore
            self.name = type(self.function).__name__
            self.title = name_to_title(self.name)
            # Get description from function
            try:
                doc_string = inspect.getdoc(self.function.__call__)  # type: ignore
                if doc_string:
                    self.description = doc_string
                if (
                    not self.description
                    or self.description == "Call self as a function."
                ):
                    # Get docstring from class instead of __call__ function
                    doc_string = inspect.getdoc(self.function)
                    if doc_string:
                        self.description = doc_string
            except Exception as e:
                pass
        else:
            raise CallableTypeError("Unknown callable type.")

        # Get spec
        self.spec = get_spec(self.function)

        # Get config
        if self.config is None:
            # only happens when user set import string or callable
            self.config = gen_workcell_config(
                import_string=self.import_string,
                provider_name=self.provider.get("name"),
                version=self.version,
                runtime=self.runtime,
                tags=str(self.tags),
                envs=str(self.envs),
            )

    def __call__(self, input: Any, **kwargs: Any) -> Any:
        input_obj = input
        if isinstance(input, str):
            # Allow json input
            input_obj = parse_raw_as(self.input_type, input)
        if isinstance(input, dict):
            # Allow dict input
            input_obj = parse_obj_as(self.input_type, input)
        return self.function(input_obj, **kwargs)


class WorkcellApp:
    def __init__(
        self,
        fn: Callable | str | None,
        inputs: Component,
        outputs: Component,
        preprocess: bool,
        postprocess: bool,
        inputs_as_dict: bool,
    ):
        self.fn = fn
        self.inputs = inputs
        self.outputs = outputs
        self.preprocess = preprocess
        self.postprocess = postprocess
        self.total_runtime = 0
        self.total_runs = 0
        self.inputs_as_dict = inputs_as_dict

    def __str__(self):
        return str(
            {
                "fn": getattr(self.fn, "__name__", "fn")
                if self.fn is not None
                else None,
                "preprocess": self.preprocess,
                "postprocess": self.postprocess,
            }
        )

    def __repr__(self):
        return str(self)
