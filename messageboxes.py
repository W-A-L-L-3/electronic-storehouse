# File with messageboxes's classes

import tkinter.messagebox as mb


class ErrorMb:
    """Messagebox with Error-type"""

    def __init__(self, title="", message=""):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class InfoMb:
    """Messagebox with some info"""

    def __init__(self, title="", message=""):
        self.title = title
        self.message = message

    def show(self):
        mb.showinfo(self.title, self.message)
