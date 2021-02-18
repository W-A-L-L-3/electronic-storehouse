# File with widget's classes

import tkinter as tk

import constants as const
import exceptions
import exceptions as exc
import text
from gui import messageboxes as mb, style
from server.storehouseModel import Item


class MainMenu(tk.Frame):
    def __init__(self, window, init_func, add_func, info_func, take_func, remote_info_func):
        super().__init__(window)
        self.__init_func = init_func
        self.__add_func = add_func
        self.__info_func = info_func
        self.__take_func = take_func
        self.__remote_info_func = remote_info_func

        self.__init_btn = tk.Button(self,
                                    text=text.main_menu["init"],
                                    font=style.Btn.font,
                                    width=style.Btn.big_width,
                                    command=self.__call_init)

        self.__add_btn = tk.Button(self,
                                   text=text.main_menu["add"],
                                   font=style.Btn.font,
                                   width=style.Btn.big_width,
                                   state=tk.DISABLED,
                                   command=self.__add_func)

        self.__info_btn = tk.Button(self,
                                    text=text.main_menu["info"],
                                    font=style.Btn.font,
                                    width=style.Btn.big_width,
                                    state=tk.DISABLED,
                                    command=self.__info_func)

        self.__take_btn = tk.Button(self,
                                    text=text.main_menu["take"],
                                    font=style.Btn.font,
                                    width=style.Btn.big_width,
                                    state=tk.DISABLED,
                                    command=self.__take_func)

        self.__remote_info_btn = tk.Button(self,
                                           text=text.main_menu["remote_info"],
                                           font=style.Btn.font,
                                           width=style.Btn.big_width,
                                           state=tk.DISABLED,
                                           command=self.__remote_info_func)

    def __call_init(self):
        """Call init function and show results"""
        result = self.__init_func()
        if result == exceptions.OK:
            mb.InfoMb(title=text.successful_init["title"],
                      message=text.successful_init["message"]).show()
            self.__activate_btns()
        elif result == exceptions.RECEIVING_ERROR:
            mb.ErrorMb(title=text.receiving_error["title"],
                       message=text.receiving_error["message"]).show()

    def __activate_btns(self):
        """Activate buttons for interacting with storehouse"""
        self.__init_btn["state"] = tk.DISABLED
        self.__add_btn["state"] = tk.ACTIVE
        self.__info_btn["state"] = tk.ACTIVE
        self.__take_btn["state"] = tk.ACTIVE
        self.__remote_info_btn["state"] = tk.ACTIVE

    def draw(self):
        self.__init_btn.pack(pady=style.Btn.pady)
        self.__add_btn.pack(pady=style.Btn.pady)
        self.__info_btn.pack(pady=style.Btn.pady)
        self.__take_btn.pack(pady=style.Btn.pady)
        self.__remote_info_btn.pack(pady=style.Btn.pady)
        self.pack(padx=20, pady=15)


class InfoTable(tk.Frame):
    def __init__(self, window, table, need_pos_column):
        super().__init__(window)
        self.__header = Header(self, need_pos_column=need_pos_column)
        self.__list = []
        for i in range(len(table)):
            self.__list.append(InfoRow(self, table[i], (1 + i), need_pos_column))

    def draw(self):
        self.__header.draw()
        for row in self.__list:
            row.draw()
        self.pack(padx=15, pady=(5, 15))


class Header:
    def __init__(self, window, need_pos_column=False):
        self.__number = tk.Label(window,
                                 text=text.info_header[0],
                                 font=style.font_name)
        self.__name = tk.Label(window,
                               text=text.info_header[1],
                               font=style.font_name)
        self.__size = tk.Label(window,
                               text=text.info_header[2],
                               font=style.font_name)
        self.__mass = tk.Label(window,
                               text=text.info_header[3],
                               font=style.font_name)
        if need_pos_column:
            self.__pos = tk.Label(window,
                                  text=text.info_header[4],
                                  font=style.font_name)
        else:
            self.__pos = None

    def draw(self):
        self.__number.grid(row=0, column=0,
                           padx=(0, style.InfoTable.padx), pady=(0, style.InfoTable.pady * 2),
                           sticky=tk.W)
        self.__name.grid(row=0, column=1,
                         padx=style.InfoTable.padx, pady=(0, style.InfoTable.pady * 2))
        self.__size.grid(row=0, column=2,
                         padx=style.InfoTable.padx, pady=(0, style.InfoTable.pady * 2))
        self.__mass.grid(row=0, column=3,
                         padx=style.InfoTable.padx, pady=(0, style.InfoTable.pady * 2))

        if self.__pos is not None:
            self.__pos.grid(row=0, column=4,
                            padx=(style.InfoTable.padx, 0), pady=(0, style.InfoTable.pady * 2))


