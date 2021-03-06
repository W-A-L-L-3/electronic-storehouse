# File with server's operations

import pickle

import constants as const
import exceptions
import server.myRequests as myRequests
from server.storehouseModel import ElectronicStorehouse


def init():
    """
    Storehouse initialization.
    Get params and save storehouse object to the file
    :return
    exceptions.RECEIVING_ERROR if an error occurred while getting the parameters
    exceptions.OK if initialization was successful
    """
    try:
        parameters = myRequests.get_parameters()
    except exceptions.GettingParamsError:
        return exceptions.RECEIVING_ERROR
    else:
        storehouse = ElectronicStorehouse(parameters)
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


def storehouse_object(func):
    """
    load storehouse-object from file,
    run func,
    save storehouse-object to the file
    """

    def wrapper(*args, **kwargs):
        storehouse = upload_storehouse()
        res = func(storehouse, *args, **kwargs)
        save_storehouse(storehouse)
        return res

    return wrapper


@storehouse_object
def get_info(storehouse):
    return storehouse.all_items


@storehouse_object
def get_remote_info(storehouse):
    return storehouse.remote_part.all_items


@storehouse_object
def add_items(storehouse, items_list):
    """
    :param storehouse: Object of storehouse
    :param items_list: List of <class 'Item'>
    """
    storehouse.add_items(items_list, add_item_to_the_api)


def add_item_to_the_api(item):
    """
    Send request to the api with info about new item
    """
    myRequests.add_new_item(item)


@storehouse_object
def give_item(storehouse, item_name):
    storehouse.remove_item(item_name, take_item_from_the_api)


def take_item_from_the_api(pos):
    """
    Send request to the api to take item from pos
    """
    myRequests.take_item(pos)
