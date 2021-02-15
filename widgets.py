# File with widget's classes

import tkinter as tk

import style
import text


class MainMenu(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.__init_btn = tk.Button(self,
                                    text=text.main_menu["init"],
                                    font=style.Btn.font,
                                    width=style.Btn.width)

        self.__add_btn = tk.Button(self,
                                   text=text.main_menu["add"],
                                   font=style.Btn.font,
                                   width=style.Btn.width)

        self.__info_btn = tk.Button(self,
                                    text=text.main_menu["info"],
                                    font=style.Btn.font,
                                    width=style.Btn.width)

        self.__remove_btn = tk.Button(self,
                                      text=text.main_menu["remove"],
                                      font=style.Btn.font,
                                      width=style.Btn.width)

        self.__remote_info_btn = tk.Button(self,
                                           text=text.main_menu["remote_info"],
                                           font=style.Btn.font,
                                           width=style.Btn.width)

    def draw(self):
        self.__init_btn.pack(pady=style.Btn.pady)
        self.__add_btn.pack(pady=style.Btn.pady)
        self.__info_btn.pack(pady=style.Btn.pady)
        self.__remove_btn.pack(pady=style.Btn.pady)
        self.__remote_info_btn.pack(pady=style.Btn.pady)
        self.pack(padx=20, pady=15)