class InfoRow:

    def __init__(self, window, item, row_ind, need_pos_column):
        """
        :param item: <class 'server.storehouseModel.Item'>
        """
        self.__row_ind = row_ind

        self.__number = tk.Label(window,
                                 text=str(self.__row_ind),
                                 font=style.font_name)

        self.__name = tk.Label(window,
                               text=item.name,
                               font=style.font_name,
                               justify=tk.LEFT)

        self.__size = tk.Label(window,
                               text=f"{item.size[0]}*{item.size[1]}*{item.size[2]}",
                               font=style.font_name)

        self.__mass = tk.Label(window,
                               text=item.mass,
                               font=style.font_name)
        if need_pos_column:
            self.__pos = tk.Label(window,
                                  text=item.pos,
                                  font=style.font_name)
        else:
            self.__pos = None

    def draw(self):
        self.__number.grid(row=self.__row_ind, column=0,
                           padx=(0, style.InfoTable.padx), pady=style.InfoTable.pady)
        self.__name.grid(row=self.__row_ind, column=1,
                         padx=style.InfoTable.padx, pady=style.InfoTable.pady,
                         sticky=tk.W)
        self.__size.grid(row=self.__row_ind, column=2,
                         padx=style.InfoTable.padx, pady=style.InfoTable.pady)
        self.__mass.grid(row=self.__row_ind, column=3,
                         padx=style.InfoTable.padx, pady=style.InfoTable.pady)
        if self.__pos is not None:
            self.__pos.grid(row=self.__row_ind, column=4,
                            padx=(style.InfoTable.padx, 0), pady=style.InfoTable.pady)


def exceptions_tracker(func):
    def wrapper(*args):
        try:
            items_list = func(*args)
        except exc.EntryContentError as e:
            mb.ExceptionMb(e).show()
        else:
            return items_list

    return wrapper


