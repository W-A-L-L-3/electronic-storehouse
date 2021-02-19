# File with storehouse model's class
import constants as const
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
        self._all_items = []  # List of items <class 'Item'>

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


class StorehouseCell:
    def __init__(self, cell_type, item):
        self.cell_type = cell_type
        self.item = item


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
        self.remote_part = RemoteStorehouse()

        size = parameters["size"]
        self.__size = Size(size)
        self.__merged = parameters["merged"]

        self.__storage = self.__gen_storage()

    def __gen_storage(self):
        """
        Generate storage dictionary.
        d[cell_name] = StorehouseCell(cell_type, Item)
        """
        storage_dict = dict()
        for i in range(self.__size.x):
            letter = chr(ord("A") + i)
            for j in range(self.__size.y):
                storage_dict[letter + str(j + 1)] = StorehouseCell(const.Cell.TYPE_1, None)

        for m_list in self.__merged:
            for cell in m_list:
                storage_dict.pop(cell, None)
            if len(m_list) == 2:
                c_name = self.__gen_cell_name(m_list)
                storage_dict[c_name] = StorehouseCell(const.Cell.TYPE_2, None)
            elif len(m_list) == 4:
                c_name = self.__gen_cell_name(m_list)
                storage_dict[c_name] = StorehouseCell(const.Cell.TYPE_3, None)
            else:
                raise TypeError("len(m_list) != 2 and != 4")
        return storage_dict

    def __gen_cell_name(self, m_list):
        first_letter = m_list[0][0]
        first_num = m_list[0][1]
        second_letter = m_list[-1][0]
        second_num = m_list[-1][1]

        if len(m_list) == 2:
            if first_letter == second_letter:
                letter = first_letter
                num = str(min(first_num, second_num)) + "-" + str(max(first_num, second_num))
                return letter + num

            elif first_num == second_num:
                letter = min(first_letter, second_letter) + "-" + max(first_letter, second_letter)
                num = first_num
                return letter + num
            else:
                raise ValueError("Error with type_2 cell")

        elif len(m_list) == 4:
            letter = min(first_letter, second_letter) + "-" + max(first_letter, second_letter)
            num = str(min(first_num, second_num)) + "-" + str(max(first_num, second_num))
            return letter + num

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
