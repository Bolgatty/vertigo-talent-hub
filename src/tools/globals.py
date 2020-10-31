"""Author : Femy Anish
Date : 17/10/2020
"""

import tkinter as tk
from PIL import ImageTk, Image


class Globals:
    """
    class to define the standards to be followed for the entire application for designing the GUI
    """

    bkg_main = "light grey"
    btn_main_bg = "cyan2"
    btn_main_fg = ""
    bg_panel_header = '#000000'
    button_color = '#00917c'
    import_button_color = 'red'
    button_fg = 'white'
    button_font = 16
    confirm_panel_font = 12
    bg_frame = 'light grey'
    frame = None

    def create_button(self, **kwargs):
        print(kwargs["frame"])
        browse_button = tk.Button(kwargs["frame"], bg=self.button_color, fg=self.button_fg,
                                  font=self.button_font, text=kwargs["text"], command=kwargs["command"])
        browse_button.place(relx=kwargs["relx"], rely=kwargs["rely"], relwidth=kwargs["relwidth"],
                            relheight=kwargs["relheight"])

    def create_frame(self, root, **kwargs):
        self.frame = tk.Frame(root, bg=self.bg_frame)
        self.frame.place(relx=kwargs["relx"], rely=kwargs["rely"], relwidth=kwargs["relwidth"],
                         relheight=kwargs["relheight"])
        return self.frame

    def load_image(self, frame, **kwargs):
        img = ImageTk.PhotoImage(Image.open(kwargs["image"]))
        panel = tk.Label(frame, image=img)
        panel.image = img
        panel.place(x=kwargs["x"], y=kwargs["x"])

    def create_label(self, frame, text, font,type, **kwargs):
        if type == "entry":
            bg_color = "white"
            fg = "black"
        else:
            bg_color = self.bg_panel_header
            fg = 'white'

        import_file_desc = tk.Label(frame, text=text,
                                    bg=bg_color, fg=fg, font=font)
        import_file_desc.place(relx=kwargs["relx"], rely=kwargs["rely"], relwidth=kwargs["relwidth"],
                               relheight=kwargs["relheight"])
        return import_file_desc
