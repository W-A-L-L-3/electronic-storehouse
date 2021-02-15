# File with server's operations
import pickle

import constants as const
import exceptions
import myRequests
from storehouseModel import Storehouse


def init():
    """Storehouse initialization"""
    try:
        parameters = myRequests.get_parameters()
    except exceptions.ReceivingError:
        return exceptions.RECEIVING_ERROR
    else:
        storehouse = Storehouse(parameters)

    with open(const.STOREHOUSE_FILE_NAME, 'wb') as f:
        pickle.dump(storehouse, f)
    print(storehouse)
    return exceptions.OK
