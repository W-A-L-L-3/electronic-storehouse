# File with widget's classes

import tkinter as tk

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
        print("call init")
        print("res:", self.__init_func())

    def draw(self):
        self.__init_btn.pack(pady=style.Btn.pady)
        self.__add_btn.pack(pady=style.Btn.pady)
        self.__info_btn.pack(pady=style.Btn.pady)
        self.__remove_btn.pack(pady=style.Btn.pady)
        self.__remote_info_btn.pack(pady=style.Btn.pady)
        self.pack(padx=20, pady=15)
