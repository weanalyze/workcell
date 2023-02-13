import os
import dotenv
from typing import List, Optional

from huggingface_hub import HfApi
from huggingface_hub import RepoUrl
from huggingface_hub.hf_api import SpaceInfo

from workcell.core.errors import (
    HuggingfaceCreateRepoError,
    HuggingfaceGetSpaceError,
    HuggingfaceUploadFolderError,
    HuggingfaceDeleteRepoError,
)

IGNORE_PATTERNS = ['__pycache__', '.*', '*.pyc', '*.pyo', '*.pyd', '*.so', '*.dylib', '*.egg-info', '*.egg', '*.dist-info', '*.egg-info', '*.egg', '*.dist-info', '*.git', '*.hg', '*.svn', '*.DS_Store', '*.gitignore', '*.gitattributes', '*.gitmodules', '*.gitkeep']


class HuggingfaceWrapper:

    def __init__(self, endpoint: Optional[str]=None, token: Optional[str]=None) -> None:
        if endpoint:
            self._endpoint = endpoint
        else:
            self._endpoint = "https://huggingface.co"
        self._token = token
        # init
        self.hf_api = HfApi(
            endpoint=self._endpoint, 
            token=self._token, # Token is not persisted on the machine.    
        )
        pass
    
    def list_spaces(self, author: str) -> List[SpaceInfo]:
        # HfApi client api
        spaces = self.hf_api.list_spaces(author=author)
        return spaces
    
    def create_space(
        self, 
        repo_id: str, 
        src_folder: str, 
        ignore_patterns: List[str] = IGNORE_PATTERNS
    ) -> RepoUrl:
        """
        Create a new space and upload a folder to it.
        Params:
        repo_id (str): A namespace (user or an organization) and a repo name separated by a /.
        src_folder (str): The path to the folder to upload.
        Returns:
        repo_url (RepoUrl): The url of the repo.
        """
        # HfApi client api
        try:
            repo_url = self.hf_api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="docker")
        except Exception as e:
            raise HuggingfaceCreateRepoError(e)
        try:
            folder_url = self.hf_api.upload_folder(
                repo_id=repo_id, 
                repo_type="space", 
                folder_path=src_folder,
                ignore_patterns=ignore_patterns
            )
        except Exception as e:
            raise HuggingfaceUploadFolderError(e)
        return repo_url

    def get_space(
        self, 
        repo_id:str
    ) -> SpaceInfo:
        """
        Retrieve space by repo_id.
        Params:
        repo_id (str): A namespace (user or an organization) and a repo name separated by a /.
        Returns:
        space_info (SpaceInfo): The space repository information.
        """
        try:
            space_info = self.hf_api.repo_info(repo_id=repo_id, repo_type="space")
        except Exception as e:
            return None
        return space_info

    def update_space(
        self, 
        repo_id:str, 
        src_folder:str,
        ignore_patterns: List[str] = IGNORE_PATTERNS
    ) -> RepoUrl:
        """
        TODO: Need further update.
        Update space by upload folder.
        Params:
        repo_id (str): A namespace (user or an organization) and a repo name separated by a /.
        src_folder (str): The path to the folder to upload.
        Returns:
        folder_url (str): A URL to visualize the uploaded folder on the hub
        """
        try:
            folder_url = self.hf_api.upload_folder(
                repo_id=repo_id, 
                repo_type="space", 
                folder_path=src_folder,
                ignore_patterns=ignore_patterns
            )
        except Exception as e:
            raise HuggingfaceUploadFolderError(e)
        return folder_url

    def delete_space(self, repo_id:str) -> None:
        """
        Delete space by repo_id.
        Params:
        repo_id (str): A namespace (user or an organization) and a repo name separated by a /.
        Returns:
        None
        """        
        try:
            self.hf_api.delete_repo(repo_id=repo_id, repo_type="space")
        except Exception as e:
            raise HuggingfaceDeleteRepoError(e) 
        return None
        