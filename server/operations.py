# File with server's operations

import pickle

import constants as const
import exceptions
import server.myRequests as myRequests
from server.storehouseModel import Storehouse


def init():
    """
    Storehouse initialization.
    Get params ans save storehouse object to the file
    :return
    exceptions.RECEIVING_ERROR if an error occurred while getting the parameters
    exceptions.OK if initialization was successful
    """
    try:
        parameters = myRequests.get_parameters()
    except exceptions.ReceivingError:
        return exceptions.RECEIVING_ERROR
    else:
        storehouse = Storehouse(parameters)
    save_storehouse(storehouse)

    return exceptions.OK


def save_storehouse(storehouse):
    """Save storehouse-object to the file"""
    with open(const.STOREHOUSE_FILE_NAME, 'wb') as file:
        pickle.dump(storehouse, file)


def upload_storehouse():
    """Upload storehouse-object from the file"""
    with open(const.STOREHOUSE_FILE_NAME, 'rb') as file:
        return pickle.load(file)


def get_info():
    storehouse = upload_storehouse()
    return storehouse.all_items

def add_items(items_list):
    """
    :param items_list: List of <class 'Item'>
    """
    for item in items_list:
        print(item)
