# File with constants

STOREHOUSE_FILE_NAME = 'storehouse.pickle'

API_ADDRESS = 'http://127.0.0.1:5000'
GET_PARAMS_ADDRESS = f'{API_ADDRESS}/scheme'

MAX_ADDING_ITEMS = 30  # Maximum number of rows on one adding-window


class AddingW:
    NAME_INDEX = 1
    SIZE_INDEX = 2
    MASS_INDEX = 3


class Cell:
    """Size of storehouse's cells"""
    TYPE_1 = (1000, 1000, 1000)
    TYPE_2 = (2000, 1000, 1000)
    TYPE_3 = (2000, 2000, 1000)

    REMOTE = "REMOTE"


class ItemsSizes:
    SMALL = "small"
    MEDIUM = "medium"
    BIG = "big"
    LARGE = "large"
