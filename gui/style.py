# File with style-settings for application's interface

font_name = "Helvetica"

font = (font_name, 12)

class Btn:
    """Style-settings for buttons"""
    font = (font_name, 11)
    big_width = 28
    small_width = 10
    pady = 5


class Entry:
    """Style-settings for entries"""
    font = (font_name, 11)

    name_f_width = 18
    size_f_width = 16
    mass_f_width = 7

    padx = 5
    pady = 5

    ok_color = "#CCFFCF"
    warning_color = "#FFF7CC"
    error_color = "#FFCCCC"


class InfoTable:
    """Style-settings for table with info"""
    padx = 10
    pady = 5
