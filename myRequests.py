# File with my requests operations

import requests
from requests.exceptions import ConnectionError

import constants as const
import exceptions


def get_parameters():
    try:
        response = requests.get(const.GET_PARAMS_ADDRESS)
    except ConnectionError:
        raise exceptions.ReceivingError
    else:
        if response.status_code != 200:  # If request is not completed successfully
            raise exceptions.ReceivingError
        return response.json()


if __name__ == "__main__":
    params = get_parameters()
    print(params)
