"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : This program contains Import Resume GUI"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from datetime import datetime
from src.tools.resume_analyser import ResumeAnalyser
from src.tools.globals import Globals as gb
from src.tools.thread_pool_ir import ThreadPoolIR as tpir


class ImportResumeGUI:
    """
     class that defines the methods responsible for Import Resume GUI
    """

    def __init__(self, root, master):
        """
        constructor will be called from TalentHubGUI's new_window method while clicking ImportResume button
        :param root: an instance of top level window
        :param root: an instance of root or base  level window
        """
        self.root = root  # main window of the import resume screen
        self.master = master  # base window for all modules
        self.root.grab_set()
        self.root.geometry('740x500+0+0')
        self.root.resizable(False, False)
        self.root.title('Import Resume')
        self.root.focus_set()
        # self.root.wait_window(self.master)
        self.frame_import_panel = None
        self.file = None
        self.dict = None
        self.entry_name = None
        self.entry_email = None
        self.entry_contact_no = None
        self.open_import_panel()

    def open_import_panel(self):
        """
        method called to add widgets to the import_resume window
        """
        self.frame_import_panel = gb().create_frame(self.root, relx=0, rely=0, relwidth=1, relheight=1)

        gb().load_image(self.frame_import_panel, image="src/gui/images/techy.png", x=0, y=0)

        lbl_file_select = gb().create_label(self.frame_import_panel, text='Please select a file', font=16, relx=0.1,
                                            rely=0.1, type="",
                                            relwidth=0.80, relheight=0.1)

        gb().create_button(frame=self.frame_import_panel, text="Browse",
                           command=lambda: self.browse_resume(lbl_file_select), relx=0.3,
                           rely=0.40, relwidth=0.17, relheight=0.1)

        gb().create_button(frame=self.frame_import_panel, text="Cancel", command=lambda: self.close_window(),
                           relx=0.55,
                           rely=0.40, relwidth=0.17, relheight=0.1)

    def browse_resume(self, lbl_file_select):
        """
        method called when browse button is clicked from import resume window
        """

        self.file = fd.askopenfile(parent=self.root, initialdir="/", title="Select file",
                                   filetypes=(("all files", "*.*"), ("all files", "*.*")))

        lbl_file_select.config(text="Please select a file")

        try:
            if self.file:
                text_file = self.file.name
                file_extension = text_file.split('.')
                extension = file_extension[len(file_extension) - 1]
                print("file extension:::", extension)
                if extension != 'pdf' and extension != 'DOCx' and extension != 'docx':
                    raise Exception
                else:
                    lbl_file_select.config(text="File Name :" + text_file)

                    gb().create_button(frame=self.frame_import_panel, text="Import", command=self.import_resume,
                                       relx=0.43, rely=0.55, relwidth=0.17, relheight=0.1)

        except Exception as e:
            mb.showerror('Error', 'Upload Resume in PDF/DOCx format only!!', parent=self.root)
            print("File not selected", e)

    def import_resume(self):
        """
        method called when import button is clicked from open import panel
        """

        try:

            #self.dict = ResumeAnalyser().parse_resume(self.file.name)
            """thread module begins"""
            check_tag = "parse_resume"
            new_data = []
            self.prog_root = tk.Toplevel()
            self.dict = tpir(self.prog_root, self.file.name, check_tag, new_data).workerThread1()
            """thread module ends"""

            if self.dict['email']:
                candidate_email = self.dict['email']
                self.dict['email'] = candidate_email.lower()
            if self.dict['name']:
                candidate_name = self.dict['name']
                self.dict['name'] = candidate_name.capitalize()

            if self.dict['email'] and self.dict['name']:
                self.confirm_window(ConfirmWindow, self.dict, self.file)
            else:
                print("in exception:::")
                raise Exception

        except Exception as e:
            print("Error: in wrong doc format::", e)
            mb.showerror('Error', 'This file does\'nt seem to be a resume!! \n'
                                  'Upload Resume in PDF/DOCx format only!!', parent=self.root)

    def close_window(self):
        print("close window called")
        self.root.destroy()
        self.master.deiconify()

    def confirm_window(self, _class, data, file):
        print("in confirm window::")
        win_confirm_resume = tk.Toplevel(self.root)
        win_confirm_resume.attributes("-topmost", True)
        _class(win_confirm_resume, data, file)