class AddingWList(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.__header = Header(self, need_pos_column=False)
        self.__list = []
        self.__list.append(AddingWRow(self, row_ind=1))

    def add_row(self):
        row = 1 + len(self.__list)
        if row <= const.MAX_ADDING_ITEMS:
            self.__list.append(AddingWRow(self, row_ind=row))
            self.__list[-1].draw()

    def draw(self):
        self.__header.draw()
        for row in self.__list:
            row.draw()
        self.pack(padx=(10, 15), pady=(10, 15))

    @exceptions_tracker
    def get_list(self):
        """Return list of items, info about witch in entries"""
        items_list = []
        for row in self.__list:
            name = row.formatted_name()
            size = row.formatted_size()
            mass = row.formatted_mass()
            items_list.append(Item(name, size, mass, pos=None))
        return items_list


class AddingWRow:

    @staticmethod
    def __check_name(value):
        """
        Check value of field 'name'.
        :return: True if it is correct, else False
        """
        return value != ""

    @staticmethod
    def __check_size(value):
        """
        Check value of field 'size'.
        :return: True if it is correct, else False
        """
        seps = value.count("*") == 2
        vals = False
        if seps:
            v = value.split("*")
            vals = len(v) == 3 and v[0].isdigit() and v[1].isdigit() and v[2].isdigit()
        return seps and vals

    @staticmethod
    def __check_mass(value):
        """
        Check value of field 'mass'.
        :return: True if it is correct, else False
        """
        try:
            a = float(value)
        except ValueError:
            return False
        else:
            return True

    def __init__(self, window, row_ind):
        self.__row_ind = row_ind

        self.__number = tk.Label(window,
                                 text=str(self.__row_ind),
                                 font=style.font_name)

        self.__name = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.name_f_width)

        self.__size = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.size_f_width)

        self.__mass = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.mass_f_width)

        self.__name.bind("<Leave>", self.__color_name)
        self.__size.bind("<Leave>", self.__color_size)
        self.__mass.bind("<Leave>", self.__color_mass)

    def draw(self):
        self.__number.grid(row=self.__row_ind, column=0,
                           padx=style.Entry.padx, pady=style.Entry.pady)
        self.__name.grid(row=self.__row_ind, column=1,
                         padx=style.Entry.padx, pady=style.Entry.pady)
        self.__size.grid(row=self.__row_ind, column=2,
                         padx=style.Entry.padx, pady=style.Entry.pady)
        self.__mass.grid(row=self.__row_ind, column=3,
                         padx=style.Entry.padx, pady=style.Entry.pady)

    def __get_name(self):
        """Return str value of field 'name'"""
        value = str(self.__name.get())
        return value

    def __get_size(self):
        """Return str value of field 'size'"""
        value = str(self.__size.get())
        return value

    def __get_mass(self):
        """Return str value of field 'mass'"""
        value = str(self.__mass.get())
        return value

    def formatted_name(self):
        """
        :return: name in str if it is correct
        """
        value = self.__get_name()
        if self.__check_name(value):
            return value
        else:
            raise exc.EntryContentError(const.AddingW.NAME_INDEX)

    def formatted_size(self):
        """
        :return: size in tuple(x, y, z) if it is correct
        """
        value = self.__get_size()
        if self.__check_size(value):
            t = value.split("*")
            return tuple(t)
        else:
            raise exc.EntryContentError(const.AddingW.SIZE_INDEX)

    def formatted_mass(self):
        """
        :return: mass in int if it is correct
        """
        value = self.__get_mass()
        if self.__check_mass(value):
            return int(value)
        else:
            raise exc.EntryContentError(const.AddingW.MASS_INDEX)

    def __color_name(self, event):
        """

        If it is correct, fill entry green, else red
        """
        value = self.__get_name()
        if self.__check_name(value):
            self.__name["bg"] = style.Entry.ok_color
        else:
            self.__name["bg"] = style.Entry.warning_color

    def __color_size(self, event):
        """
        Check value in field 'size'.
        If it is correct, fill entry green, else red
        """
        value = self.__get_size()
        if self.__check_size(value):
            self.__size["bg"] = style.Entry.ok_color
        else:
            self.__size["bg"] = style.Entry.error_color

    def __color_mass(self, event):
        """
        Check value in field 'mass'.
        If it is correct, fill entry green, else red
        """
        value = self.__get_mass()
        if self.__check_mass(value):
            self.__mass["bg"] = style.Entry.ok_color
        else:
            self.__mass["bg"] = style.Entry.error_color


class AddingWButtons(tk.Frame):

    def __init__(self, window, enter_func, add_row_func):
        super().__init__(window)

        self.__enter_button = tk.Button(self,
                                        text=text.enter_btn,
                                        font=style.Btn.font,
                                        width=style.Btn.small_width,
                                        command=enter_func)

        self.__add_row_button = tk.Button(self,
                                          text=text.add_row_btn,
                                          font=style.Btn.font,
                                          width=style.Btn.small_width,
                                          command=add_row_func)

    def draw(self):
        self.__enter_button.pack(side=tk.RIGHT, padx=(10, 0))
        self.__add_row_button.pack(side=tk.RIGHT)
        self.pack(pady=(0, 10), padx=(0, 15), side=tk.RIGHT)


class GivingWWidgets(tk.Frame):
    def __init__(self, window, give_func):
        super().__init__(window)
        self.__give_func = give_func
        self.__label = tk.Label(self,
                                text=text.info_header[1],
                                font=style.font)

        self.__field = tk.Entry(self,
                                font=style.Entry.font,
                                width=style.Entry.name_f_width)

        self.__button = tk.Button(self,
                                  text=text.take_btn,
                                  font=style.Btn.font,
                                  width=style.Btn.small_width,
                                  command=self.__give_func)

    def get_name(self):
        """
        :return: value of entry
        """
        return str(self.__field.get())

    def draw(self):
        self.__label.pack(pady=(0, 5))
        self.__field.pack(pady=(0, 10))
        self.__button.pack()
        self.pack(padx=15, pady=10)
