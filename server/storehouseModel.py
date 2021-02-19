# File with storehouse model's class
import exceptions as exc


class Size:
    """Class for storehouse sizes"""

    def __init__(self, size):
        self.x = size["size_x"]
        self.y = size["size_y"]
        self.z = size["size_z"]


class Item:
    def __init__(self, name, size, mass, pos):
        """
        :param name: Name of the item <str>
        :param size: Size of the item <tuple> (x, y, z)
        :param mass: Mass of the item <int>
        :param pos: Position of the item <str>
        """
        self.name = name
        self.size = size
        self.mass = mass
        self.pos = pos

    def __repr__(self):
        r = "==========\n"
        n = f"Name: {self.name}, Type: {type(self.name)};\n"
        s = f"Size: {self.size}, Type: {type(self.size)};\n"
        m = f"Mass: {self.mass}, Type: {type(self.mass)};\n"
        p = f"Pos : {self.pos}, Type: {type(self.pos)};\n"
        return r + n + s + m + p + r


class Storehouse:
    def __init__(self):
        self._all_items = []

    @property
    def all_items(self):
        return self._all_items

    def add_items(self, items_list):
        """
        Add items to the storehouse
        :param items_list: list of <class 'Item'>
        """
        self._all_items.extend(items_list)

    def remove_item(self, item_name):
        for item in self._all_items:
            if item.name == item_name:
                self._all_items.remove(item)
                break
        else:
            raise exc.ItemNotFoundError


class ElectronicStorehouse(Storehouse):
    """Electronic storehouse model"""

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
        super().__init__()
        size = parameters["size"]
        self.__size = Size(size)
        self.__merged = parameters["merged"]

        self.remote_part = RemoteStorehouse()

    def __repr__(self):
        res = f"""
"size":
    "size_x": {self.__size.x},
    "size_y": {self.__size.y},
    "size_z": {self.__size.z}
"merged": {self.__merged}
"""
        return res


class RemoteStorehouse(Storehouse):
    def __init__(self):
        super().__init__()
