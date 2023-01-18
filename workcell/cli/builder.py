import os
import shutil
import zipfile
import typer
import docker
from workcell.core.errors import DockerBuildError



def package_workcell(
    build_dir: str,
    zip_file: str
) -> None:
    """Package workcell build_dir into zipfile.
    Args:
        build_dir (str): path to workcell build dir.
            e.g. build_dir = ".workcell"
        zip_file (str): path to save zipfile.
            e.g. zip_file = ".workcell/workcell.zip"
    Returns:
        None
    """
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as archive:
        exclude_prefixes = ('__', '.')  # exclusion prefixes
        exclude_suffixes = ('.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.zip')
        for dirpath, dirnames, filenames in os.walk(build_dir):
            # exclude all dirs starting with exclude_prefixes
            dirnames[:] = [d for d in dirnames if not d.startswith(exclude_prefixes)]
            # If you remove something from the 'subdirs' (second parameter) of os.walk() , 
            # os.walk() does not walk into it, that way that entire directory will be skipped. 
            # Details at docs.python.org/3/library/os.html#os.walk
            archive.write(dirpath, arcname=os.path.basename(dirpath))
            for filename in filenames: 
                if not filename.endswith(exclude_suffixes): 
                    abs_path = os.path.join(dirpath, filename)
                    archive.write(abs_path, arcname=os.path.relpath(abs_path, build_dir)) 


def copy_builder(
    src: str, 
    dest: str, 
    clear_before_copy: bool=True, 
    exclude_files: list=None
) -> None:
    """Wrap user function in template

    Args:
        src (str): a folder to user defined function.
            e.g. src = "./examples/hello-workcell"
        dest (str): path to wrap user function into build folder.
            e.g. dest = "./build/function"
        clear_before_copy (bool): if clear dest folder before copy.
        exclude_files (list): list of files to exclude from src.
            e.g. exclude_files = ["Dockerfile"]

    Returns:
        None: mkdir for builder folder.    
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    else:
        if clear_before_copy:
            shutil.rmtree(dest)
            os.makedirs(dest)

    if exclude_files is None:
        exclude_files = ['.*']
    else:
        exclude_files = exclude_files + ['.*']
    
    try:
        if os.path.isfile(src):
            # copy file
            shutil.copy(src, dest)
        else:
            # copy folder
            shutil.copytree(
                src, 
                dest, 
                symlinks=False, 
                ignore=shutil.ignore_patterns(*exclude_files), # exclude hidden files
                ignore_dangling_symlinks=False, 
                dirs_exist_ok=True, 
            )
    except Exception as e:
        raise Exception("Copy builder failed! {}".format(e))


def init_workcell_project_dir(
    project_dir: str, 
    scaffold_dir: str
) -> None:
    """Init workcell project dir.

    Args:
        project_dir (str): path of user function dir.
            e.g. project_dir = "./{project_dir}"         
        scaffold_dir (str): path of template dir.
            e.g. scaffold_dir = ".../workcell/templates/scaffold/python3.8" 
          
    Returns:
        None: Init project dir. 
    """
    # clear existing build folder
    if os.path.exists(project_dir):
        typer.secho(f'Workcell project_dir: \"{project_dir}\" exist!', fg=typer.colors.RED, err=True)   
    # create build folder
    os.makedirs(project_dir)  
    # copy template & function files
    copy_builder(
        src = scaffold_dir,
        dest = project_dir, 
        clear_before_copy=True
    )
    return None


def init_workcell_build_dir(
    function_dir: str, 
    build_dir: str,
    runtime_dir: str,
    exclude_files: list = []
) -> None:
    """Init workcell build folder

    Args:
        function_dir (str): path of user function dir.
            e.g. function_dir = "./{project_dir}"         
        build_dir (str): path to wrap user function into build folder.
            e.g. build_dir = "/{project_dir}/.workcell"
        runtime_dir (str): path of template dir.
            e.g. runtime_dir = ".../workcell/templates/runtime/python3.8" 
        exclude_files (list): list of files to exclude from runtime_dir.
            e.g. exclude_files = ["Dockerfile"]
          
    Returns:
        None: mkdir for builder folder.    
    """
    # clear existing build folder
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)          
    # create build folder
    os.makedirs(build_dir)  
    # copy runtime & function files
    copy_builder(
        src = runtime_dir,
        dest = build_dir, 
        clear_before_copy=False
    )
    copy_builder(
        src = function_dir,
        dest = build_dir,
        clear_before_copy=False
    )
    return None


def image_builder(src: str, image_uri: str, client: docker.APIClient = None) -> None:
    """Wrap user function in template
    Args:
        src (str): path contains Dockerfile to wrap user function into build folder.
            e.g. build_path = "./build/hello-workcell"
        image_uri (str): docker image uri.
            e.g. tags = "weanalyze/workcell:latest"
    Returns:
        None: docker images.
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker build path
    typer.echo("Building docker path: {}".format(src))
    log_generator = client.build(path=src, tag=image_uri, decode=True)
    log_docker_output(log_generator, "Build workcell docker image: {}".format(image_uri))


def image_pusher(repository: str, client: docker.APIClient = None) -> None:
    """Push docker image to docker hub
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker push
    log_generator = client.push(repository=repository, stream=True, decode=True)
    log_docker_output(log_generator, "Pushing workcell docker image to docker hub: {}".format(repository))


def log_subprocess_output(pipe):
    """
    Log output to console from a generator returned from subprocess
    :param pipe: The pipe to log the output of (e.g. subprocess.PIPE)
    """    
    for line in iter(pipe.readline, b''): # b'\n'-separated lines
        typer.echo(f'Running subprocess command: {line.decode("utf-8").strip()}. ')


def log_docker_output(generator, task_name: str = 'docker command execution') -> None:
    """
    Log output to console from a generator returned from docker client
    :param Any generator: The generator to log the output of
    :param str task_name: A name to give the task, i.e. 'Build database image', used for logging
    """
    while True:
        try:
            output = generator.__next__()
            if 'stream' in output:
                if output['stream'] != '\n':
                    output_str = output['stream'].strip('\r\n').strip('\n')
                    typer.echo(output_str)
            elif 'error' in output:
                typer.secho(f'Error from {task_name}, error: \"{output["error"]}\"', fg=typer.colors.RED, err=True)
                raise DockerBuildError(output["error"])
            else:
                pass
        except StopIteration:
            typer.secho(f'{task_name} complete.', fg=typer.colors.GREEN, err=False)
            break
        except ValueError:
            typer.secho(f'Error parsing output from {task_name}: \"{output}\"', fg=typer.colors.RED, err=True)
