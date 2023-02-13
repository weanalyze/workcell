from __future__ import annotations
import os
import re
import ast
import json
import inspect
import importlib
import dotenv
import requests
from urllib.parse import urlparse
import posixpath
from typing import List

from workcell.core.errors import (
    WorkcellConfigGenerateError,
    WorkcellImportStringFormatError,
    WorkcellParamsFormatError,
    WorkcellParamsMissingError
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
    workcell_provider: str="huggingface",
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
        image_uri (str): docker image uri.
            e.g. image_uri = "weanalyze/hello_workcell:latest"        
        workcell_provider (str): workcell provider.
            e.g. workcell_provider = "huggingface"                
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_runtime (str): workcell runtime.
            e.g. workcell_runtime = "python3.8" 
        workcell_tags (dict): workcell tags.
            e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}'
        workcell_env (dict): workcell env.
            e.g. workcell_env = '{"STAGE":"latest"}'

    Return:
        workcell_config (dict): build config for workcell.
    """
    # extract workcell_config
    try:
        workcell_entrypoint = format_workcell_entrypoint(import_string) # format workcell_entrypoint from import_string
        workcell_name = workcell_entrypoint.split(":")[-1] # a.k.a function_name, "hello_workcell" 
        workcell_version = workcell_version # "latest" | "v1.0.0" | "dev" | "prod"
        workcell_runtime = workcell_runtime # "python3.8" | "python3.9" | "nodejs14.x" | "nodejs12.x"
    except Exception as e:
        raise WorkcellConfigGenerateError(e)
    # workcell code
    try:
        ## TODO: add Docker Hub username support
        # if image_uri == "":
        #     # default build tag: {username}/{workcell_name}:{workcell_version}
        #     image_uri = "{}/{}:{}".format(username, workcell_name, workcell_version) 
        ## ready to deploy
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
        "workcell_name": workcell_name, 
        "workcell_provider": workcell_provider,         
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


