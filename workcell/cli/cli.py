"""Command line interface."""
import os
import sys
import dotenv
import typer
from typing import Tuple
from workcell import __version__ as workcell_version
from workcell.core.constants import (
    SUPPORT_PROVIDER,
    SUPPORT_RUNTIME,
    SCAFFOLD_FOLDER, 
    RUNTIME_FOLDER, 
    WORKCELL_SERVER_NAME,
    WORKCELL_SERVER_PORT    
)
from workcell.core.utils import (
    safe_join,
    gen_workcell_config, 
    save_workcell_config, 
    load_workcell_config, 
    valid_workcell_import_string
)
from workcell.deploy.huggingface import HuggingfaceWrapper
from workcell.utils.serve import launch_app, launch_app_socket  # type: ignore
from workcell.cli.builder import (
    init_workcell_build_dir, 
    init_workcell_project_dir
)
from workcell.cli.export import ExportFormat

"""
Set local project directory
"""
# Switch to local project directory
# Add the current working directory to the sys path
# This is required to resolve the workcell path
sys.path.append(os.getcwd()) 

"""
Load environment variables
"""
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

"""
Typer command line tools
"""
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
    workcell_provider: str = typer.Option("huggingface", "--provider", "-p"), # "localhost", "huggingface", "weanalyze"
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r") # "python3.8", "python3.9"
) -> None:
    """Init a new workcell template.
    This will create a template dir for workcell deployment.
    """
    # user project dir
    project_dir = os.path.join(os.getcwd(), project_name) # "./{project_dir}"
    scaffold_dir = os.path.join(SCAFFOLD_FOLDER, workcell_provider, workcell_runtime) # ".../workcell/templates/scaffold/huggingface/python3.8"
    init_workcell_project_dir(project_dir, scaffold_dir)
    typer.secho(f'Workcell project_dir created: {project_dir}', fg=typer.colors.GREEN, err=False)
    return None

@cli.command()
def serve(
    workcell_path: str,
    port: int = typer.Option(int(WORKCELL_SERVER_PORT), "--port", "-p"),
    host: str = typer.Option(str(WORKCELL_SERVER_NAME), "--host", "-h"),
) -> None:
    """Start a HTTP API server for the workcell.
    This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.
    """
    launch_app(workcell_path, port, host)
    # launch_app_socket(workcell_path, port, host)

@cli.command()
def pack(
    import_string: str,
    workcell_provider: str = typer.Option("huggingface", "--provider", "-p"),
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r"),
    workcell_tags: str = typer.Option("{}", "--workcell_tags"),
    workcell_env: str = typer.Option("{}", "--workcell_env"),
) -> Tuple[str, str]:
    """Prepare deployment image for workcell.
    This will create a deployment folder and build docker image. \n
    Args: \n
        import_string (str): import_string, a.k.a workcell fqdn. \n
            e.g. import_string = "app:hello_workcell" \n
        workcell_provider (str): workcell provider. \n
            e.g. workcell_provider = "huggingface" \n            
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
    # check if provider valid
    if workcell_provider not in SUPPORT_PROVIDER:
        typer.secho(f"Given provider: {workcell_provider} is not valid. Please choose from {SUPPORT_PROVIDER}!", fg=typer.colors.RED, err=True)
        return None
    # check if runtime valid
    if workcell_runtime not in SUPPORT_RUNTIME:
        typer.secho(f"Given runtime: {workcell_runtime} is not valid. Please choose from {SUPPORT_RUNTIME}!", fg=typer.colors.RED, err=True)
        return None    
    # function name
    function_name = import_string.split(":")[1]
    # check if function_name exists in app.py
    if not valid_workcell_import_string(import_string):
        typer.secho(f"Import function: {function_name} from app.py failed, check spelling or dependencies.", fg=typer.colors.RED, err=True)
        return None
    # generate workcell_config
    workcell_config = gen_workcell_config(
        import_string = import_string,
        workcell_provider = workcell_provider, # workcell_provider in [ "huggingface", ...]
        workcell_version = workcell_version,
        workcell_runtime = workcell_runtime, # workcell_runtime in [ "python3.8", ...]
        workcell_tags = workcell_tags,
        workcell_env = workcell_env
    ) 
    # user project dir
    function_dir = os.getcwd() # "./{project_dir}"
    build_dir = safe_join(function_dir, ".workcell") # "{project_dir}/.workcell/"
    template_dir = safe_join(RUNTIME_FOLDER, f"{workcell_provider}/{workcell_runtime}") # ".../workcell/templates/runtime/huggingface/python3.8"
    workcell_config_file = safe_join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"
    # init project dir
    if os.path.exists(os.path.join(function_dir,'Dockerfile')):
        typer.secho("Dockerfile exists, will use user-defined docker image.", fg=typer.colors.GREEN, err=False)
        init_workcell_build_dir(
            function_dir=function_dir, 
            build_dir=build_dir,
            runtime_dir=template_dir, 
            exclude_files=["Dockerfile"] # exclude from template_dir
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
    typer.secho("✨ Workcell pack complete!" + "\n" 
                + "Build dir: {}".format(build_dir), fg=typer.colors.GREEN)
    return build_dir, workcell_config

@cli.command()
def deploy(
    build_dir: str = typer.Option(".workcell", "--build_dir", "-b"),
) -> None:
    """Deploy workcell.
    This will deploy workcell by workcell_config.json in buidl_dir. Must be running in project folder or given build_dir.
    Args: \n
        provider (str): service provider, e.g. huggingface. \n
        build_dir (str): project build directory. \n
    Return: \n
        repo_url (str): huggingface repo url.
    """
    # check if environment variable `HUGGINGFACE_USERNAME` and `HUGGINGFACE_TOKEN`
    if not os.getenv("HUGGINGFACE_USERNAME") or (os.getenv("HUGGINGFACE_USERNAME") is None):
        typer.secho("Please set environment variable `HUGGINGFACE_USERNAME`.", fg=typer.colors.RED, err=True)
        return None     
    if not os.getenv("HUGGINGFACE_TOKEN") or (os.getenv("HUGGINGFACE_TOKEN") is None):
        typer.secho("Please set environment variable `HUGGINGFACE_TOKEN`.", fg=typer.colors.RED, err=True)
        return None 
    # load workcell_config
    workcell_config = load_workcell_config(
        src = os.path.join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"  
    )
    # parse workcell_config to deplot resources
    # repo_id = "{}/{}".format(os.getenv("HUGGINGFACE_USERNAME"), workcell_config['workcell_name'])
    repo_id = workcell_config['workcell_id']
    # huggingface hub api wrapper
    hf_wrapper = HuggingfaceWrapper(token=os.getenv("HUGGINGFACE_TOKEN"))
    # check if exsists before create workspace
    space_info = hf_wrapper.get_space(repo_id=repo_id)
    if space_info is not None:
        typer.secho("💥 Failed to create space!" + "\n"
                    + "Provider: {}, repo: {} already exists!".format(workcell_config['workcell_provider'], repo_id), fg=typer.colors.RED, err=True)
        return None
    # create space
    try:
        repo_url = hf_wrapper.create_space(repo_id=repo_id, src_folder="./.workcell/")
        typer.secho("✨ Workcell deploy complete!" + "\n"
                    + "Provider: {}".format(workcell_config['workcell_provider']) + "\n" 
                    + "Endpoint: {}".format(repo_url), fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho("Failed to create space! Exception type: {}, message: {}.".format(type(e), e), fg=typer.colors.RED, err=True)
    return None

@cli.command()
def up(
    import_string: str,
    workcell_provider: str = typer.Option("huggingface", "--provider", "-p"),
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r"),
    workcell_tags: str = typer.Option("{}", "--workcell_tags"),
    workcell_env: str = typer.Option("{}", "--workcell_env"),
) -> None:
    """Build->push->deploy a workcell to weanalyze cloud.
    This will create a deployment folder and build docker image. \n
    Args: \n
        import_string (str): import_string, a.k.a workcell fqdn. \n
            e.g. import_string = "app:hello_workcell" \n
        workcell_provider (str): workcell provider. \n
            e.g. workcell_provider = "huggingface" \n            
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
    # Step1. Pack
    build_dir, _ = pack(
        import_string,
        workcell_provider,
        workcell_version,
        workcell_runtime,
        workcell_tags,
        workcell_env
    ) 
    # Step2. Deploy
    deploy(build_dir)
    return None

