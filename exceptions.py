# File with my exceptions

RECEIVING_ERROR = 1
OK = 0


class GettingParamsError(Exception):
    pass


class EntryContentError(ValueError):
    """Incorrect values in entries"""

    def __init__(self, field, exception_type=""):
        self.field = field  # Field index
        self.exception_type = exception_type


class ItemNotFoundError(Exception):
    pass
