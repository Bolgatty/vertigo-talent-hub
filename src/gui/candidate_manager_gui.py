import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from src.tools.resume_analyser import ResumeAnalyser as ra
from src.gui.candidates_table import CandidateTable as ct
from src.db.db_manager import DatabaseManager as db
from PIL import ImageTk, Image
import os


class CandidateManager:
    """
     class that defines the methods responsible for Import Resume GUI
    """

    def __init__(self, toplevel_window):
        """
        constructor will be called from TalentHubGUI's new_window method while clicking ImportResume button
        :param toplevel_window: an instance of top level window
        """
        self.root = toplevel_window  # main window of the import resume screen
        self.root.grab_set()
        # self.master = master  # base window for all modules
        self.root.geometry('740x510+0+0')
        self.root.resizable(False, False)
        self.root.title('Candidate Manager')
        self.font_label = 20
        self.select_vendor()

    def select_vendor(self):
        """
        method called to choose vendor
        """
        vendor_frame = tk.Frame(self.root)
        vendor_frame.pack(fill="both")

        vendor_label = tk.Label(vendor_frame, width=30, pady=10,
                                            text="Choose Vendor", font=self.font_label)
        vendor_label.pack(fill="x", padx=20)

        # Dropdown options
        vendor_choices = db().get_all_vendor_names()
        self.vendor_combo = ttk.Combobox(vendor_frame,
                                                     values=vendor_choices,
                                                     state="readonly", font=self.font_label)
        self.vendor_combo.pack(fill='x', padx=20, pady=10)
        self.vendor_combo.current(0)

        skill_label = tk.Label(vendor_frame, width=30, pady=10,
                                text="Select Skill", font=self.font_label)
        skill_label.pack(fill="x", expand="yes", padx=20)

        checkbox_frame = tk.Frame(vendor_frame)
        checkbox_frame.pack(fill="x", padx=20, expand="yes", anchor=tk.CENTER)

        self.checkVar1 = tk.IntVar()
        self.checkVar2 = tk.IntVar()
        c1 = tk.Checkbutton(checkbox_frame, text="Python", variable=self.checkVar1,
                            onvalue=1, offvalue=0)
        c2 = tk.Checkbutton(checkbox_frame, text="Java", variable=self.checkVar2,
                            onvalue=1, offvalue=0)
        c1.pack()
        c2.pack()

        self.ok_button = tk.Button(vendor_frame, text="OK", font=self.font_label, command=self.open_import_panel)
        self.ok_button.pack(pady=20)

    def open_import_panel(self):
        """
        method called to add widgets to the import_resume window
        """

        self.ok_button.config(state=tk.DISABLED)

        self.import_frame = tk.Frame(self.root)
        self.import_frame.pack(fill="both", expand=True)

        # self.canvas = tk.Canvas(self.import_frame)
        #
        # # This creates a line of length 200 (straight horizontal line)
        # self.canvas.create_line(15, 25, 1200, 25)
        # self.canvas.pack(fill="x")

        import_label = tk.Label(self.import_frame, width=50, pady=10,
                                            text="Please select your File/Folder to import", font=self.font_label)
        import_label.pack(padx=20)

        self.var = tk.IntVar()

        r1 = tk.Radiobutton(self.import_frame, text="File", variable=self.var, value=1, font=self.font_label,
                         command=self.select_browse)
        r1.place(x=250, y=80)

        r2 = tk.Radiobutton(self.import_frame, text="Folder", variable=self.var, value=2, font=self.font_label,
                         command=self.select_browse)
        r2.place(x=400, y=80)

        self.import_file_path_label = tk.Label(self.import_frame, text='')
        self.import_file_path_label.pack(fill='x')

    def select_browse(self):

        browse_button = tk.Button(self.import_frame, text="Browse", font=self.font_label, command=self.browse_resume)
        browse_button.place(x=250, y=120)

        cancel_button = tk.Button(self.import_frame, text="Cancel", font=self.font_label, command=self.root.destroy)
        cancel_button.place(x=400, y=120)

    def browse_resume(self):
        self.import_file_path_label.configure(text="")
        if self.var.get() == 1:
            self.file_path = fd.askopenfilenames(initialdir="/", title="Select a File",
                                                    filetypes=(("all current_files", "*.*"), ("all current_files", "*.*")))
            if self.file_path:
                print("File name:", self.file_path)
                self.import_file_path_label.configure(text='Attached Files -' + self.file_path[0]+'...')
        else:
            self.current_directory = fd.askdirectory()
            if self.current_directory:
                print("Folder selected", self.current_directory)
                current_files = os.listdir(self.current_directory)
                print(current_files)
                self.list_files = []
                for i in current_files:
                    file_path = self.current_directory+'/'+i
                    self.list_files.append(file_path)
                print(self.list_files)
                self.import_file_path_label.configure(text='Attached Folder -' + self.current_directory)
        try:
            import_button = tk.Button(self.import_frame, font=self.font_label, text='Import', command=self.import_resume)
            import_button.place(x=330, y=180)

        except Exception as e:
            print(e)

    def import_resume(self):
        if self.var.get() == 1:
            self.candidate_info = []
            for i in self.file_path:
                dixt = ra().parse_resume(i)
                self.candidate_info.append(dixt)
                print("Parsed", dixt['name'])
        else:
            self.candidate_info = []
            for i in self.list_files:
                a = ra().parse_resume(i)
                self.candidate_info.append(a)
                print("Parsed", a['name'])

        self.display_candidates(self.candidate_info)

    def display_candidates(self, candidate_info):
        label_list = self.get_label()
        ct(self.root, label_list, candidate_info).candidate_table()

    def get_label(self):
        labels = []

        vendor_name = self.vendor_combo.get()
        split_vendor_space = vendor_name.split(' ')
        labels.append('vendor#' + ''.join(split_vendor_space))

        skill1 = self.checkVar1.get()
        if skill1 != 0:
            labels.append('skill#Python')

        skill2 = self.checkVar2.get()
        if skill2 != 0:
            labels.append('skill#Java')

        print(labels)
        return labels













root = tk.Tk()
CandidateManager(root)
root.mainloop()



