import os
from typing import Optional, List

from fastapi import Header

from config import config


def api_keys_in_env() -> List[Optional[str]]:
    api_keys = []

    for key in os.environ.keys():
        if key.startswith(config.API_KEY_PREFIX):
            api_keys.append(os.getenv(key))

    return api_keys


def get_api_key(x_api_key: Optional[str] = Header(...)) -> Optional[str]:
    if x_api_key not in api_keys_in_env():
        return None
    return x_api_key
