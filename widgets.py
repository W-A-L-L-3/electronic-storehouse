# File with widget's classes

import tkinter as tk

import exceptions
import messageboxes as mb
import style
import text


class MainMenu(tk.Frame):
    def __init__(self, window, init_func):
        super().__init__(window)
        self.__init_func = init_func
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
                                    state=tk.DISABLED)

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
