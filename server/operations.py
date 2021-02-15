# File with server's operations

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
    storehouse.save()

    return exceptions.OK
