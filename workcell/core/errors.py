from typing import Any, List, Set
from colorama import Fore, Style


###############
# Workcell Building
###############

class Error(Exception):
    """Error base, use Error for user, Exception for us:)"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)

class WorkcellConfigFormatError(Error):
    """Raised when a Workcell config format invalid."""
    def __init__(self, msg):
        super().__init__(
            f"The workcell config format invalid: {msg}. "
        )

class WorkcellConfigGenerateError(Error):
    """Raised when a Workcell config generated failed."""
    def __init__(self, msg):
        super().__init__(
            f"The workcell config generate failed: {msg}. "
        )

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
    def __init__(self, msg):
        super().__init__(
            f"The workcell config params generate failed: {msg}, params should be wrapped as string, or there're something missing (username/provider etc.). "
        )

class WorkcellParamsMissingError(Error):
    """Raised when a Workcell parameters is missing."""
    def __init__(self, workcell_params):
        super().__init__(
            f"There're something missing in workcell configs: {workcell_params}, username / provider / ... etc. "
        )

class CallableTypeError(Error):
    """Raised when a Workcell function is not callable."""
    def __init__(self, callable):
        super().__init__(
            f"This function is not callable because it is either stateful or is a generator. Function name: {callable}. "
        )

class DockerBuildError(Error):
    """Raised when a Workcell docker container build failed."""
    def __init__(self, docker_build_output: List[str]):
        super().__init__(
            f'Docker build failed, error: \"{docker_build_output}.\"'
        )

###############
# Main Routes
###############

class TemplateNotFoundError(Error):
    """Raised when a Template file not found."""
    def __init__(self, msg):
        super().__init__(
            f"Workcell ui template not found: {msg}. "
        )


class WorkcellProviderInvalidError(Error):
    """Raised when a workcell's provider is invalid."""
    def __init__(self, msg):
        super().__init__(
            f"Workcell provider invalid: {msg}. "
        )

###############
# Deployment: Huggingface Space
###############

class HuggingfaceCreateRepoError(Error):
    """Raised when a huggingface space repo create failed."""
    def __init__(self, msg):
        super().__init__(
            f"Huggingface space repo create failed: {msg}. "
        )

class HuggingfaceGetSpaceError(Error):
    """Raised when a huggingface space get failed."""
    def __init__(self, msg):
        super().__init__(
            f"Huggingface space get failed: {msg}. "
        )

class HuggingfaceUploadFolderError(Error):
    """Raised when a huggingface space upload folder failed."""
    def __init__(self, msg):
        super().__init__(
            f"Huggingface space upload folder failed: {msg}. "
        )

class HuggingfaceDeleteRepoError(Error):
    """Raised when a huggingface space delete repo failed."""
    def __init__(self, msg):
        super().__init__(
            f"Huggingface space delete repo failed: {msg}. "
        )