# File with widget's classes

import tkinter as tk

import constants as const
import exceptions
import text
from gui import messageboxes as mb, style


class MainMenu(tk.Frame):
    def __init__(self, window, init_func, add_func, info_func):
        super().__init__(window)
        self.__init_func = init_func
        self.__add_func = add_func
        self.__info_func = info_func
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

        self.__remove_btn = tk.Button(self,
                                      text=text.main_menu["remove"],
                                      font=style.Btn.font,
                                      width=style.Btn.big_width,
                                      state=tk.DISABLED)

        self.__remote_info_btn = tk.Button(self,
                                           text=text.main_menu["remote_info"],
                                           font=style.Btn.font,
                                           width=style.Btn.big_width,
                                           state=tk.DISABLED)

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
        self.__add_btn["state"] = tk.ACTIVE
        self.__info_btn["state"] = tk.ACTIVE
        self.__remove_btn["state"] = tk.ACTIVE
        self.__remote_info_btn["state"] = tk.ACTIVE

    def draw(self):
        self.__init_btn.pack(pady=style.Btn.pady)
        self.__add_btn.pack(pady=style.Btn.pady)
        self.__info_btn.pack(pady=style.Btn.pady)
        self.__remove_btn.pack(pady=style.Btn.pady)
        self.__remote_info_btn.pack(pady=style.Btn.pady)
        self.pack(padx=20, pady=15)


class InfoTable(tk.Frame):
    def __init__(self, window, table):
        super().__init__(window)
        self.__header = Header(self, need_pos_column=True)
        self.__list = []
        for i in range(len(table)):
            self.__list.append(InfoRow(self, table[i], (1 + i)))

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

    def __init__(self, window, item, row_ind):
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

        self.__pos = tk.Label(window,
                              text=item.pos,
                              font=style.font_name)

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
        self.__pos.grid(row=self.__row_ind, column=4,
                        padx=(style.InfoTable.padx, 0), pady=style.InfoTable.pady)


class AddingWRows(tk.Frame):

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


class AddingWRow:

    def __init__(self, window, row_ind):
        self.__row_ind = row_ind

        self.__number = tk.Label(window,
                                 text=str(self.__row_ind),
                                 font=style.font_name)

        self.__name = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.big_width)

        self.__size = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.big_width)

        self.__mass = tk.Entry(window,
                               font=style.Entry.font,
                               width=style.Entry.small_width)

    def draw(self):
        self.__number.grid(row=self.__row_ind, column=0,
                           padx=style.Entry.padx, pady=style.Entry.pady)
        self.__name.grid(row=self.__row_ind, column=1,
                         padx=style.Entry.padx, pady=style.Entry.pady)
        self.__size.grid(row=self.__row_ind, column=2,
                         padx=style.Entry.padx, pady=style.Entry.pady)
        self.__mass.grid(row=self.__row_ind, column=3,
                         padx=style.Entry.padx, pady=style.Entry.pady)


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
