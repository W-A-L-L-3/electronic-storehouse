# Main application's code

import tkinter as tk

import server.operations as server_operations
from gui.widgets import MainMenu
from gui.windowsParameters import WindowParams


class MainWindow(tk.Tk):
    """Application's main window"""

    def __init__(self):
        super().__init__()
        self.parameters = WindowParams(title="Electronic storehouse", pady=300, padx=300)
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

    def run(self):
        """Launching the app"""
        self.__menu.draw()
        self.mainloop()

    def open_info_window(self):
        info_window = InfoWindow(self)


class InfoWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.grab_set()
        self.focus_set()
        self.wait_window()
