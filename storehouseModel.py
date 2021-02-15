# File with storehouse model's class
import pickle

import constants as const


class Storehouse:
    """Storehouse model"""

    def __init__(self, parameters):
        """
        Parameters in format:
        {
          "size":
            {
              "size_x": <size:int>,
              "size_y": <size:int>,
              "size_z": <size:int>
            },
          "merged":
            [
              [<block:string>, <block:string>],
              [<block:string>, <block:string>]
            ]
        }
        """
        size = parameters["size"]
        self.__size = Size(size)
        self.__merged = parameters["merged"]

    def __repr__(self):
        res = f"""
"size":
    "size_x": {self.__size.x},
    "size_y": {self.__size.y},
    "size_z": {self.__size.z}
"merged": {self.__merged}
"""
        return res

    def save(self):
        """Save self-object to the file"""
        with open(const.STOREHOUSE_FILE_NAME, 'wb') as file:
            pickle.dump(self, file)


class Size:
    """Class for storehouse sizes"""

    def __init__(self, size):
        self.x = size["size_x"]
        self.y = size["size_y"]
        self.z = size["size_z"]
