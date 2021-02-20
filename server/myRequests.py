# File with my requests operations

import json

import requests
from requests.exceptions import ConnectionError, Timeout

import constants as const
import exceptions


def get_parameters():
    """Get parameters of storehouse from API"""
    try:
        response = requests.get(const.GET_PARAMS_ADDRESS, timeout=0.5)
    except (ConnectionError, Timeout):
        raise exceptions.GettingParamsError

    else:
        if response.status_code != 200:  # If request is not completed successfully
            raise exceptions.GettingParamsError
        return response.json()


def add_new_item(item):
    """Send info about new item to the API"""
    try:
        data = {
            "uuid": item.uid,
            "destination": item.pos}
        r = requests.post(const.API_ADDRESS, data=json.dumps(data))
        print(r.status_code, r.reason)
    except (ConnectionError, Timeout):
        pass
    else:
        return exceptions.OK


def take_item(position):
    """Request for getting item from the cell"""
    try:
        data = {
            "destination": position
        }
        r = requests.post(const.API_ADDRESS, data=json.dumps(data))
        print(r.status_code, r.reason)
    except (ConnectionError, Timeout):
        pass
    else:
        return exceptions.OK
