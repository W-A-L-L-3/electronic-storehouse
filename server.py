# File with server's operations
import pickle

import constants as const
from storehouseModel import Storehouse


def init():
    """Storehouse initialization"""
    storehouse = Storehouse()
    with open(const.STOREHOUSE_FILE_NAME, 'wb') as f:
        pickle.dump(storehouse, f)
    print("save")