class ConfirmWindow:
    def __init__(self, confirm_root, data, file):

        self.confirm_root = confirm_root
        self.confirm_root.geometry('740x500+0+0')
        self.confirm_root.resizable(False, False)
        self.confirm_root.title('Confirm Details')
        self.file = file
        self.data = data
        self.frame_import_confirmation = None
        self.entry_name = None
        self.entry_email = None
        self.entry_contact_no = None
        self.success_display(self.data)

    def success_display(self, data):
        """
        called from import_resume() if no exception occurs when importing the file
        this method contains the fields that display name, email and other labels and a save button to save
        resume parsed data into JIRA
        :param data: contains dict
        """
        self.frame_import_confirmation = gb().create_frame(self.confirm_root, relx=0, rely=0, relwidth=1, relheight=1)

        gb().load_image(self.frame_import_confirmation, image="src/gui/images/design.png", x=0, y=0)

        gb().create_label(self.frame_import_confirmation, text='Please Confirm the details', font=16, type="",
                          relx=0.1, rely=0.1, relwidth=0.80, relheight=0.1)

        gb().create_label(self.frame_import_confirmation, text='Name', font=12, type="entry",
                          relx=0.1, rely=0.23, relwidth=0.25, relheight=0.1)

        self.entry_name = tk.Entry(self.frame_import_confirmation)
        self.entry_name.place(relx=0.38, rely=0.23, relwidth=0.52, relheight=0.1)
        self.entry_name.insert(0, data['name'])

        gb().create_label(self.frame_import_confirmation, text='Email', font=12, type="entry",
                          relx=0.1, rely=0.36, relwidth=0.25, relheight=0.1)
        self.entry_email = tk.Entry(self.frame_import_confirmation)
        self.entry_email.place(relx=0.38, rely=0.36, relwidth=0.52, relheight=0.1)
        self.entry_email.insert(0, data['email'])

        gb().create_label(self.frame_import_confirmation, text='Contact Number', font=12, type="entry",
                          relx=0.1, rely=0.49, relwidth=0.25, relheight=0.1)

        self.entry_contact_no = tk.Entry(self.frame_import_confirmation)
        self.entry_contact_no.place(relx=0.38, rely=0.49, relwidth=0.52, relheight=0.1)
        self.entry_contact_no.insert(0, data['mobile_number'])

        gb().create_button(frame=self.frame_import_confirmation, text="Save",
                           command=lambda: self.save_candidate(data, self.file.name), relx=0.3,
                           rely=0.65, relwidth=0.17, relheight=0.1)
        gb().create_button(frame=self.frame_import_confirmation, text="Cancel", command=self.confirm_root.destroy,
                           relx=0.52,
                           rely=0.65, relwidth=0.17, relheight=0.1)

    def save_candidate(self, new_data, file):
        """
        method called when save button is clicked
        :param file: contains path of the file that is selected
        :param new_data: contains the data to be saved into JIRA
        """
        name = self.entry_name.get()
        new_data['name'] = name.capitalize()
        email = self.entry_email.get()
        new_data['email'] = email.lower()
        contact_no = self.entry_contact_no.get()
        new_data['mobile_number'] = contact_no

        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        new_data['date'] = dt_string

        #check_duplicate = ResumeAnalyser().json_validation(new_data)

        """thread module - begins"""
        check_tag = "json_validation"
        #self.master = tk.Toplevel()
        check_duplicate = tpir(self.confirm_root, self.file.name, check_tag, new_data).workerThread1()
        """thread module - ends"""

        if check_duplicate:
            #matched_desc = ResumeAnalyser().get_matched_desc(new_data)
            """thread module - begins"""
            check_tag = "matched_desc"
            #self.master = tk.Toplevel()
            matched_desc = tpir(self.confirm_root, self.file.name, check_tag, new_data).workerThread1()
            """thread module - ends"""

            if mb.askyesno('Duplicate Existing', 'Candidate ' + matched_desc['name'] +
                                                 ' \'s resume is already existing!\n\n''Last Updated on ' +
                                                 matched_desc[
                                                     'date'] + '\n\n' 'Do you want to save updated Resume version??',
                           parent=self.confirm_root):
                ResumeAnalyser().replace_candidate_resume(new_data, matched_desc)

                mb.showinfo('Yes', 'Saved updated Resume', parent=self.confirm_root)

        else:
            #new_id = ResumeAnalyser().save_new_candidate_resume(new_data, file)
            """thread module - begins"""
            check_tag = "save_new_candidate_resume"
            #self.master = tk.Toplevel()
            new_id = tpir(self.confirm_root, self.file, check_tag, new_data).workerThread1()
            """thread module - ends"""

            mb.showinfo('Saved', 'Saved New candidate into Jira Database', parent=self.confirm_root)
            print('Saved New candidate into Jira Database', new_id)
