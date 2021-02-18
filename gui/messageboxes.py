# File with messageboxes's classes

import tkinter.messagebox as mb

import constants as const
import text


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


class ExceptionMb(ErrorMb):
    """Messageboxes for my exceptions"""

    def __get_msg(self, field):
        first_part = text.entry_content_error["message"]
        if field == const.AddingW.NAME_INDEX:
            return first_part + " field 'Name'"

        elif field == const.AddingW.SIZE_INDEX:
            return first_part + " field 'Size'"

        elif field == const.AddingW.MASS_INDEX:
            return first_part + " field 'Mass'"
        else:
            raise ValueError("field index error")

    def __init__(self, exception):
        super().__init__(title=text.entry_content_error["title"],
                         message=self.__get_msg(exception.field))
