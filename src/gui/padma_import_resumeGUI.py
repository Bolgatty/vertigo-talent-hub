"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : This program contains Import Resume GUI"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from src.thread_pool import ThreadPool
from src.resume_analyser import ResumeAnalyser


class ImportResumeGUI:
    """
     class that defines the methods responsible for GUI
    """

    def __init__(self, root):
        """
        constructor will be called from main file when ImportResumeGUI's class object is initiated
        :param root: an instance of Tkinter’s Tk class that creates a window
        """
        self.root = root

        #self.master = tk.Toplevel()

        canvas = tk.Canvas(self.root, height=400, width=800)
        canvas.pack()

        self.frame = None
        self.frame_import_panel = None
        self.file = None
        self.dict = None
        self.frame_import_confirmation = None
        self.entry_name = None
        self.entry_email = None
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.import_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.confirm_panel_font = 12
        self.bg_frame = '#8cffee'
        self.initial_display()

    def initial_display(self):
        """
        method called from constructor to exhibit initial display
        """
        self.root.title('Import Resume')

        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        img = ImageTk.PhotoImage(Image.open("whity.png"))
        panel = tk.Label(self.frame, image=img)
        panel.image = img
        panel.place(x=0, y=0)

        b = tk.Button(self.frame, text='Import Resume', bg=self.button_color, fg=self.button_fg,
                      font=self.button_font, command=self.open_import_panel)
        b.place(relx=0.37, rely=0.37, relwidth=0.25, relheight=0.25)

    def open_import_panel(self):
        """
        method called when Import Resume button is clicked from the initial display
        """
        self.frame.place_forget()

        self.frame_import_panel = tk.Frame(self.root, bg=self.bg_frame)
        self.frame_import_panel.place(relx=0, rely=0, relwidth=1, relheight=1)

        img = ImageTk.PhotoImage(Image.open("whity.png"))
        panel = tk.Label(self.frame_import_panel, image=img)
        panel.image = img
        panel.place(x=0, y=0)

        import_file_desc = tk.Label(self.frame_import_panel, text='Please select a file',
                                    bg=self.bg_panel_header, fg='white', font=16)
        import_file_desc.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.1)

        browse_button = tk.Button(self.frame_import_panel, bg=self.button_color, fg=self.button_fg,
                                  font=self.button_font, text='Browse', command=self.browse_resume)
        browse_button.place(relx=0.3, rely=0.40, relwidth=0.17, relheight=0.1)

        cancel_button1 = tk.Button(self.frame_import_panel, bg=self.button_color, fg=self.button_fg,
                                   font=self.button_font, text='Cancel', command=self.initial_display)
        cancel_button1.place(relx=0.55, rely=0.40, relwidth=0.17, relheight=0.1)

    def browse_resume(self):
        """
        method called when browse button is clicked from open import panel
        """

        print('open browser')
        self.file = fd.askopenfile(initialdir="/", title="Select file",
                                   filetypes=(("all files", "*.*"), ("all files", "*.*")))
        try:
            import_file_path_label = tk.Label(self.frame_import_panel, text='File Name :'+self.file.name,
                                              bg='white', font=5)
            import_file_path_label.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)

            import_button = tk.Button(self.frame_import_panel, bg=self.import_button_color,
                                      fg=self.button_fg, font=self.button_font, text='Import',
                                      command=self.import_resume)
            import_button.place(relx=0.43, rely=0.55, relwidth=0.17, relheight=0.1)
        except Exception as e:
            print(e)

    def import_resume(self):
        """
        method called when import button is clicked from open import panel
        """
        try:
            exception_test = False
            file_extension = self.file.name.split('.')
            print(file_extension)
            extension = file_extension[len(file_extension) - 1]
            if extension != 'pdf' and extension != 'DOCx' and extension != 'docx':
                print(extension)
                raise Exception('Wrong Format Extension')
        except Exception as e:
            exception_test = True
            print("Error:", e)

        if exception_test:
            mb.showerror('Error', 'Upload Resume in PDF/DOCx format only!!')
            self.open_import_panel()
        else:
            self.dict = ThreadPool(ResumeAnalyser().parse_resume(self.file.name))
            try:
                '''thread module - padma'''
                #check_tag = "parse_resume"
                # data= []
                # self.master = tk.Toplevel()
                # self.dict = ThreadPool\
                #     (self.master, self.file.name, check_tag, data).workerThread1()
                #self.root.withdraw()
                print("padma", self.dict)
                '''thread module - padma'''
                #self.dict = ResumeAnalyser().parse_resume(self.file.name)
                print('Display Name and email fields')

                self.success_display(self.dict)
            except Exception as e:
                print("Error:", e)
                mb.showerror('Error', 'This file does\'nt seem to be a resume!! \nUpload Resume in PDF/DOCx format only!!')
                self.open_import_panel() 

    def success_display(self, data):
        """
        called from import_resume() if no duplicates of particular candidate found
        :param data: contains dict
        """
        print("inside Success_display")
        self.frame_import_panel.place_forget()

        self.frame_import_confirmation = tk.Frame(self.root, bg=self.bg_frame)
        self.frame_import_confirmation.place(relx=0, rely=0, relwidth=1, relheight=1)


        img = ImageTk.PhotoImage(Image.open("whity.png"))
        panel = tk.Label(self.frame_import_confirmation, image=img)
        panel.image = img
        panel.place(x=0, y=0)

        confirm_details_label = tk.Label(self.frame_import_confirmation, text='Please Confirm the details',
                                         bg=self.bg_panel_header, fg='white', font=16)
        confirm_details_label.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.1)

        label_name = tk.Label(self.frame_import_confirmation, bg="white",
                              text='Name', font=self.confirm_panel_font)
        label_name.place(relx=0.1, rely=0.23, relwidth=0.25, relheight=0.1)

        self.entry_name = tk.Entry(self.frame_import_confirmation)
        self.entry_name.place(relx=0.38, rely=0.23, relwidth=0.52, relheight=0.1)
        self.entry_name.insert(0, data['name'])

        label_email = tk.Label(self.frame_import_confirmation,
                               bg="white", text='Email', font=self.confirm_panel_font)
        label_email.place(relx=0.1, rely=0.36, relwidth=0.25, relheight=0.1)

        self.entry_email = tk.Entry(self.frame_import_confirmation)
        self.entry_email.place(relx=0.38, rely=0.36, relwidth=0.52, relheight=0.1)
        self.entry_email.insert(0, data['email'])

        label_contact_no = tk.Label(self.frame_import_confirmation,
                               bg="white", text='Contact Number', font=self.confirm_panel_font)
        label_contact_no.place(relx=0.1, rely=0.49, relwidth=0.25, relheight=0.1)

        self.entry_contact_no = tk.Entry(self.frame_import_confirmation)
        self.entry_contact_no.place(relx=0.38, rely=0.49, relwidth=0.52, relheight=0.1)
        self.entry_contact_no.insert(0, data['mobile_number'])

        save_button = tk.Button(self.frame_import_confirmation, bg=self.button_color,
                                fg=self.button_fg, font=self.button_font, text='Save',
                                command=self.save_candidate(data))
        save_button.place(relx=0.3, rely=0.65, relwidth=0.17, relheight=0.1)

        cancel_button1 = tk.Button(self.frame_import_confirmation, bg=self.button_color,
                                   fg=self.button_fg, font=self.button_font, text='Cancel',
                                   command=self.open_import_panel)
        cancel_button1.place(relx=0.52, rely=0.65, relwidth=0.17, relheight=0.1)
        print(data)

    def save_candidate(self, data):
        """
        method called when save button is clicked
        :param data: contains the data to be saved into JIRA
        """
        name = self.entry_name.get()
        data['name'] = name
        email = self.entry_email.get()
        data['email'] = email
        contact_no = self.entry_contact_no.get()
        data['mobile_number'] = contact_no
        '''thread module - padma'''
        #check_tag = "json_validation"
        # jsonstring = ResumeAnalyser().create_new_candidate(data)
        #self.master = tk.Toplevel()
        #check_duplicate = ThreadPool(self.master, self.file.name, check_tag, data).workerThread1()

        # self.root.withdraw()
        #print("padma", check_duplicate)
        '''thread module - padma'''
        check_duplicate = ResumeAnalyser().json_validation(data)
        if check_duplicate:
            print('x')
            mb.showwarning('Duplicate Existing', 'Candidate ' + data['name'] + 's resume is already existing!\n')
        else:
            '''thread module - padma'''
            check_tag = "save_candidate"
            #self.master = tk.Toplevel()
            #ThreadPool(self.master).workerThread1()
            # self.root.withdraw()
            #print("padma-saved candidate")
            ''' thread module - padma'''
            ResumeAnalyser().save_new_candidate_resume(data, self.file.name)
            print(data)
            mb.showinfo('Saved', 'Saved New candidate into Jira Database')
            print('Saved New candidate into Jira Database')
            self.initial_display()

root = tk.Tk()
ImportResumeGUI(root)
root.mainloop()