from typing import Any, List, Set
from colorama import Fore, Style


class WorkcellImportStringFormatError(Exception):
    def __init__(self, import_string):
        super().__init__(
            f"The workcell import string is not valid: {import_string}, should be formated as 'project_folder.app:function_name' or 'app:function_name'. "
        )

class WorkcellFunctionNotExistsError(Exception):
    def __init__(self, workcell_name):
        super().__init__(
            f"The function is not exists in app.py: {workcell_name}, please check your function name. "
        )
        
class WorkcellParamsFormatError(Exception):
    def __init__(self, workcell_params):
        super().__init__(
            f"The workcell params is not valid: {workcell_params}, params should be wrapped as string. "
        )

class CallableTypeError(Exception):
    def __init__(self, callable):
        super().__init__(
            f"The callable is not a function or a class: {callable}. "
        )

class DockerBuildError(Exception):
    def __init__(self, docker_build_output: List[str]):
        super().__init__(
            f'Docker build failed, error: \"{docker_build_output}.\"'
        )