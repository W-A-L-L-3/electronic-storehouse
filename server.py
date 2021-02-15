# File with server's operations

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
    storehouse.save()
    return exceptions.OK
