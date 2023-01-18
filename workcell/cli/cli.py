"""Command line interface."""
import os
import sys
import json
import requests
import dotenv
import typer
from pydantic.error_wrappers import ValidationError

from workcell import __version__ as workcell_version
from workcell.api.fastapi_app import launch_api  # type: ignore
from workcell.ui.streamlit_ui import launch_ui  # type: ignore
from workcell.core.constants import SCAFFOLD_FOLDER, RUNTIME_FOLDER, WORKCELL_API_GATEWAY
from workcell.core.utils import (
    gen_workcell_config, 
    save_workcell_config, 
    load_workcell_config, 
    valid_workcell_import_string
)
from workcell.cli.builder import (
    init_workcell_build_dir, 
    init_workcell_project_dir,
    package_workcell, 
    image_builder, 
    image_pusher
)
from workcell.cli.export import ExportFormat


# Switch to local project directory
# Add the current working directory to the sys path
# This is required to resolve the workcell path
sys.path.append(os.getcwd()) 

# Init weanalyze config directory
weanalyze_config_dir = os.path.join(os.path.expanduser("~"), ".weanalyze")
if not os.path.exists(weanalyze_config_dir):
    os.mkdir(weanalyze_config_dir)
# Load weanalyze global environment variables
weanalyze_dotenv =  os.path.join(os.path.expanduser("~"), ".weanalyze", "env")
if not os.path.exists(weanalyze_dotenv):
    with open(weanalyze_dotenv, "w") as f:
        f.write("WORKCELL_USERNAME=''" + "\n")
        f.write("WORKCELL_TOKEN=''" + "\n")
dotenv.load_dotenv(weanalyze_dotenv)
# Load project environment variables
project_dotenv =  os.path.join(os.getcwd(), ".env")
dotenv.load_dotenv(project_dotenv)


# Typer command
cli = typer.Typer()


# Cli commandas
@cli.command()
def version(
) -> str:
    """Return workcell version.

    This will return the version of workcell package.
    """
    typer.secho(f'workcell-cli version: {workcell_version}', fg=typer.colors.GREEN, err=False)
    return None

@cli.command()
def new(
    project_name: str,
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r")
) -> None:
    """Init a new workcell template.

    This will create a template dir for workcell deployment.
    """
    # user project dir
    project_dir = os.path.join(os.getcwd(), project_name) # "./{project_dir}"
    scaffold_dir = os.path.join(SCAFFOLD_FOLDER, workcell_runtime) # ".../workcell/templates/scaffold/python3.8"
    init_workcell_project_dir(project_dir, scaffold_dir)
    typer.secho(f'Workcell project_dir created: {project_dir}', fg=typer.colors.GREEN, err=False)
    return None


@cli.command()
def serve(
    workcell_path: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a HTTP API server for the workcell.

    This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.
    """
    launch_api(workcell_path, port, host)
    return None


@cli.command()
def serve_ui(
    workcell_path: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a UI server for the workcell.

    This will launch a Streamlit server based on the Pydantic standard.
    """
    launch_ui(workcell_path, port, host)
    return None


@cli.command()
def login(
    username: str = typer.Option("", "--username", "-u"),
    access_token: str = typer.Option("", "--access_token", "-a"),
) -> None:
    """Login into weanalyze.co.
    
    Provide username and access_token to login into weanalyze.co.
    """
    # Verification
    try:    
        # check if already logged in
        if (os.getenv("WORKCELL_USERNAME") == username) and ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            typer.secho("Already logged in ! (username: {})".format(os.environ['WORKCELL_USERNAME']), fg=typer.colors.GREEN, err=False)
            return None
        else:
            if (username == "") and (access_token == ""):
                typer.secho("Please provide username and access_token.", fg=typer.colors.RED, err=True)
                return None
            elif access_token == "":
                access_token = typer.prompt("Access Token", hide_input=True)
                # login params
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}            
                data = {
                    'username': username,
                    'password': access_token
                } 
                # login url
                url = WORKCELL_API_GATEWAY + "/auth/token"
                # login request   
                response = requests.post(url=url, data=data, headers=headers)
                if response.status_code == 200:
                    # extract workcell_token
                    workcell_token = response.json()["access_token"] # long-time cli workcell_token
                    dotenv.set_key(weanalyze_dotenv, "WORKCELL_USERNAME", username)
                    dotenv.set_key(weanalyze_dotenv, "WORKCELL_TOKEN", workcell_token)
                    typer.echo("Login successful! (username: {}).".format(username))
                else:
                    typer.secho("Login failed! (response.status_code: {}, response.text:{}).".format(response.status_code, response.text), fg=typer.colors.RED, err=True) 
            else:
                pass
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    return None


