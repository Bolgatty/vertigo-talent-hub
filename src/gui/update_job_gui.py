import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
from src.db.jd_manager import JDManager as jd
from src.gui.jobs_table_display_gui import JobsTable as jt
import tkcalendar as tc
import threading

class UpdateJob:
    def __init__(self, root, first_frame):
        self.first_frame = first_frame
        self.root = root
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.save_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.label_font = 5
        self.label_bg = 'SystemButtonFace'
        self.bg_frame = 'white'

    def update_job_details(self, selected_job_id, issue_key):
        """
             displays the fields required for add job screen
        """
        selected_job_description = jd().get_particular_desc(issue_key)
        selected_job_description['issue_key'] = issue_key
        job_id = selected_job_description['job_id']
        job_location = selected_job_description['job_location']
        job_title = selected_job_description['job_title']
        no_of_hires = selected_job_description['no_of_hires']
        phone_no = selected_job_description['phone_no']
        type_of_contract =  selected_job_description['type_of_contract']
        application_deadline = selected_job_description['application_deadline']
        company_name = selected_job_description['company_name']
        contact_person = selected_job_description['contact_person']
        job_description = selected_job_description['job_description']
        type_of_employment = selected_job_description['type_of_employment']

        top = tk.Toplevel(self.root)
        top.geometry('700x800')
        top.grab_set()
        top.resizable(False, False)

        self.u_wrapper = tk.Frame(top, bg='white')
        self.u_wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

        canvas = tk.Canvas(self.u_wrapper, bg="#ed9ef0",width=1,height=1)
        canvas.pack(side="left", fill="both", expand="yes")

        scroll = ttk.Scrollbar(self.u_wrapper, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        inner_frame = tk.Frame(canvas, height=700, width=700)
        # inner_frame.pack()

        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        header_frame = tk.Frame(inner_frame)
        header_frame.pack(fill="x")

        label_main = tk.Label(header_frame, text="Update Job", bg="black", width=60, pady=10,
                              fg="white", font=self.label_font, )
        label_main.pack(fill="x")

        inner_frame_one = tk.Frame(inner_frame)
        inner_frame_one.pack(fill="x")

        label_job_id = tk.Label(inner_frame_one, text="Job ID", width=30, pady=10,
                                bg=self.label_bg, font=self.label_font)
        label_job_id.pack(side="left")

        self.u_entry_job_id = tk.Label(inner_frame_one, text=job_id, width=30, pady=10,
                                     bg=self.label_bg, font=self.label_font)
        self.u_entry_job_id.pack(side="left")

        inner_frame_two = tk.Frame(inner_frame)
        inner_frame_two.pack(fill="x")

        label_company_name = tk.Label(inner_frame_two, text="Company name", width=30, pady=10,
                                      bg=self.label_bg, font=self.label_font)
        label_company_name.pack(side="left")

        self.u_entry_company_name = tk.Entry(inner_frame_two, font=self.label_font, width=25)
        self.u_entry_company_name.pack(side="left", padx=10)
        self.u_entry_company_name.insert(0, company_name)

        inner_frame_three = tk.Frame(inner_frame)
        inner_frame_three.pack(fill="x")

        label_job_title = tk.Label(inner_frame_three, text="Job Title", width=30, pady=10,
                                   bg=self.label_bg, font=self.label_font)
        label_job_title.pack(side="left")

        self.u_entry_job_title = tk.Entry(inner_frame_three, font=self.label_font, width=25)
        self.u_entry_job_title.pack(side="left", padx=10)
        self.u_entry_job_title.insert(0, job_title)

        inner_frame_four = tk.Frame(inner_frame)
        inner_frame_four.pack(fill="x")

        label_location = tk.Label(inner_frame_four, text="Job Location", width=30, pady=10,
                                  bg=self.label_bg, font=self.label_font)
        label_location.pack(side="left")

        self.u_entry_job_location = tk.Entry(inner_frame_four, font=self.label_font, width=25)
        self.u_entry_job_location.pack(side="left", padx=10)
        self.u_entry_job_location.insert(0, job_location)

        inner_frame_five = tk.Frame(inner_frame)
        inner_frame_five.pack(fill="x")

        label_no_of_hires = tk.Label(inner_frame_five, text="No. of hires", width=30, pady=10,
                                     bg=self.label_bg, font=self.label_font)
        label_no_of_hires.pack(side="left")

        self.u_entry_no_of_hires = tk.Entry(inner_frame_five, font=self.label_font, width=25)
        self.u_entry_no_of_hires.pack(side="left", padx=10)
        self.u_entry_no_of_hires.insert(0, no_of_hires)

        inner_frame_five = tk.Frame(inner_frame)
        inner_frame_five.pack(fill="x")

        label_contact_person = tk.Label(inner_frame_five, text="Contact Person", width=30, pady=10,
                                        bg=self.label_bg, font=self.label_font)
        label_contact_person.pack(side="left")

        self.u_entry_contact_person = tk.Entry(inner_frame_five, font=self.label_font, width=25)
        self.u_entry_contact_person.pack(side="left", padx=10)
        self.u_entry_contact_person.insert(0, contact_person)

        inner_frame_six = tk.Frame(inner_frame)
        inner_frame_six.pack(fill="x")

        label_phone_no = tk.Label(inner_frame_six, text="Phone No.", width=30, pady=10,
                                  bg=self.label_bg, font=self.label_font)
        label_phone_no.pack(side="left")

        self.u_entry_phone_no = tk.Entry(inner_frame_six, font=self.label_font, width=25)
        self.u_entry_phone_no.pack(side="left", padx=10)
        self.u_entry_phone_no.insert(0, phone_no)

        inner_frame_seven = tk.Frame(inner_frame)
        inner_frame_seven.pack(fill="x")

        label_type_of_employment = tk.Label(inner_frame_seven, width=30, pady=10,
                                            text="Type of Employment",
                                            bg=self.label_bg,
                                            font=self.label_font)
        label_type_of_employment.pack(side="left")

        # Dropdown options
        type_of_employment_choices = ['Full Time', 'Part Time']
        self.u_entry_type_of_employment = ttk.Combobox(inner_frame_seven,
                                                     values=type_of_employment_choices,
                                                     state="readonly",
                                                     width=24,
                                                     font=self.label_font)
        self.u_entry_type_of_employment.pack(side="left", padx=10)
        self.u_entry_type_of_employment.insert(0, phone_no)
        self.u_entry_type_of_employment.set(type_of_employment)

        inner_frame_eight = tk.Frame(inner_frame)
        inner_frame_eight.pack(fill="x")

        label_type_of_contract = tk.Label(inner_frame_eight, width=30, pady=10,
                                          text="Type of Contract",
                                          bg=self.label_bg,
                                          font=self.label_font)
        label_type_of_contract.pack(side="left")

        type_of_contract_choices = ['1 Year', '6 Months', '3 Months', 'Interen']
        self.u_entry_type_of_contract = ttk.Combobox(inner_frame_eight,
                                                   values=type_of_contract_choices,
                                                   state="readonly",
                                                   width=24,
                                                   font=self.label_font)
        self.u_entry_type_of_contract.pack(side="left", padx=10)
        self.u_entry_type_of_contract.set(type_of_contract)

        inner_frame_nine = tk.Frame(inner_frame)
        inner_frame_nine.pack(fill="x")

        label_application_deadline = tk.Label(inner_frame_nine, width=30, pady=10,
                                              text="Application Deadline",
                                              bg=self.label_bg,
                                              font=self.label_font)
        label_application_deadline.pack(side="left")

        self.u_entry_application_deadline = tc.DateEntry(inner_frame_nine,
                                                       state="readonly",
                                                       font=self.label_font,
                                                       width=24)
        self.u_entry_application_deadline.pack(side="left", padx=10)
        self.u_entry_application_deadline.set_date(application_deadline)

        inner_frame_ten = tk.Frame(inner_frame)
        inner_frame_ten.pack(fill="x", pady=10)

        label_frame = tk.Frame(inner_frame_ten)
        label_frame.pack(side="top", fill="x",padx=40)

        label_job_description = tk.Label(label_frame, width=30, pady=2,
                                         text="Job Description",
                                         font=self.label_font)
        label_job_description.pack(side="left")

        def clear():
            self.u_entry_job_description.delete(1.0, tk.END)

        def buttelize():
            self.u_entry_job_description.insert(tk.INSERT, '\u2022')

        format_button = tk.Frame(label_frame)
        format_button.pack(side="right", fill="both")

        clr_button = tk.Button(format_button, text="Clear", command=clear)
        clr_button.pack(side="left", padx=10, pady=2)

        bullet_button = tk.Button(format_button, text="Bullet", command=buttelize)
        photo_align = Image.open("images/icons/list_bullets.png")
        photo_align = photo_align.resize((20, 20), Image.ANTIALIAS)
        self.u_image_align_right = ImageTk.PhotoImage(photo_align)
        bullet_button.config(image=self.u_image_align_right)
        bullet_button.pack(side="right", pady=2)

        text_frame = tk.Frame(inner_frame_ten)
        text_frame.pack(side="right")

        textscrollbar = tk.Scrollbar(text_frame)

        self.u_entry_job_description = tk.Text(text_frame,wrap="word",
                                             font=self.label_font,
                                             width=50,
                                             height=5,
                                             yscrollcommand=textscrollbar.set)
        textscrollbar.config(command=self.u_entry_job_description.yview)
        textscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.u_entry_job_description.pack(fill="x", padx=15)
        self.u_entry_job_description.insert(1.0, job_description)

        inner_frame_11 = tk.Frame(inner_frame)
        inner_frame_11.pack(fill="x", pady=10)

        update_button = tk.Button(inner_frame_11, text="Save", bg=self.button_color, font=self.button_font,
                                fg=self.button_fg, command=threading.Thread(target=lambda: self.update_jira(issue_key, selected_job_id, top)).start)
        update_button.pack(side="left", padx=180, pady=20)

        def cancel():
            top.destroy()
            self.root.grab_set()

        cancel_button = tk.Button(inner_frame_11, text="Cancel", bg=self.button_color, font=self.button_font,
                                  fg=self.button_fg, command=top.destroy)
        cancel_button.pack(side="left", pady=20)
        top.mainloop()

    def update_button(self):
        # print('Inside Update button function :', jt.selected_job_id[0], jt.issue_key_list[0])
        if jt.selected_job_id:
            if mb.askyesno("Confirm Update", "Are you sure you want to update the selected job ?"):
                self.update_job_details(jt.selected_job_id[0], jt.issue_key_list[0])
        else:
            mb.showwarning("Error", "Please select the job you want to update")

    def update_jira(self, issue_key, selected_job_id, top):

        update_jb_dict = {}
        update_jb_dict['job_id'] = selected_job_id

        update_jb_dict['issue_key'] = issue_key

        company_name = self.u_entry_company_name.get()
        update_jb_dict['company_name'] = company_name

        job_title = self.u_entry_job_title.get()
        update_jb_dict['job_title'] = job_title

        job_location = self.u_entry_job_location.get()
        update_jb_dict['job_location'] = job_location

        contact_person = self.u_entry_contact_person.get()
        update_jb_dict['contact_person'] = contact_person

        type_of_employment = self.u_entry_type_of_employment.get()
        update_jb_dict['type_of_employment'] = type_of_employment

        type_of_contract = self.u_entry_type_of_contract.get()
        update_jb_dict['type_of_contract'] = type_of_contract

        job_description = self.u_entry_job_description.get("1.0", tk.END)
        update_jb_dict['job_description'] = job_description

        application_deadline = str(self.u_entry_application_deadline.get())
        update_jb_dict['application_deadline'] = application_deadline

        try:
            self.no_of_hires = int(self.u_entry_no_of_hires.get())
            update_jb_dict['no_of_hires'] = self.no_of_hires
        except ValueError:
            mb.showerror("Error", "Please give valid number in No. of hires field!")
            self.u_entry_no_of_hires.focus()

        try:
            self.phone_no = self.u_entry_phone_no.get()
            update_jb_dict['phone_no'] = self.no_of_hires
        except ValueError:
            mb.showerror("Error", "Please enter a valid Phone No.!")
            self.u_entry_phone_no.focus()

        if self.no_of_hires and self.phone_no:
            jd().update_job(issue_key, update_jb_dict)
            mb.showinfo("Info", "Selected Jobs updated successfully")
            jt(self.root).jobs_table(self.first_frame)
            top.destroy()
        else:
            mb.showwarning('Warning', 'Please fill in the all the details')