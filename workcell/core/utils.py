from __future__ import annotations
import os
import re
import ast
import json
import yaml
import inspect
import importlib
import dotenv
import rich
import requests
from urllib.parse import urlparse
import posixpath
from typing import List, Dict

from workcell.core.errors import (
    WorkcellConfigGenerateError,
    WorkcellImportStringFormatError,
    WorkcellParamsFormatError,
    WorkcellParamsMissingError,
)

# Load weanalyze global environment variables
weanalyze_dotenv = os.path.join(os.path.expanduser("~"), ".weanalyze", "env")
dotenv.load_dotenv(weanalyze_dotenv)
# Load project environment variables
project_dotenv = os.path.join(os.getcwd(), ".env")
dotenv.load_dotenv(project_dotenv)
LOCALHOST_NAME = os.getenv("WORKCELL_SERVER_NAME", "127.0.0.1")


########
# Helper functions for file
########


def safe_join(directory: str, path: str) -> str | None:
    """Safely join zero or more untrusted path components to a base directory to avoid escaping the base directory.
    Borrowed from: werkzeug.security.safe_join"""
    _os_alt_seps: List[str] = list(
        sep for sep in [os.path.sep, os.path.altsep] if sep is not None and sep != "/"
    )

    if path != "":
        filename = posixpath.normpath(path)
    else:
        return directory

    if (
        any(sep in filename for sep in _os_alt_seps)
        or os.path.isabs(filename)
        or filename == ".."
        or filename.startswith("../")
    ):
        return None
    return posixpath.join(directory, filename)


########
# Helper functions for url
########
def get_local_server_without_check(
    server_name: str | None = None,
    server_port: int | None = None,
    ssl_keyfile: str | None = None,
    ssl_certfile: str | None = None,
    ssl_keyfile_password: str | None = None,
):
    """Get a local server endpoint for the provided Interface
    Parameters:
    server_name: to make app accessible on local network, set this to "0.0.0.0". Can be set by environment variable WORKCELL_SERVER_NAME.
    server_port: will start workcell app on this port (if available). Can be set by environment variable WORKCELL_SERVER_PORT.
    auth: If provided, username and password (or list of username-password tuples) required to access the Workcells. Can also provide function that takes username and password and returns True if valid login.
    ssl_keyfile: If a path to a file is provided, will use this as the private key file to create a local server running on https.
    ssl_certfile: If a path to a file is provided, will use this as the signed certificate for https. Needs to be provided if ssl_keyfile is provided.
    ssl_keyfile_password: If a password is provided, will use this with the ssl certificate for https.
    Returns:
    port: the port number the server is running on
    path_to_local_server: the complete address that the local server can be accessed at
    """
    server_name = server_name or LOCALHOST_NAME
    port = server_port
    url_host_name = "localhost" if server_name == "0.0.0.0" else server_name

    if ssl_keyfile is not None:
        if ssl_certfile is None:
            raise ValueError(
                "ssl_certfile must be provided if ssl_keyfile is provided."
            )
        path_to_local_server = "https://{}:{}/".format(url_host_name, port)
    else:
        path_to_local_server = "http://{}:{}/".format(url_host_name, port)

    return url_host_name, port, path_to_local_server


def get_server_url_from_ws_url(ws_url: str):
    ws_url_parsed = urlparse(ws_url)
    scheme = "http" if ws_url_parsed.scheme == "ws" else "https"
    port = f":{ws_url_parsed.port}" if ws_url_parsed.port else ""
    return f"{scheme}://{ws_url_parsed.hostname}{port}{ws_url_parsed.path.replace('queue/join', '')}"


def validate_url(possible_url: str) -> bool:
    headers = {"User-Agent": "workcell (https://weanalyze.co/; contact@weanalyze.co)"}
    try:
        head_request = requests.head(possible_url, headers=headers)
        if head_request.status_code == 405:
            return requests.get(possible_url, headers=headers).ok
        return head_request.ok
    except Exception:
        return False


########
# Helper functions for workcell
########
def name_to_title(name: str) -> str:
    """Converts a camelCase or snake_case name to title case."""
    # If camelCase -> convert to snake case
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
    # Convert to title case
    return name.replace("_", " ").strip().title()


def format_workcell_entrypoint(import_string: str) -> str:
    """Format a workcell entrypoint from an string.
    Args:
        import_string, str, acceptable import_string:
            e.g. import_string = "app:hello_world"
            e.g. import_string = "hello_world.app:hello_world"

    Returns:
        workcell_entrypoint, str, standard workcell_entrypoint: app:{function_name}
            e.g. workcell_entrypoint = "app:hello_world"

    """
    # import string validation
    if "/" in import_string:
        raise WorkcellImportStringFormatError(import_string)
    if import_string.startswith("."):
        raise WorkcellImportStringFormatError(import_string)
    if ":" not in import_string:
        raise WorkcellImportStringFormatError(import_string)

    # extract loader_path and function_name, import_string = "project_folder.app:function_name"
    loader_path = import_string.split(":")[0]
    function_name = import_string.split(":")[1]

    # workcell_entrypoint from loader path
    workcell_entrypoint = "{}:{}".format(loader_path, function_name)
    return workcell_entrypoint


