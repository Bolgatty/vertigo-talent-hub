import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import tkcalendar as tc
import threading
from src.db.jd_manager import JDManager as jd
from src.gui.jobs_table_display_gui import JobsTable as jt

class AddJob:

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

    def add_job(self):
        """
             displays the fields required for add job screen
        """
        jb_dict = {}

        self.id = jd().job_id_generator()
        self.job_id = 'JD0'+str(self.id)

        # self.first_frame.place_forget()

        top = tk.Toplevel(self.root)
        top.geometry('700x800')
        top.grab_set()
        top.resizable(False, False)

        self.wrapper = tk.Frame(top, bg='white')
        self.wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

        canvas = tk.Canvas(self.wrapper, bg="#ed9ef0",width=1,height=1)
        canvas.pack(side="left", fill="both", expand="yes")

        scroll = ttk.Scrollbar(self.wrapper, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        inner_frame = tk.Frame(canvas, height=700, width=700)
        # inner_frame.pack()

        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        header_frame = tk.Frame(inner_frame)
        header_frame.pack(fill="x")

        label_main = tk.Label(header_frame, text="Add Job", bg="black", width=60, pady=10,
                              fg="white", font=self.label_font, )
        label_main.pack(fill="x")

        inner_frame_one = tk.Frame(inner_frame)
        inner_frame_one.pack(fill="x")

        label_job_id = tk.Label(inner_frame_one, text="Job ID", width=30, pady=10,
                                bg=self.label_bg, font=self.label_font)
        label_job_id.pack(side="left")

        self.entry_job_id = tk.Label(inner_frame_one, text=self.job_id, width=30, pady=10,
                                     bg=self.label_bg, font=self.label_font)
        self.entry_job_id.pack(side="left")

        inner_frame_two = tk.Frame(inner_frame)
        inner_frame_two.pack(fill="x")

        label_company_name = tk.Label(inner_frame_two, text="Company name", width=30, pady=10,
                                      bg=self.label_bg, font=self.label_font)
        label_company_name.pack(side="left")

        self.entry_company_name = tk.Entry(inner_frame_two, font=self.label_font, width=25)
        self.entry_company_name.pack(side="left", padx=10)

        inner_frame_three = tk.Frame(inner_frame)
        inner_frame_three.pack(fill="x")

        label_job_title = tk.Label(inner_frame_three, text="Job Title", width=30, pady=10,
                                   bg=self.label_bg, font=self.label_font)
        label_job_title.pack(side="left")

        self.entry_job_title = tk.Entry(inner_frame_three, font=self.label_font, width=25)
        self.entry_job_title.pack(side="left", padx=10)

        inner_frame_four = tk.Frame(inner_frame)
        inner_frame_four.pack(fill="x")

        label_location = tk.Label(inner_frame_four, text="Job Location", width=30, pady=10,
                                  bg=self.label_bg, font=self.label_font)
        label_location.pack(side="left")

        self.entry_job_location = tk.Entry(inner_frame_four, font=self.label_font, width=25)
        self.entry_job_location.pack(side="left", padx=10)

        inner_frame_five = tk.Frame(inner_frame)
        inner_frame_five.pack(fill="x")

        label_no_of_hires = tk.Label(inner_frame_five, text="No. of hires", width=30, pady=10,
                                     bg=self.label_bg, font=self.label_font)
        label_no_of_hires.pack(side="left")

        self.entry_no_of_hires = tk.Entry(inner_frame_five, font=self.label_font, width=25)
        self.entry_no_of_hires.pack(side="left", padx=10)

        inner_frame_five = tk.Frame(inner_frame)
        inner_frame_five.pack(fill="x")

        label_contact_person = tk.Label(inner_frame_five, text="Contact Person", width=30, pady=10,
                                        bg=self.label_bg, font=self.label_font)
        label_contact_person.pack(side="left")

        self.entry_contact_person = tk.Entry(inner_frame_five, font=self.label_font, width=25)
        self.entry_contact_person.pack(side="left", padx=10)

        inner_frame_six = tk.Frame(inner_frame)
        inner_frame_six.pack(fill="x")

        label_phone_no = tk.Label(inner_frame_six, text="Phone No.", width=30, pady=10,
                                  bg=self.label_bg, font=self.label_font)
        label_phone_no.pack(side="left")

        self.entry_phone_no = tk.Entry(inner_frame_six, font=self.label_font, width=25)
        self.entry_phone_no.pack(side="left", padx=10)

        inner_frame_seven = tk.Frame(inner_frame)
        inner_frame_seven.pack(fill="x")

        label_type_of_employment = tk.Label(inner_frame_seven, width=30, pady=10,
                                            text="Type of Employment",
                                            bg=self.label_bg,
                                            font=self.label_font)
        label_type_of_employment.pack(side="left")

        # Dropdown options
        type_of_employment_choices = ['Full Time', 'Part Time']
        self.entry_type_of_employment = ttk.Combobox(inner_frame_seven,
                                                     values=type_of_employment_choices,
                                                     state="readonly",
                                                     width=24,
                                                     font=self.label_font)
        self.entry_type_of_employment.pack(side="left", padx=10)
        self.entry_type_of_employment.current(0)

        inner_frame_eight = tk.Frame(inner_frame)
        inner_frame_eight.pack(fill="x")

        label_type_of_contract = tk.Label(inner_frame_eight, width=30, pady=10,
                                          text="Type of Contract",
                                          bg=self.label_bg,
                                          font=self.label_font)
        label_type_of_contract.pack(side="left")

        type_of_contract_choices = ['1 Year', '6 Months', '3 Months', 'Interen']
        self.entry_type_of_contract = ttk.Combobox(inner_frame_eight,
                                                   values=type_of_contract_choices,
                                                   state="readonly",
                                                   width=24,
                                                   font=self.label_font)
        self.entry_type_of_contract.pack(side="left", padx=10)
        self.entry_type_of_contract.current(0)

        inner_frame_nine = tk.Frame(inner_frame)
        inner_frame_nine.pack(fill="x")

        label_application_deadline = tk.Label(inner_frame_nine, width=30, pady=10,
                                              text="Application Deadline",
                                              bg=self.label_bg,
                                              font=self.label_font)
        label_application_deadline.pack(side="left")

        self.entry_application_deadline = tc.DateEntry(inner_frame_nine,
                                                       state="readonly",
                                                       font=self.label_font,
                                                       width=24)
        self.entry_application_deadline.pack(side="left", padx=10)

        inner_frame_ten = tk.Frame(inner_frame)
        inner_frame_ten.pack(fill="x", pady=10)

        label_frame = tk.Frame(inner_frame_ten)
        label_frame.pack(side="top", fill="x",padx=40)

        label_job_description = tk.Label(label_frame, pady=2,
                                         text="Job Description",
                                         font=self.label_font)
        label_job_description.pack(side="left", padx=35)

        def clear():
            self.entry_job_description.delete(1.0, tk.END)

        def buttelize():
            self.entry_job_description.insert(tk.INSERT, '\u2022')

        format_button = tk.Frame(label_frame)
        format_button.pack(side="right", fill="both")

        clr_button = tk.Button(format_button, text="Clear", command=clear, anchor='nw')
        clr_button.pack(side="left", pady=2, padx=10)

        bullet_button = tk.Button(format_button, text="Bullet", command=buttelize, anchor='e')
        photo_align = Image.open("icons/list_bullets.png")
        photo_align = photo_align.resize((20, 20), Image.ANTIALIAS)
        self.image_align_right = ImageTk.PhotoImage(photo_align)
        bullet_button.config(image=self.image_align_right)
        bullet_button.pack(side="right", pady=2)

        text_frame = tk.Frame(inner_frame_ten)
        text_frame.pack(side="right")

        textscrollbar = tk.Scrollbar(text_frame)

        self.entry_job_description = tk.Text(text_frame,wrap="word",
                                             font=self.label_font,
                                             width=50,
                                             height=5,
                                             yscrollcommand=textscrollbar.set)
        textscrollbar.config(command=self.entry_job_description.yview)
        textscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.entry_job_description.pack(fill="x", padx=15)

        inner_frame_11 = tk.Frame(inner_frame)
        inner_frame_11.pack(fill="x", pady=10)

        save_button = tk.Button(inner_frame_11, text="Save", bg=self.button_color, font=self.button_font,
                                fg=self.button_fg, command=threading.Thread(target=lambda: self.save_details(jb_dict, top)).start)
        save_button.pack(side="left", padx=180, pady=20)

        cancel_button = tk.Button(inner_frame_11, text="Cancel", bg=self.button_color, font=self.button_font,
                                  fg=self.button_fg, command=top.destroy)
        cancel_button.pack(side="left", pady=20)
        top.mainloop()

    def save_details(self, jb_dict, top):
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
            jt(self.root).jobs_table(self.first_frame)
            top.destroy()
        else:
            mb.showwarning('Warning', 'Please fill in the all the details')