@cli.command()
def build(
    import_string: str,
    image_tag: str = typer.Option("", "--image_tag", "-t"),
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r"),
    workcell_tags: str = typer.Option("{}", "--workcell_tags"),
    workcell_env: str = typer.Option("{}", "--workcell_env"),
) -> str:
    """Prepare deployment image for workcell.

    This will create a deployment folder and build docker image. \n
    Args: \n
        import_string (str): import_string, a.k.a workcell fqdn. \n
            e.g. import_string = "app:hello_workcell" \n
        image_tag (str): docker image tag. \n
            e.g. image_tag = "weanalyze/hello_workcell:latest" \n
            if set to default "", it will be "{username}/{workcell_name}:{workcell_version}" \n
        workcell_version (str): workcell version. \n
            e.g. workcell_version = "latest" \n
        workcell_runtime (str): workcell runtime. \n
            e.g. workcell_runtime = "python3.8" \n
        workcell_tags (dict): workcell tags. \n
            e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' \n
        workcell_env (dict): workcell env. \n
            e.g. workcell_env = '{"STAGE":"latest"}' \n
    Return: \n
        build_dir (str): project build directory. \n
        workcell_config (dict): workcell configuration dict. \n
    """
    # check if environment variable `DOCKERHUB_USERNAME`
    if not os.getenv("DOCKERHUB_USERNAME") or (os.getenv("DOCKERHUB_USERNAME") is None):
        typer.secho("Please set environment variable `DOCKERHUB_USERNAME`.", fg=typer.colors.RED, err=True)
        return None
    dockerhub_username = os.getenv("DOCKERHUB_USERNAME")
    function_name = import_string.split(":")[1]
    image_tag = image_tag if image_tag != "" else "{}/{}:{}".format(dockerhub_username, function_name, workcell_version)
    # check if function_name exists in app.py
    if not valid_workcell_import_string(import_string):
        typer.secho(f"Given function: {function_name} does not exists in app.py.", fg=typer.colors.RED, err=True)
        return None
    # generate workcell_config
    workcell_config = gen_workcell_config(
        import_string = import_string,
        image_uri = image_tag,
        workcell_version = workcell_version,
        workcell_runtime = workcell_runtime, # workcell_runtime in [ "python3.8", ...]
        workcell_tags = workcell_tags,
        workcell_env = workcell_env
    ) 
    # user project dir
    function_dir = os.getcwd() # "./{project_dir}"
    template_dir = os.path.join(RUNTIME_FOLDER, workcell_runtime) # ".../workcell/templates/runtime/python3.8"
    build_dir = os.path.join(os.getcwd(), ".workcell") # "{project_dir}/.workcell/"
    workcell_config_file = os.path.join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"
    
    # init project dir
    if os.path.exists(os.path.join(function_dir,'Dockerfile')):
        typer.secho("Dockerfile exists, will use user-defined docker image.", fg=typer.colors.GREEN, err=False)
        init_workcell_build_dir(
            function_dir=function_dir, 
            build_dir=build_dir,
            runtime_dir=template_dir, 
            exclude_files=["Dockerfile"]
        ) 
    else:
        init_workcell_build_dir(
            function_dir=function_dir, 
            build_dir=build_dir,
            runtime_dir=template_dir
        )         
    # overwrite workcell_config into package_dir
    save_workcell_config(
        workcell_config = workcell_config, 
        dest = workcell_config_file
    ) 
    # build docker image
    image_builder(
        src = build_dir,
        image_uri = workcell_config["workcell_code"]['ImageUri']
    ) 
    # package .workcell into zipfile
    package_workcell(
        build_dir,
        zip_file = os.path.join(build_dir, 'workcell.zip')
    ) 
    typer.secho("Workcell build complete!", fg=typer.colors.GREEN)
    return build_dir, workcell_config


@cli.command()
def push(
    build_dir: str = typer.Option(".workcell", "--build_dir", "-b"),
) -> None:
    """Push image for workcell.
    This will push image to repository based on workcell_config. Must be running in project folder or given build_dir.

    Args: \n
        build_dir (str): project build directory. \n
    Return: \n
        None.
    """
    # load workcell_config
    workcell_config = load_workcell_config(
        src = os.path.join(build_dir, "workcell_config.json")  # "{project_dir}/.workcell/workcell_config.json"  
    ) 
    # load workcell_config    
    image_pusher(
        repository = workcell_config["workcell_code"]['ImageUri']
    ) 
    return None