def valid_workcell_import_string(import_string: str) -> bool:
    """Valid a function exists in app.py.
    Args:
        import_string, str, acceptable import_string:
            e.g. import_string = "app:hello_world"
            e.g. import_string = "hello_world.app:hello_world"
            e.g. import_string = "foo.bar.hello_world.app:hello_world"

    Returns:
        is_valid, bool, True if function exists in app.py, False if not.

    """
    # format workcell_entrypoint
    workcell_entrypoint = format_workcell_entrypoint(import_string)
    # split workcell_entrypoint
    function_file, function_name = (
        workcell_entrypoint.split(":")[0].split(".")[-1],
        workcell_entrypoint.split(":")[1],
    )
    # check function exists in app.py
    spec = importlib.import_module(function_file, os.getcwd())
    if hasattr(spec, function_name) and inspect.isfunction(
        getattr(spec, function_name)
    ):
        return True
    else:
        return False


def gen_provider_config(
    import_string: str,
    provider_name: str = "huggingface",
) -> Dict:
    """Prepare provider config for workcell.
    This will create a provider config dict.
    Args:
        import_string (str): import string / workcell name.
            e.g. import_string = "app:hello_workcell"
        provider_name (str): workcell provider.
            e.g. provider_name = "huggingface"
    Return:
        provider (dict): provider config dict.
    """
    entrypoint = format_workcell_entrypoint(
        import_string
    )  # format workcell_entrypoint from import_string
    name = entrypoint.split(":")[-1]  # a.k.a function_name, "hello_workcell"
    if provider_name == "huggingface":
        if os.environ.get("HUGGINGFACE_USERNAME"):
            repo_id = "{}/{}".format(os.environ.get("HUGGINGFACE_USERNAME"), name)
            provider = {
                "name": "huggingface",
                "repository": repo_id,
                "branch": "main",  # TODO: from user input
            }
        else:
            # if there is no `HUGGINGFACE_USERNAME` set, we will set to None and move on, until user pack it.
            provider = {"name": "huggingface", "repository": "", "branch": ""}
    else:
        # TODO:
        provider = {"name": "weanalyze"}
    return provider


def gen_workcell_config(
    import_string: str,
    provider_name: str = "huggingface",
    version: str = "latest",
    runtime: str = "python3.8",
    tags: str = "{}",
    envs: str = "{}",
) -> Dict:
    """Prepare template folder for workcell.
    This will create a folder and package template in build_path.
    Args:
        import_string (str): import string / workcell name.
            e.g. import_string = "app:hello_workcell"
        provider_name (str): workcell provider.
            e.g. provider_name = "huggingface"
        version (str): workcell version.
            e.g. version = "latest"
        runtime (str): workcell runtime.
            e.g. runtime = "python3.8"
        tags (dict): workcell tags.
            e.g. tags = '{"vendor":"aws", "service-type":"http"}'
        envs (dict): workcell env.
            e.g. envs = '{"STAGE":"latest"}'

    Return:
        workcell_config (dict): build config for workcell.
    """
    # transparent workcell_config
    try:
        entrypoint = format_workcell_entrypoint(
            import_string
        )  # format workcell_entrypoint from import_string
        name = entrypoint.split(":")[-1]  # a.k.a function_name, "hello_workcell"
        version = version  # "latest" | "v1.0.0" | "dev" | "prod"
        runtime = runtime  # "python3.8" | "python3.9" | "nodejs14.x" | "nodejs12.x"
    except Exception as e:
        raise WorkcellConfigGenerateError(e)

    # workcell provider, wrap into dict
    try:
        provider = gen_provider_config(import_string, provider_name)
    except Exception as e:
        raise WorkcellParamsFormatError(msg=provider_name)

    # workcell tags
    try:
        tags = ast.literal_eval(tags)  # useful tags
    except:
        raise WorkcellParamsFormatError(tags)

    # workcell envs
    try:
        envs = ast.literal_eval(envs)  # useful tags
    except:
        raise WorkcellParamsFormatError(envs)

    # pack config
    workcell_config = {
        "name": name,
        "provider": provider,
        "version": version,
        "runtime": runtime,
        "entrypoint": entrypoint,
        "tags": tags,
        "envs": envs,
    }
    return workcell_config


def save_workcell_config(workcell_config: dict, dest: str) -> None:
    """Save workcell config to a YAML file.
    Args:
        workcell_config (dict): build config for workcell.
        dest (str): path to save workcell config.
            e.g. dest = ".workcell/workcell.yaml"
    Returns:
        None
    """
    with open(dest, "w") as f:
        yaml.dump(workcell_config, f, default_flow_style=False, sort_keys=False)
    return None


def load_workcell_config(
    src: str,
) -> None:
    """Load workcell config from a YAML file.
    Args:
        src (str): path to load workcell config.
            e.g. src = ".workcell/workcell.yaml"
    Returns:
        None
    """
    with open(src) as f:
        # use safe_load instead load
        workcell_config = yaml.safe_load(f)
    return workcell_config


def colab_check() -> bool:
    """
    Check if workcell is deploy to huggingface
    :return is_colab (bool): True or False
    """
    is_colab = False
    try:  # Check if running interactively using ipython.
        from IPython import get_ipython

        from_ipynb = get_ipython()
        if "google.colab" in str(from_ipynb):
            is_colab = True
    except (ImportError, NameError):
        pass
    return is_colab
