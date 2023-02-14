
from __future__ import annotations
import re
import requests


def get_hf_host(
    space_name: str, 
    api_key: str | None = None, 
    **kwargs
) -> str:
    # fetching url
    space_url = "https://huggingface.co/spaces/{}".format(space_name)
    host_url = "https://huggingface.co/api/spaces/{}/host".format(space_name)

    # headers
    headers = {}
    if api_key is not None:
        headers["Authorization"] = f"Bearer {api_key}"

    # requests
    resp = requests.get(host_url, headers=headers).json()
    # extract host
    subdomain, host = resp.get("subdomain"), resp.get("host")

    if host is None:
        raise ValueError(
            f"Could not find Space: {space_name}. If it is a private or gated Space, please provide your Hugging Face access token (https://huggingface.co/settings/tokens) as the argument for the `api_key` parameter."
        )
    
    return host
