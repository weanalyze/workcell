from typing import Any, List, Set
from colorama import Fore, Style


class Error(Exception):
    """Error base, use Error for user, Exception for us:)"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)

class WorkcellImportStringFormatError(Error):
    """Raised when a Workcell function can not be imported by import_string."""
    def __init__(self, import_string):
        super().__init__(
            f"The workcell import string is not valid: {import_string}, should be formated as 'project_folder.app:function_name' or 'app:function_name'. "
        )

class WorkcellFunctionNotExistsError(Error):
    """Raised when a Workcell function is not exists in app.py."""
    def __init__(self, workcell_name):
        super().__init__(
            f"The function is not exists in app.py: {workcell_name}, please check your function name. "
        )
        
class WorkcellParamsFormatError(Error):
    """Raised when a Workcell parameters is not valid."""
    def __init__(self, workcell_params):
        super().__init__(
            f"The workcell params is not valid: {workcell_params}, params should be wrapped as string. "
        )

class CallableTypeError(Error):
    """Raised when a Workcell function is not callable."""
    def __init__(self, callable):
        super().__init__(
            f"The callable is not a function or a class: {callable}. "
        )

class DockerBuildError(Error):
    """Raised when a Workcell docker container build failed."""
    def __init__(self, docker_build_output: List[str]):
        super().__init__(
            f'Docker build failed, error: \"{docker_build_output}.\"'
        )
