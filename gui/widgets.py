# File with widget's classes

import tkinter as tk

import exceptions
import text
from gui import messageboxes as mb, style


class MainMenu(tk.Frame):
    def __init__(self, window, init_func, info_func):
        super().__init__(window)
        self.__init_func = init_func
        self.__info_func = info_func
        self.__init_btn = tk.Button(self,
                                    text=text.main_menu["init"],
                                    font=style.Btn.font,
                                    width=style.Btn.width,
                                    command=self.__call_init)

        self.__add_btn = tk.Button(self,
                                   text=text.main_menu["add"],
                                   font=style.Btn.font,
                                   width=style.Btn.width,
                                   state=tk.DISABLED)

        self.__info_btn = tk.Button(self,
                                    text=text.main_menu["info"],
                                    font=style.Btn.font,
                                    width=style.Btn.width,
                                    state=tk.DISABLED,
                                    command=self.__info_func)

        self.__remove_btn = tk.Button(self,
                                      text=text.main_menu["remove"],
                                      font=style.Btn.font,
                                      width=style.Btn.width,
                                      state=tk.DISABLED)

        self.__remote_info_btn = tk.Button(self,
                                           text=text.main_menu["remote_info"],
                                           font=style.Btn.font,
                                           width=style.Btn.width,
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
        self.__header = Header(self)
        self.__list = []
        for i in range(len(table)):
            self.__list.append(InfoRow(self, table[i], (1 + i)))

    def draw(self):
        self.__header.draw()
        for row in self.__list:
            row.draw()
        self.pack(padx=15, pady=(5, 15))


class Header:
    def __init__(self, window):
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

    def draw(self):
        self.__number.grid(row=0, column=0)
        self.__name.grid(row=0, column=1)
        self.__size.grid(row=0, column=2)
        self.__mass.grid(row=0, column=3)


class InfoRow:

    def __init__(self, window, item, row_ind):
        """
        :param item: <class "server.storehouseModel.Item">
        """
        self.__row_ind = row_ind

        self.number = tk.Label(window,
                               text=str(self.__row_ind),
                               font=style.font_name)

        self.name = tk.Label(window,
                             text=item.name,
                             font=style.font_name)

        self.size = tk.Label(window,
                             text=f"{item.size[0]}*{item.size[1]}*{item.size[2]}",
                             font=style.font_name)

        self.mass = tk.Label(window,
                             text=item.mass,
                             font=style.font_name)

    def draw(self):
        self.number.grid(row=self.__row_ind, column=0,
                         padx=style.InfoTable.padx, pady=style.InfoTable.pady)
        self.name.grid(row=self.__row_ind, column=1,
                       padx=style.InfoTable.padx, pady=style.InfoTable.pady)
        self.size.grid(row=self.__row_ind, column=2,
                       padx=style.InfoTable.padx, pady=style.InfoTable.pady)
        self.mass.grid(row=self.__row_ind, column=3,
                       padx=style.InfoTable.padx, pady=style.InfoTable.pady)
