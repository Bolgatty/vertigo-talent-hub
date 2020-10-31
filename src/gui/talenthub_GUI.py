"""Author : Femy Anish
Date : 17/10/2020
Program : This program contains Import Resume GUI"""

import tkinter as tk
from time import strftime, time

import datetime as dt
from src.gui.import_resumeGUI import ImportResumeGUI as irg
from src.tools.globals import Globals as gb


class TalentHubGUI:
    """
     main class that displays all main components of Talent Hunt application
    """

    def __init__(self, root):
        """
        constructor will be called from main file when TalentHubGUI's class object is initiated
        :param root: an instance of Tkinter’s Tk class that creates a window
        """
        self.root = root
        root.title('Talent Hub Recruitment System')
        root.geometry('740x500+0+0')
        root.resizable(0, 0)
        root.configure(bg=gb.bkg_main)
        self.show_widgets()

    def show_widgets(self):
        """
        method called from constructor to exhibit initial display
        """

        self.frame = tk.Frame(self.root, bg=gb.bkg_main)
        self.frame.place(relx=0, rely=0, relwidth=740, relheight=500)
        label1 = tk.Label(self.frame, text="", bg=gb.bkg_main)
        label1.grid(row=0, column=0, padx=30, pady=5)
        self.left_frame()
        self.middle_frame()
        self.right_frame()

    def time(self):
        lbl_clock = tk.Label(self.frame, font=('calibri', 15, 'bold'), bg=gb.bkg_main)
        string = f"{dt.datetime.now():%a, %b %d %Y}" + " , " + strftime('%I:%M:%S %p')
        lbl_clock.config(text=string)
        lbl_clock.after(1000, self.time)
        lbl_clock.grid(row=13, column=40, padx=50)

    def left_frame(self):
        self.create_button("Import Resume", row=5, col=0, padx=30, pady=10,_class=irg)
        self.create_button("New Candidate", row=7, col=0, padx=30, pady=10)
        self.create_button("Delete Candidate", row=9, col=0, padx=30, pady=10)
        self.create_button("Generate JD", row=11, col=0, padx=30, pady=10)
        self.create_button("Update Job", row=13, col=0, padx=30, pady=10)
        self.create_button("Remove Job", row=15, col=0, padx=30, pady=10)
        self.create_button("Admin", row=17, col=0, padx=30, pady=10)

    def middle_frame(self):
        lbl_talenthub = tk.Label(self.frame, font=('calibri', 20, 'bold'), text="Talent Hunt", bg=gb.bkg_main)
        lbl_version = tk.Label(self.frame, font=('calibri', 15, 'bold'), text="Version 1.0 (powered by Team Vertigo)",
                               bg=gb.bkg_main)
        lbl_talenthub.grid(row=11, column=40)
        lbl_version.grid(row=12, column=40, padx=50)
        self.time()

    def right_frame(self):
        self.create_button("Analytics", row=5, col=110, padx=0, pady=10)
        self.create_button("Add Vendor", row=7, col=110, padx=0, pady=10)
        self.create_button("Remove Vendor", row=9, col=110, padx=0, pady=10)
        self.create_button("Add Customer", row=11, col=110, padx=0, pady=10)
        self.create_button("Delete Customer", row=13, col=110, padx=0, pady=10)
        self.create_button("Display Sheet", row=15, col=110, padx=0, pady=10)
        self.create_button("Export Data", row=17, col=110, padx=0, pady=10)

    def create_button(self, text, row, col, padx=0, pady=0,**kwargs):
        but = tk.Button(
            self.frame, text=text, width=13, background=gb.btn_main_bg,
            command=lambda: self.new_window(kwargs['_class']))
        but.config(font=("Raleway", 10))
        but.grid(row=row, column=col, padx=padx, pady=pady)

    def new_window(self, _class):
        win_import_resume = tk.Toplevel(self.root)
        win_import_resume.attributes("-topmost", True)
        _class(win_import_resume, self.root)
