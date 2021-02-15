# Main application's code

import tkinter as tk

import server.operations as server_operations
from gui.widgets import MainMenu, InfoTable
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
                               info_func=self.open_info_window)
        self.info_window = None

    def run(self):
        """Launching the app"""
        self.__menu.draw()
        self.mainloop()

    def open_info_window(self):
        table = server_operations.get_info()
        self.info_window = InfoWindow(self, table)
        self.info_window.draw()


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

    def __init__(self, parent, table):
        super().__init__(parent, title="Information about storehouse")
        self.__table = InfoTable(self, table)

    def draw(self):
        self.__table.draw()
        print("table draw")
        self.set_focus()
