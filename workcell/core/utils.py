import os
import re
import ast
import json
import inspect
import importlib
from workcell.core.errors import (
    WorkcellImportStringFormatError,
    WorkcellParamsFormatError
)


def name_to_title(
    name: str
) -> str:
    """Converts a camelCase or snake_case name to title case."""
    # If camelCase -> convert to snake case
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
    # Convert to title case
    return name.replace("_", " ").strip().title()


def format_workcell_entrypoint(
    import_string: str
) -> str:
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
    # if contains porject_folder, remove it
    # if "." in import_string:
    #     import_string = import_string.split(".")[-1]
    
    # extract loader_path and function_name, import_string = "project_folder.app:function_name"
    loader_path = import_string.split(":")[0]
    function_name = import_string.split(":")[1]

    # workcell_entrypoint from loader path
    workcell_entrypoint = "{}:{}".format(loader_path, function_name)
    return workcell_entrypoint


def valid_workcell_import_string(
    import_string: str
) -> bool:
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
    workcell_entrypoint = format_workcell_entrypoint(
        import_string
    )
    # split workcell_entrypoint
    function_file, function_name = \
        workcell_entrypoint.split(":")[0].split('.')[-1], \
        workcell_entrypoint.split(":")[1]
    # check function exists in app.py
    spec = importlib.import_module(function_file, os.getcwd())
    if (hasattr(spec, function_name) and \
        inspect.isfunction(getattr(spec, function_name))):
        return True
    else:
        return False 


def gen_workcell_config(
    import_string: str,
    image_uri:  str="",    
    workcell_version: str="latest",
    workcell_runtime: str="python3.8", 
    workcell_tags: str="{}",
    workcell_env: str="{}"
) -> str:
    """Prepare template folder for workcell.
    This will create a folder and package template in build_path.
    Args:
        import_string (str): import string / workcell fqdn.
            e.g. import_string = "app:hello_workcell"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_runtime (str): workcell runtime.
            e.g. workcell_runtime = "python3.8" 
        image_uri (str): docker image uri.
            e.g. image_uri = "weanalyze/hello_workcell:latest"
        workcell_tags (dict): workcell tags.
            e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}'
        workcell_env (dict): workcell env.
            e.g. workcell_env = '{"STAGE":"latest"}'

    Return:
        workcell_config (dict): build config for workcell.
    """
    # extract workcell_config
    try:
        username = os.environ["WORKCELL_USERNAME"]
        workcell_entrypoint = format_workcell_entrypoint(import_string) # format workcell_entrypoint from import_string
        workcell_name = workcell_entrypoint.split(":")[-1] # a.k.a function_name, "hello_workcell" 
        workcell_version = workcell_version # "latest" | "v1.0.0" | "dev" | "prod"
        workcell_runtime = workcell_runtime # "python3.8" | "python3.9" | "nodejs14.x" | "nodejs12.x"
    except:
        raise WorkcellImportStringFormatError(import_string)
    # workcell code
    try:
        if image_uri == "":
            image_uri = "{}/{}:{}".format(username, workcell_name, workcell_version) # default build tag: {username}/{workcell_name}:{workcell_version}
            workcell_code = {
                "ImageUri": image_uri
            }
        else:
            workcell_code = {
                "ImageUri": image_uri
            }
    except:
        raise WorkcellParamsFormatError(workcell_code)        
    # workcell tags
    try:
        workcell_tags = ast.literal_eval(workcell_tags) # useful tags
    except:
        raise WorkcellParamsFormatError(workcell_tags)
    # workcell env
    try:
        workcell_env = ast.literal_eval(workcell_env) # useful tags
    except:
        raise WorkcellParamsFormatError(workcell_env)
    # pack config
    workcell_config = {
        "username": username,
        "workcell_name": workcell_name, 
        "workcell_version": workcell_version, 
        "workcell_runtime": workcell_runtime, 
        "workcell_entrypoint": workcell_entrypoint, 
        "workcell_code": workcell_code,
        "workcell_tags": workcell_tags, 
        "workcell_env": workcell_env,
    } 
    return workcell_config


def save_workcell_config(
    workcell_config: dict, 
    dest: str
) -> None:
    """Save workcell config to a file.
    Args:
        workcell_config (dict): build config for workcell.
        dest (str): path to save workcell config.
            e.g. dest = ".workcell/workcell_config.json"
    Returns:
        None
    """
    with open(dest, "w") as f:
        json.dump(workcell_config, f, indent=4)
    return None


def load_workcell_config(
    src: str,
) -> None:
    """Save workcell config to a file.
    Args:
        src (str): path to load workcell config.
            e.g. src = ".workcell/workcell_config.json"
    Returns:
        None
    """
    with open(src, "r") as f:
        workcell_config = json.load(f)
    return workcell_config


