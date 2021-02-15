# Main application's code

import tkinter as tk

import server
from widgets import MainMenu
from windowsParameters import WindowParams


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
        self.__menu = MainMenu(self, init_func=server.init)

    def run(self):
        """Launching the app"""
        self.__menu.draw()
        self.mainloop()


window = MainWindow()
window.run()
