# File with messageboxes's classes

import tkinter.messagebox as mb


class MyMb:
    def __init__(self, title, message):
        self.title = title
        self.message = message


class ErrorMb(MyMb):
    """Messagebox with Error-type"""

    def __init__(self, title="", message=""):
        super().__init__(title, message)

    def show(self):
        mb.showerror(self.title, self.message)


class InfoMb(MyMb):
    """Messagebox with some info"""

    def __init__(self, title="", message=""):
        super().__init__(title, message)

    def show(self):
        mb.showinfo(self.title, self.message)