@cli.command()
def teardown(
    build_dir: str = typer.Option(".workcell", "--build_dir", "-b"),
) -> None:
    """Teardown workcell deployment.
    This will deploy workcell by workcell_config.json in buidl_dir. Must be running in project folder or given build_dir.
    Args: \n
        build_dir (str): project build directory. \n
    Return: \n
        None.
    """
    # check if environment variable `HUGGINGFACE_USERNAME` and `HUGGINGFACE_TOKEN`
    if not os.getenv("HUGGINGFACE_USERNAME") or (os.getenv("HUGGINGFACE_USERNAME") is None):
        typer.secho("Please set environment variable `HUGGINGFACE_USERNAME`.", fg=typer.colors.RED, err=True)
        return None     
    if not os.getenv("HUGGINGFACE_TOKEN") or (os.getenv("HUGGINGFACE_TOKEN") is None):
        typer.secho("Please set environment variable `HUGGINGFACE_TOKEN`.", fg=typer.colors.RED, err=True)
        return None 
    # load workcell_config
    workcell_config = load_workcell_config(
        src = os.path.join(build_dir, "workcell_config.json") # "{project_dir}/.workcell/workcell_config.json"  
    )
    # parse workcell_config to deplot resources
    # repo_id = "{}/{}".format(os.getenv("HUGGINGFACE_USERNAME"),workcell_config['workcell_name'])
    repo_id = workcell_config['workcell_id']
    # huggingface hub api wrapper
    hf_wrapper = HuggingfaceWrapper(token=os.getenv("HUGGINGFACE_TOKEN"))
    # check if exsists before teardown workspace
    space_info = hf_wrapper.get_space(repo_id=repo_id)
    if space_info is None:
        typer.secho("💥 Failed to teardown space!" + "\n"
                    + "Provider: {}, repo: {} not exists!".format(workcell_config['workcell_provider'], repo_id), fg=typer.colors.RED, err=True)
        return None
    # teardown space
    try:
        repo_url = hf_wrapper.delete_space(repo_id=repo_id)
        typer.secho("✨ Workcell teardown complete!" + "\n"
                    + "Provider: {}".format(workcell_config['workcell_provider']) + "\n" 
                    + "Endpoint: {}".format(repo_url), fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho("Failed to teardown space! Exception type: {}, message: {}.".format(type(e), e), fg=typer.colors.RED, err=True)
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