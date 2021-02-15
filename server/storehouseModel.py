# File with storehouse model's class


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
        self.__all_items = []

        self.__all_items.append(Item("Test", (1, 1, 1), 100))

    def __repr__(self):
        res = f"""
"size":
    "size_x": {self.__size.x},
    "size_y": {self.__size.y},
    "size_z": {self.__size.z}
"merged": {self.__merged}
"""
        return res

    @property
    def all_items(self):
        return self.__all_items


class Size:
    """Class for storehouse sizes"""

    def __init__(self, size):
        self.x = size["size_x"]
        self.y = size["size_y"]
        self.z = size["size_z"]


class Item:
    def __init__(self, name, size, mass):
        """
        :param name: Name of item <str>
        :param size: Size of item <tuple> (x, y, z)
        :param mass: Mass of item <int>
        """
        self.name = name
        self.size = size
        self.mass = mass

    def __repr__(self):
        return f"Name: {self.name}. Size: {self.size}. Mass: {self.mass}"
