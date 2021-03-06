# Main application's code

import tkinter as tk

import exceptions as exc
import server.operations as server_operations
import text
from gui.messageboxes import InfoMb, ErrorMb
from gui.widgets import MainMenu, InfoTable, AddingWList, AddingWButtons, GivingWWidgets
from gui.windowsParameters import WindowParams


class MainWindow(tk.Tk):
    """Application's main window"""

    def __init__(self):
        super().__init__()
        self.parameters = WindowParams(title="Electronic storehouse",
                                       pady=300, padx=300,
                                       resizable=(False, False))
        self.title(self.parameters.title)
        self.geometry(self.parameters.geometry())
        self.resizable(*self.parameters.resizable)
        try:
            self.iconbitmap(self.parameters.ico_path)
        except tk.TclError:  # Icon display error
            pass  # Default Tkinter's icon
        self.__menu = MainMenu(self,
                               init_func=server_operations.init,
                               add_func=self.open_adding_window,
                               info_func=self.open_info_window,
                               take_func=self.open_giving_window,
                               remote_info_func=self.open_remote_info_window)
        self.info_window = None
        self.adding_window = None
        self.giving_window = None
        self.remote_info_window = None

    def run(self):
        """Launching the app"""
        self.__menu.draw()
        self.mainloop()

    def open_info_window(self):
        table = server_operations.get_info()
        self.info_window = InfoWindow(self,
                                      "Information about storehouse",
                                      table, need_pos_column=True)
        self.info_window.draw()

    def open_adding_window(self):
        self.adding_window = AddingWindow(self,
                                          add_func=server_operations.add_items)
        self.adding_window.draw()

    def open_giving_window(self):
        self.giving_window = GivingWindow(self,
                                          give_func=server_operations.give_item)
        self.giving_window.draw()

    def open_remote_info_window(self):
        table = server_operations.get_remote_info()
        self.remote_info_window = InfoWindow(self,
                                             "Information about remote storehouse",
                                             table, need_pos_column=False)
        self.remote_info_window.draw()


class ChildWindow(tk.Toplevel):
    def __init__(self, parent, title="", width=None, height=None,
                 padx=None, pady=None, resizable=(True, True)):

        super().__init__(parent)
        self.parameters = WindowParams(title, width, height, padx, pady, resizable)
        self.title(self.parameters.title)
        self.geometry(self.parameters.geometry())
        self.resizable(*self.parameters.resizable)
        try:
            self.iconbitmap(self.parameters.ico_path)
        except tk.TclError:  # Icon display error
            pass  # Default Tkinter's icon

    def set_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()


class InfoWindow(ChildWindow):
    """Class of window for information about storehouse"""

    def __init__(self, parent, title, table, need_pos_column):
        super().__init__(parent,
                         title=title,
                         resizable=(False, False))
        self.__table = InfoTable(self, table, need_pos_column)

    def draw(self):
        self.__table.draw()
        self.set_focus()


class AddingWindow(ChildWindow):
    """Class of window for adding items to the storehouse"""

    def __init__(self, parent, add_func):
        super().__init__(parent,
                         title="Add items to the storehouse",
                         resizable=(False, False))
        self.__add_items_to_server = add_func
        self.__rows = AddingWList(self)
        self.__buttons = AddingWButtons(self,
                                        add_row_func=self.__rows.add_row,
                                        enter_func=self.add_items)

    def add_items(self):
        items_list = self.__rows.get_list()
        if items_list is not None:  # If all values was correct
            self.__add_items_to_server(items_list)
            InfoMb(title=text.correct_adding["title"],
                   message=text.correct_adding["message"]).show()
            self.destroy()

    def draw(self):
        self.__rows.draw()
        self.__buttons.draw()
        self.set_focus()


class GivingWindow(ChildWindow):
    def __init__(self, parent, give_func):
        super().__init__(parent,
                         resizable=(False, False))
        self.__give_func = give_func
        self.__widgets = GivingWWidgets(self, self.call_give)

    def call_give(self):
        try:
            self.__give_func(item_name=self.__widgets.get_name())
        except exc.ItemNotFoundError:
            ErrorMb(title=text.item_not_found_error["title"],
                    message=text.item_not_found_error["message"]).show()
        else:
            InfoMb(title=text.correct_taking["title"],
                   message=text.correct_taking["message"]).show()
            self.destroy()

    def draw(self):
        self.__widgets.draw()
        self.set_focus()