@cli.command()
def deploy(
    build_dir: str = typer.Option(".workcell", "--build_dir", "-b"),
) -> None:
    """Deploy workcell.
    This will deploy workcell by workcell_config.json in buidl_dir. Must be running in project folder or given build_dir.

    Args: \n
        build_dir (str): project build directory. \n
    Return: \n
        None.
    """
    # load workcell_config
    workcell_config = load_workcell_config(
        src = os.path.join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"  
    )
    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            # auth params
            headers = {
                "Authorization": "Bearer {}".format(os.getenv("WORKCELL_TOKEN")),
            }             
            # auth url 
            url = WORKCELL_API_GATEWAY + "/workcell/deploy"
            # package .workcell, and deploy with workcell_config to weanalyze cloud
            zip_file = os.path.join(build_dir, 'workcell.zip')
            # post to deploy
            with open(zip_file, "rb") as f:
                # request    
                response = requests.post(
                    url=url, 
                    headers=headers, 
                    data={'workcell_config':json.dumps(workcell_config)}, 
                    files={"workcell_zipfile": f} 
                )
            if response.status_code == 200:
                typer.echo("Workcell deployed, response text: {}".format(response.text))    
            else:
                typer.secho("Workcell deploy failed, status code: {}, response text: {}".format(response.status_code, response.text), fg=typer.colors.RED, err=True)
        else:
            typer.secho("Login required!", fg=typer.colors.RED, err=True)
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)    
    return None


@cli.command()
def up(
    import_string: str,
    image_tag: str = typer.Option("", "--image_tag", "-t"),
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r"),
    workcell_tags: str = typer.Option("{}", "--workcell-tags"),
    workcell_env: str = typer.Option("{}", "--workcell-env"),
) -> None:
    """Build->push->deploy a workcell to weanalyze cloud.

    This will create a deployment on weanalyze cloud. \n
    Args: \n
        import_string (str): import_string, a.k.a workcell fqdn. \n
            e.g. import_string = "app:hello_workcell" \n
        image_tag (str): docker image tag. \n
            e.g. image_tag = "weanalyze/hello_workcell:latest" \n
            if set to default "", it will be "{username}/{workcell_name}:{workcell_version}" \n
        workcell_version (str): workcell version. \n
            e.g. workcell_version = "latest" \n
        workcell_runtime (str): workcell runtime. \n
            e.g. workcell_runtime = "python3.8" \n
        workcell_tags (dict): workcell tags. \n
            e.g. workcell_tags = '{"vendor":"aws", "service-type":"http"}' \n
        workcell_env (dict): workcell env. \n
            e.g. workcell_env = '{"STAGE":"latest"}' \n
    Return: \n
        None.
    """
    # Step1. Building
    build_dir, _ = build(
        import_string,
        image_tag,
        workcell_version,
        workcell_runtime,
        workcell_tags,
        workcell_env
    )
    # Step2. Push 
    push(build_dir)    
    # Step3. Deploy
    deploy(build_dir)
    return None
    

@cli.command()
def teardown(
    build_dir: str = typer.Option(".workcell", "--build_dir", "-b"),
) -> None:
    """Teardown a workcell on weanalyze cloud.

    This will delete workcell infra on weanalyze cloud. Must be running in project folder or given build_dir.

    Args: \n
        build_dir (str): project build directory. \n
    Return: \n
        None.
    """
    from workcell.core.utils import load_workcell_config
    # function waiting for deployment
    workcell_config_file = os.path.join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"  
    # load workcell_config
    workcell_config = load_workcell_config(
        src = workcell_config_file
    )
    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            # auth params
            headers = {
                "Authorization": "Bearer {}".format(os.getenv("WORKCELL_TOKEN")),
            }             
            # auth url 
            url = WORKCELL_API_GATEWAY + "/workcell/teardown"
            # post to teardown
            response = requests.post(
                url=url, 
                headers=headers, 
                json=json.dumps(workcell_config),
            )
            if response.status_code == 200:
                typer.echo("Workcell teardown complete, response text: {}".format(response.text))    
            else:
                typer.secho("Workcell teardown failed, status code: {}, response text: {}".format(response.status_code, response.text), fg=typer.colors.RED, err=True)
        else:
            typer.secho("Login required!", fg=typer.colors.RED, err=True)
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    return None


@cli.command()
def export(
    import_string: str, 
    format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export a workcell."""
    if format == ExportFormat.ZIP:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.DOCKER:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.WE:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.PYZ:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )        
    return None


if __name__ == "__main__":
    cli()