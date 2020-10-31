"""Author : Vidhya Gayathri
Date : 15/10/2019
Program : This program contains JD Management GUI"""

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import tkcalendar as tc
import threading
from src.db.jd_manager import JDManager as jd


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
        self.second_frame = None
        self.issue_key_list = []
        self.selected_job_id = []
        self.root.geometry("700x700")
        self.root.title("Job Description Management")
        self.root.resizable(False, False)
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.save_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.label_font = 5
        self.label_bg = 'white'
        self.bg_frame = 'white'
        self.no_of_hires = None
        self.phone_no = None
        self.im_checked = ImageTk.PhotoImage(Image.open("check.png"))
        self.im_unchecked = ImageTk.PhotoImage(Image.open("uncheck.png"))
        self.job_management_gui()

    def job_management_gui(self):
        """
          method called from constructor to exhibit front display of job management screen
        """

        self.first_frame = tk.Frame(self.root, bg=self.bg_frame)
        self.first_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        img = ImageTk.PhotoImage(Image.open("poly.png"))
        panel = tk.Label(self.first_frame, image=img)
        panel.image = img
        panel.place(relx=0, rely=0)

        add_job_button = ttk.Button(self.first_frame, text="Add Job", command=self.add_job)
        add_job_button.place(relx=0.12, rely=0.12, relwidth=0.25, relheight=0.1)

        delete_job_button = ttk.Button(self.first_frame, text="Delete Job", command=self.delete_job)
        delete_job_button.place(relx=0.63, rely=0.12, relwidth=0.25, relheight=0.1)

        generate_pdf = ttk.Button(self.first_frame, text="Generate PDF", command=self.delete_job)
        generate_pdf.place(relx=0.63, rely=0.75, relwidth=0.25, relheight=0.1)

        style = ttk.Style(generate_pdf)
        style.configure("TButton", font=(None, 12, 'bold'))

        t = threading.Thread(target=self.jobs_table)
        t.start()
        #self.jobs_table()

    def delete_job(self):
        """
             method called when Delete Job button is clicked from job_management initial screen
        """
        try:
            if self.selected_job_id:
                if mb.askyesno("Confirm Deletion", "Are you sure you want to delete the selected job ?"):
                    for i in self.issue_key_list:
                        jd().delete_job(i)
                    mb.showinfo("Info", "Selected Jobs deleted successfully")
        except Exception as e:
            print(e)
            mb.showerror("Error", "Please select the job you want to delete")
        finally:
            self.jobs_table()

    def jobs_table(self):
        """
             method responsible in displaying all the jobs in a table format
        """
        self.label = tk.Label(self.first_frame, text="Available Jobs", font=('', 12, 'bold'), bg=self.bg_frame)
        self.label.place(relx=0.34, rely=0.30, relwidth=0.25)

        self.tabel_frame = tk.Frame(self.first_frame, bg=self.bg_frame)
        self.tabel_frame.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=.3)

        self.tv = ttk.Treeview(self.tabel_frame, columns=(1, 2, 3, 4, 5), height="5")
        self.tv.place(relx=0, rely=0.05, relwidth=1, relheight=1)

        # Constructing vertical scrollbar
        verscrbar = ttk.Scrollbar(self.tabel_frame, orient="vertical", command=self.tv.yview)
        verscrbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Horizontal Scrollbar
        horscrbar = ttk.Scrollbar(self.tabel_frame, orient="horizontal", command=self.tv.xview)
        horscrbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.tv.configure(yscrollcommand=verscrbar.set, xscrollcommand=horscrbar.set)

        style = ttk.Style(self.tv)
        style.configure("Treeview", rowheight=35)
        style.configure("Treeview.Heading", font=(None, 10, 'bold'))

        self.tv.tag_configure('checked', image=self.im_checked)
        self.tv.tag_configure('unchecked', image=self.im_unchecked)

        self.tv.heading('#0', text="")
        self.tv.heading('#1', text="Job ID")
        self.tv.heading('#2', text="Job Title")
        self.tv.heading('#3', text="Company Name")
        self.tv.heading('#4', text="Application Deadline")
        self.tv.heading('#5', text="Issue Key")

        self.tv.column('#0', minwidth=0, width=75, anchor='c')
        self.tv.column('#1', minwidth=0, width=75, anchor='c')
        self.tv.column('#2', minwidth=0, width=150, anchor='c')
        self.tv.column('#3', minwidth=0, width=150, anchor='c')
        self.tv.column('#4', minwidth=0, width=150, anchor='c')
        self.tv.column('#5', minwidth=0, width=150, anchor='c')

        jobs = jd().fetch_all_jobs()

        for i in jobs:
            self.tv.insert('', 'end', tags="unchecked",
                           values=(i['job_id'], i['job_title'], i['company_name'],
                                   i['application_deadline'], i['issue_key']))
        self.tv.bind('<Double 1>', self.toggle_check) # toggle_check method is called when double click event occurs

    def toggle_check(self, event):
        """
             method responsible when row(jobs table) is selected
             :param event: double click event occurs
        """
        rowid = self.tv.identify_row(event.y) # returns selected row
        tag = list(self.tv.item(rowid, "tags"))[0] # returns the items first element of the selected row
        tags = list(self.tv.item(rowid, "tags")) # returns all the items of the selected row
        tags.remove(tag) # removes the tag of the selected row
        self.tv.item(rowid, tags=tags) # sets no tags to the selected row's item
        if tag == "checked":
            self.tv.item(rowid, tags="unchecked")
            item = self.tv.item(self.tv.focus())
            self.selected_job_id.remove(item['values'][0])
            self.issue_key_list.remove(item['values'][4])
            print(self.selected_job_id)
            print(self.issue_key_list)
        else:
            self.tv.item(rowid, tags="checked")
            item = self.tv.item(self.tv.focus())
            self.selected_job_id.append(item['values'][0])
            self.issue_key_list.append(item['values'][4])
            print(self.selected_job_id)
            print(self.issue_key_list)

    # method not used as of now (22/10/2020)
    def toggle2(self, event):
        """
             method responsible when row(jobs table) is selected, makes sure only one row is selected at a time
             :param event: double click event occurs
        """
        for i in self.tv.get_children():
            self.tv.item(i, tags="unchecked")
        self.toggle_check(event)

    def add_job(self):
        """
             displays the fields required for add job screen
        """
        self.first_frame.place_forget()

        self.second_frame = tk.Frame(self.root, bg='white')
        self.second_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        jb_dict = {}

        self.id = jd().job_id_generator()
        self.job_id = 'JD0'+str(self.id)

        label_main = tk.Label(self.second_frame, text="Add Job", bg="black", fg="white", font=self.label_font)
        label_main.place(relx=0.1, rely=0.01, relwidth=0.80, relheight=0.05)

        label_job_id = tk.Label(self.second_frame, text="Job ID", bg=self.label_bg, font=self.label_font)
        label_job_id.place(relx=0.1, rely=0.07, relwidth=0.25, relheight=0.05)

        self.entry_job_id = tk.Label(self.second_frame, text=self.job_id, bg=self.label_bg, font=self.label_font)
        self.entry_job_id.place(relx=0.4, rely=0.07, relwidth=0.25, relheight=0.05)

        label_company_name = tk.Label(self.second_frame, text="Company name", bg=self.label_bg, font=self.label_font)
        label_company_name.place(relx=0.1, rely=0.13, relwidth=0.25, relheight=0.05)

        self.entry_company_name = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_company_name.place(relx=0.4, rely=0.13, relwidth=0.5, relheight=0.05)

        label_job_title = tk.Label(self.second_frame, text="Job Title", bg=self.label_bg, font=self.label_font)
        label_job_title.place(relx=0.1, rely=0.19, relwidth=0.25, relheight=0.05)

        self.entry_job_title = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_job_title.place(relx=0.4, rely=0.19, relwidth=0.5, relheight=0.05)

        label_location = tk.Label(self.second_frame, text="Job Location", bg=self.label_bg, font=self.label_font)
        label_location.place(relx=0.1, rely=0.25, relwidth=0.25, relheight=0.05)

        self.entry_job_location = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_job_location.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.05)

        label_no_of_hires = tk.Label(self.second_frame, text="No. of hires", bg=self.label_bg, font=self.label_font)
        label_no_of_hires.place(relx=0.1, rely=0.31, relwidth=0.25, relheight=0.05)

        self.entry_no_of_hires = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_no_of_hires.place(relx=0.4, rely=0.31, relwidth=0.5, relheight=0.05)

        label_contact_person = tk.Label(self.second_frame, text="Contact Person", bg=self.label_bg, font=self.label_font)
        label_contact_person.place(relx=0.1, rely=0.37, relwidth=0.25, relheight=0.05)

        self.entry_contact_person = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_contact_person.place(relx=0.4, rely=0.37, relwidth=0.5, relheight=0.05)

        label_phone_no = tk.Label(self.second_frame, text="Phone No.", bg=self.label_bg, font=self.label_font)
        label_phone_no.place(relx=0.1, rely=0.43, relwidth=0.25, relheight=0.05)

        self.entry_phone_no = tk.Entry(self.second_frame, font=self.label_font)
        self.entry_phone_no.place(relx=0.4, rely=0.43, relwidth=0.5, relheight=0.05)

        label_type_of_employment = tk.Label(self.second_frame, text="Type of Employment", bg=self.label_bg,
                                            font=self.label_font)
        label_type_of_employment.place(relx=0.1, rely=0.49, relwidth=0.30, relheight=0.05)

        # Dropdown options
        type_of_employment_choices = ['Full Time', 'Part Time']
        self.entry_type_of_employment = ttk.Combobox(self.second_frame, values=type_of_employment_choices,
                                                     font=self.label_font)
        self.entry_type_of_employment.place(relx=0.4, rely=0.49, relwidth=0.5, relheight=0.05)
        self.entry_type_of_employment.current(0)

        label_type_of_contract = tk.Label(self.second_frame, text="Type of Contract", bg=self.label_bg,
                                            font=self.label_font)
        label_type_of_contract.place(relx=0.1, rely=0.55, relwidth=0.25, relheight=0.05)

        type_of_contract_choices = ['1 Year', '6 Months', '3 Months', 'Interen']
        self.entry_type_of_contract = ttk.Combobox(self.second_frame, values=type_of_contract_choices,
                                                   font=self.label_font)
        self.entry_type_of_contract.place(relx=0.4, rely=0.55, relwidth=0.5, relheight=0.05)
        self.entry_type_of_contract.current(0)

        label_job_description = tk.Label(self.second_frame, text="Job Description", bg=self.label_bg,
                                            font=self.label_font)
        label_job_description.place(relx=0.1, rely=0.61, relwidth=0.25, relheight=0.05)

        self.entry_job_description = tk.Text(self.second_frame, font=self.label_font)
        self.entry_job_description.place(relx=0.4, rely=0.61, relwidth=0.5, relheight=0.13)

        label_application_deadline = tk.Label(self.second_frame, text="Application Deadline", bg=self.label_bg,
                                            font=self.label_font)
        label_application_deadline.place(relx=0.1, rely=0.75, relwidth=0.25, relheight=0.05)

        self.entry_application_deadline = tc.DateEntry(self.second_frame, font=self.label_font)
        # cal = tc.Calendar()
        # self.entry_application_deadline.config(cal.get_date())
        self.entry_application_deadline.place(relx=0.4, rely=0.75, relwidth=0.5, relheight=0.05)

        save_button = tk.Button(self.second_frame, text="Save", bg=self.button_color, font=self.button_font,
                                fg=self.button_fg, command=threading.Thread(target=lambda: self.save_details(jb_dict)).start)
        save_button.place(relx=0.20, rely=0.85, relwidth=0.25, relheight=0.06)

        cancel_button = tk.Button(self.second_frame, text="Cancel", bg=self.button_color, font=self.button_font,
                                  fg=self.button_fg, command=self.job_management_gui)
        cancel_button.place(relx=0.50, rely=0.85, relwidth=0.25, relheight=0.06)

    def save_details(self, jb_dict):
        """
             Saves the data entered in add job screen by the user to JIRA
        """

        jb_dict['job_id'] = self.job_id

        company_name = self.entry_company_name.get()
        jb_dict['company_name'] = company_name

        job_title = self.entry_job_title.get()
        jb_dict['job_title'] = job_title

        job_location = self.entry_job_location.get()
        jb_dict['job_location'] = job_location

        contact_person = self.entry_contact_person.get()
        jb_dict['contact_person'] = contact_person

        type_of_employment = self.entry_type_of_employment.get()
        jb_dict['type_of_employment'] = type_of_employment

        type_of_contract = self.entry_type_of_contract.get()
        jb_dict['type_of_contract'] = type_of_contract

        job_description = self.entry_job_description.get("1.0", tk.END)
        jb_dict['job_description'] = job_description

        application_deadline = str(self.entry_application_deadline.get())
        jb_dict['application_deadline'] = application_deadline

        try:
            self.no_of_hires = int(self.entry_no_of_hires.get())
            jb_dict['no_of_hires'] = self.no_of_hires
        except ValueError:
            mb.showerror("Error", "Please give valid number in No. of hires field!")
            self.entry_no_of_hires.focus()

        try:
            self.phone_no = self.entry_phone_no.get()
            jb_dict['phone_no'] = self.no_of_hires
        except ValueError:
            mb.showerror("Error", "Please enter a valid Phone No.!")
            self.entry_phone_no.focus()

        if self.no_of_hires and self.phone_no:
            jd().add_issue_key(jb_dict)
            jd().update_job_id_tracker(self.id)
            mb.showinfo('Saved', 'Saved New JOB into Jira Database')
            self.job_management_gui()
        else:
            mb.showwarning('Warning', 'Please fill in the all the details')

win = tk.Tk()
obj = JobManagement(win)
win.mainloop()




