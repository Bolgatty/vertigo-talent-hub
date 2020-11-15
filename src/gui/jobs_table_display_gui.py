import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from src.tools.thread_pool_jd import ThreadPoolJDM as jdm


class JobsTable:
    issue_key_list = []
    selected_job_id = []
    update_values = []

    def __init__(self, root):
        self.root = root
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.save_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.label_font = 5
        self.label_bg = 'SystemButtonFace'
        self.bg_frame = 'white'
        self.im_checked = ImageTk.PhotoImage(Image.open("src/gui/images/icons/check.png"))
        self.im_unchecked = ImageTk.PhotoImage(Image.open("src/gui/images/icons/uncheck.png"))

    def jobs_table(self, first_frame):
        """
             method responsible in displaying all the jobs in a table format
        """
        self.label = tk.Label(first_frame, text="Available Jobs", font=('', 12, 'bold'), bg=self.bg_frame)
        self.label.place(relx=0.34, rely=0.30, relwidth=0.25)

        self.tabel_frame = tk.Frame(first_frame, bg=self.bg_frame)
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
        style.configure("Treeview", rowheight=45)
        style.configure("Treeview.Heading", font=(None, 10, 'bold'))
        style.configure("Treeview.Heading", height=40)

        self.tv.tag_configure('checked', image=self.im_checked)
        self.tv.tag_configure('unchecked', image=self.im_unchecked)

        self.columns = ("#0", "#1", "#2", "#3", "#4", "#5")
        column_text = ("", "Job ID", "Job Title","Company Name","Application Deadline","Issue Key")

        for x in range(len(self.columns)):
            self.tv.heading(self.columns[x], text=column_text[x])

        self.tv.column('#0', minwidth=0, width=75, anchor='center')
        self.tv.column('#1', minwidth=0, width=75, anchor='c')
        self.tv.column('#2', minwidth=0, width=150, anchor='c')
        self.tv.column('#3', minwidth=0, width=150, anchor='c')
        self.tv.column('#4', minwidth=0, width=150, anchor='c')
        self.tv.column('#5', minwidth=0, width=150, anchor='c')


        #jobs = jd().fetch_all_jobs()
        #Thread class where Job manager function fetch all jobs is called through thread class to run in a separate thread.
        jobs = jdm(self.root).workerThread1()
        print(jobs)

        for i in jobs:
            self.tv.insert('', 'end', tags="unchecked",
                           values=(i['job_id'], i['job_title'], i['company_name'],
                                   i['application_deadline'], i['issue_key']))

        self.tv.bind('<Double 1>', self.toggle_check) # toggle_check method is called when double click event occurs

        for i in range(len(self.columns)):  # bind function to make the header sortable
            if i!=0:
                self.tv.heading(self.columns[i], text=column_text[i], command=lambda _col=self.columns[i]: self.treeview_sort_column(self.tv, _col, False))

    def selectItem(self, event):
        curItem = self.tv.item(self.tv.focus())
        col = self.tv.identify_column(event.x)
        cell_value = ''
        for i in range(1, len(curItem['values'])+1):
            colvalue = '#'+str(i)
            if col == '#0':
                return None
            if col == colvalue:
                cell_value = curItem['values'][i-1]
        print('cell_value = ', cell_value)
        return cell_value

    def toggle_check(self, event):
        """
             method responsible when row(jobs table) is selected
             :param event: double click event occurs
        """
        try:
            rowid = self.tv.identify_row(event.y) # returns selected row
            tag = list(self.tv.item(rowid, "tags"))[0] # returns the items first element of the selected row

            for i in self.tv.get_children():
                self.tv.item(i, tags="unchecked")

            tags = list(self.tv.item(rowid, "tags")) # returns all the items of the selected row
            #tags.remove(tag) # removes the tag of the selected row
            self.tv.item(rowid, tags=tags) # sets no tags to the selected row's item
            self.item = self.tv.item(self.tv.focus())

            if tag == "checked":
                JobsTable.selected_job_id.remove(self.item['values'][0])
                JobsTable.issue_key_list.remove(self.item['values'][4])
                JobsTable.update_values.remove(self.item['values'])
                print(JobsTable.selected_job_id)
                print(JobsTable.issue_key_list)
                print(JobsTable.update_values)
            else:
                if JobsTable.selected_job_id:
                    x=JobsTable.selected_job_id.pop()
                    y=JobsTable.issue_key_list.pop()
                    z=JobsTable.update_values.pop()
                    print("Pop elements",x,y,z)
                self.tv.item(rowid, tags="checked")
                self.item = self.tv.item(self.tv.focus())
                JobsTable.update_values.append(self.item['values'])
                JobsTable.selected_job_id.append(self.item['values'][0])
                JobsTable.issue_key_list.append(self.item['values'][4])
                print(JobsTable.update_values)
                print(JobsTable.selected_job_id)
                print(JobsTable.issue_key_list)

        except IndexError as e:
            print(e)

    def toggle2(self, event):
        """
             method responsible when row(jobs table) is selected, makes sure only one row is selected at a time
             :param event: double click event occurs
        """
        for i in self.tv.get_children():
            self.tv.item(i, tags="unchecked")
        self.toggle_check(event)

    def set_cell_value(self, event):  # Double click to enter the edit state
        for element in self.tv.selection():
            item_text = self.tv.item(element, "values")

        column = self.tv.identify_column(event.x)  # column
        row = self.tv.identify_row(event.y)  # row
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))

        entryedit = tk.Entry(self.tabel_frame, width=10 + (cn - 1) * 16)
        entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)
        cell_value = self.selectItem(event)
        col = self.tv.identify_column(event.x)
        if col != '#0':
            entryedit.insert(tk.END, cell_value)

        def saveedit():
            self.update_values.remove(list(item_text))
            self.tv.set(element, column=column, value=entryedit.get())
            update_item = self.tv.item(element, "values")
            self.update_values.append(list(update_item))
            entryedit.destroy()
            okb.destroy()

        okb = ttk.Button(self.tabel_frame, text='OK', width=4, command=saveedit)
        okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)

    def treeview_sort_column(self, tv, col, reverse):  # Treeview, column name, arrangement
        if col != '#0':
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            print(col)
            l.sort(reverse=reverse)  # Sort by
            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):  # based on sorted index movement
                tv.move(k, '', index)
                tv.heading(col, command=lambda: self.treeview_sort_column(tv, col,
                                                                     not reverse))  # Rewrite the title to make it the title of the reverse order