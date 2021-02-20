# File with storehouse model's class
import uuid

import constants as const
import exceptions as exc


class Size:
    """Class for storehouse sizes"""

    def __init__(self, size):
        self.x = size["size_x"]
        self.y = size["size_y"]
        self.z = size["size_z"]


class Item:

    @staticmethod
    def __gen_uid(name):
        """Generate UID(user identifier) by name"""
        uid = uuid.uuid5(uuid.NAMESPACE_X500, name)
        return str(uid.hex)

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

        self.__uid = self.__gen_uid(self.name)

    @property
    def uid(self):
        return self.__uid

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

    def add_items(self, items_list, send_to_the_api):
        """
        Add items to the storehouse
        :param items_list: list of <class 'Item'>
        """
        for item in items_list:
            self._add_item(item)

    def _add_item(self, item):
        """
        Add item to the storehouse
        :param item: <class 'Item'>
        """
        self._all_items.append(item)

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

    def add_items(self, items_list, send_to_the_api):
        """Add new item from the items_list"""
        for item in items_list:
            item.pos = self.__add_item_to_the_storage(item)
            if item.pos == const.Cell.REMOTE:
                self.remote_part._add_item(item)
            else:
                super()._add_item(item)
                send_to_the_api(item)

    def remove_item(self, item_name):
        try:
            super().remove_item(item_name)
        except exc.ItemNotFoundError:
            self.remote_part.remove_item(item_name)

    def __repr__(self):
        res = f"""
"size":
"size_x": {self.__size.x},
"size_y": {self.__size.y},
"size_z": {self.__size.z}
"merged": {self.__merged}
"""
        return res

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

    @staticmethod
    def __gen_cell_name(m_list):
        """Generate cell's group name by list of cell, which are combined into a group"""
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

    def __add_item_to_the_storage(self, new_item):
        """Add item object to the storage-dict and return its position"""
        all_1_is_busy = False
        all_2_is_busy = False

        for cell in self.__storage:
            if self.__storage[cell].item is None:
                item_type = self.__get_item_type(new_item.size)
                cell_type = self.__storage[cell].cell_type

                fill_1, fill_2, fill_3 = self.__check_fill(cell_type, item_type,
                                                           all_1_is_busy, all_2_is_busy)
                if fill_1 or fill_2 or fill_3:
                    new_item.pos = cell
                    self.__storage[cell].item = new_item
                    return cell

                # If not located on this iteration
                if item_type == const.Cell.TYPE_1:
                    all_1_is_busy = True

                if item_type == const.Cell.TYPE_2:
                    all_2_is_busy = True

        return const.Cell.REMOTE  # If not located

    @staticmethod
    def __check_fill(cell_type, item_type, all_1_is_busy, all_2_is_busy):
        """Checking for fill 1 or 2 or 3"""
        fill_1 = cell_type == const.Cell.TYPE_1 == item_type

        fill_2 = (cell_type == const.Cell.TYPE_2 and
                  ((item_type == const.Cell.TYPE_2) or
                   (item_type == const.Cell.TYPE_1 and all_1_is_busy)))

        fill_3 = (cell_type == const.Cell.TYPE_3 and
                  ((item_type == const.Cell.TYPE_3) or
                   (item_type in (const.Cell.TYPE_2, const.Cell.TYPE_1)
                    and all_1_is_busy and all_2_is_busy)))

        return fill_1, fill_2, fill_3

    @staticmethod
    def __get_item_type(size):
        """
        :param size: Size of item
        :return: Type of cell, in with item with this size may be located
        """
        items_sizes_combo = [(size[0], size[1], size[2]),
                             (size[1], size[0], size[2]),
                             (size[0], size[2], size[1]),
                             (size[2], size[1], size[0])]

        large_in_all = True
        any_big = False
        any_medium = False
        any_small = False

        for size in items_sizes_combo:
            large = (size[0] >= const.Cell.TYPE_3[0]
                     or size[1] >= const.Cell.TYPE_3[0]
                     or size[1] >= const.Cell.TYPE_3[0])
            large_in_all = large_in_all or large

            big = (const.Cell.TYPE_1[0] <= size[0] <= const.Cell.TYPE_3[0]
                   and const.Cell.TYPE_2[1] <= size[1] <= const.Cell.TYPE_3[1]
                   and size[2] <= const.Cell.TYPE_3[2])
            if big:
                any_big = True

            med = (const.Cell.TYPE_1[0] <= size[0] <= const.Cell.TYPE_2[0]
                   and size[1] <= const.Cell.TYPE_1[1]
                   and size[2] <= const.Cell.TYPE_2[2])
            if med:
                any_medium = True

            small = (size[0] <= const.Cell.TYPE_1[0]
                     and size[1] <= const.Cell.TYPE_1[1]
                     and size[2] <= const.Cell.TYPE_1[2])
            if small:
                any_small = True

        if any_small:
            return const.Cell.TYPE_1
        if any_medium:
            return const.Cell.TYPE_2
        if any_big:
            return const.Cell.TYPE_3
        if large_in_all:
            return const.Cell.REMOTE

        raise ValueError(f"No type defined for the size: {size}")


class RemoteStorehouse(Storehouse):
    def __init__(self):
        super().__init__()
