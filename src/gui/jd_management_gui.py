"""Author : Vidhya Gayathri
Date : 15/10/2019
Program : This program contains JD Management GUI"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from src.gui.add_job_gui import AddJob as aj
from src.gui.jobs_table_display_gui import JobsTable as jt
from src.gui.update_job_gui import UpdateJob as uj
from src.gui.delete_job_gui import DeleteJob as dj
from src.db.generate_pdf import JobGeneratepdf as gpdf


class JobManagement:
    """
     class that defines the methods responsible for Job Management Screen GUI
    """
    def __init__(self, win):
        """
         constructor will be called from main file when JobManagement GUI's class object is initiated
         :param win: an instance of Tkinter’s Tk class that creates a window
         """
        self.root = win
        self.issue_key = None
        self.entry_company_name = None
        self.entry_job_id = None
        self.job_id = None
        self.first_frame = None
        self.wrapper = None
        self.root.geometry("700x800+10+10")
        self.root.title("Job Description Management")
        self.root.resizable(False, False)
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.save_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.label_font = 5
        self.label_bg = 'SystemButtonFace'
        self.bg_frame = 'white'
        self.no_of_hires = None
        self.phone_no = None
        self.job_management_gui()

    def job_management_gui(self):
        """
          method called from constructor to exhibit front display of job management screen
        """

        self.first_frame = tk.Frame(self.root, bg=self.bg_frame)
        self.first_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        img = ImageTk.PhotoImage(Image.open("images/poly.png"))
        panel = tk.Label(self.first_frame, image=img)
        panel.image = img
        panel.place(relx=0, rely=0)

        add_job_button = ttk.Button(self.first_frame, text="Add Job", command=aj(self.root, self.first_frame).add_job)
        add_job_button.place(relx=0.12, rely=0.12, relwidth=0.25, relheight=0.1)

        delete_job_button = ttk.Button(self.first_frame, text="Delete Job", command=dj(self.root, self.first_frame).delete_job)
        delete_job_button.place(relx=0.63, rely=0.12, relwidth=0.25, relheight=0.1)

        generate_pdf = ttk.Button(self.first_frame, text="Generate PDF/DOCx",
                                command=gpdf().generate_pdf)
        generate_pdf.place(relx=0.63, rely=0.75, relwidth=0.25, relheight=0.1)

        update_job = ttk.Button(self.first_frame, text="Update Job",
                                command= uj(self.root, self.first_frame).update_button)
        update_job.place(relx=0.12, rely=0.75, relwidth=0.25, relheight=0.1)

        style = ttk.Style(update_job)
        style.configure("TButton", font=(None, 12, 'bold'))

        jt(self.root).jobs_table(self.first_frame)


win = tk.Tk()
obj = JobManagement(win)
win.mainloop()




