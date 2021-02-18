# File with my requests operations

import requests
from requests.exceptions import ConnectionError, Timeout

import constants as const
import exceptions


def get_parameters():
    """Get parameters of storehouse from API"""
    try:
        response = requests.get(const.GET_PARAMS_ADDRESS, timeout=0.5)
    except (ConnectionError, Timeout):
        raise exceptions.ReceivingError

    else:
        if response.status_code != 200:  # If request is not completed successfully
            raise exceptions.ReceivingError
        return response.json()
