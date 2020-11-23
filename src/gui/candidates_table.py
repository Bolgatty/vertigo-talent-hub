import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime
from src.tools.resume_analyser import ResumeAnalyser as ra

class CandidateTable:
    candidate_id = []
    update_values = []

    def __init__(self, root, vendor_label, candidate_info_list):
        print('Inside CandidateTable')
        self.root = root
        self.vendor_label = vendor_label
        #self.candidate_info_list = candidate_info_list
        self.candidate_info_list = [{'name':'Rachel', 'email':'wedvv@gkjbc', 'mobile_number':'98f976976',
                                     'skills':['Python','Java','Cloud','Android']},
                                    {'name':'Ram', 'email':'vsf@gkjbc', 'mobile_number':'21n551',
                                     'skills':['Design','Security','HTML','Sales']},
                                    {'name':'Raja', 'email':'my,y@gkjbc', 'mobile_number':'5a55',
                                     'skills':['Css','Linux','Scheduling','MYSQL']},
                                    {'name':'Mahasri', 'email':'yil@gkjbc', 'mobile_number':'2n6151',
                                     'skills':['Github','Java','Azure','IOS']},
                                    {'name':'Monica', 'email':'wtjhwryj@gkjbc', 'mobile_number':'15n151',
                                     'skills':['Python','Linux','HTML','Css']}]
        self.id = 0
        for i in self.candidate_info_list:
            i['id'] = self.add_candidate_id()
        #self.top = tk.Toplevel(self.root)
        self.top = root
        #self.root.withdraw()
        self.top.geometry('700x800')
        #self.top.grab_set()
        self.top.resizable(False, False)
        self.bg_panel_header = '#000000'
        self.button_color = '#00917c'
        self.save_button_color = 'red'
        self.button_fg = 'white'
        self.button_font = 16
        self.label_font = 5
        self.label_bg = 'SystemButtonFace'
        self.bg_frame = 'white'
        self.candidate_id = []

        name_label = tk.Label(self.top, text="Name")
        name_label.place(x=135, y=420)

        self.name_entry = tk.Entry(self.top, width=30)
        self.name_entry.place(x=60, y=445)

        email_label = tk.Label(self.top, text="Email")
        email_label.place(x=325, y=420)

        self.email_entry = tk.Entry(self.top, width=30)
        self.email_entry.place(x=250, y=445)

        contact_label = tk.Label(self.top, text="Contact")
        contact_label.place(x=500, y=420)

        self.contact_entry = tk.Entry(self.top, width=30)
        self.contact_entry.place(x=440, y=445)

        skill_field_label = tk.Label(self.top, text="Skillset")
        skill_field_label.place(x=60, y=475)

        self.skill_field = tk.Text(self.top)
        self.skill_field.place(x=60, y=500, height=60, width=570)

        self.clear_button = tk.Button(self.top, text='Clear', command=self.clear)
        self.clear_button.place(x=630, y=440)

        self.select_button = tk.Button(self.top, text='Select Record', command=self.select)
        self.select_button.place(x=200, y=600)

        self.update_button = tk.Button(self.top, text='Update Record', command=self.update)
        self.update_button.place(x=300, y=600)

        self.delete_button = tk.Button(self.top, text='Delete Record', command=self.delete)
        self.delete_button.place(x=400, y=600)

        self.save_button = tk.Button(self.top, text='Save Records', width=10, command=self.save)
        self.save_button.place(x=250, y=700)

        self.cancel_button = tk.Button(self.top, text='Cancel',width=10, command=self.cancel)
        self.cancel_button.place(x=350, y=700)

    def cancel(self):
        self.top.destroy()
        self.root.deiconify()

    def clear(self):
        # Clear Entry boxes
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.skill_field.delete('1.0', tk.END)

    def select(self):

        self.clear()
        selected = self.tv.focus()
        if selected:
            #grab record values
            values = self.tv.item(selected, 'values')
            self.name_entry.insert(0, values[1])
            self.email_entry.insert(0, values[2])
            self.contact_entry.insert(0, values[3])
            self.skill_field.insert(tk.END, values[4])
        else:
            mb.showwarning("Warning", "Pls Select a row!", parent=self.top)

    def delete(self):
        selected = self.tv.focus()
        values = self.tv.item(selected, 'values')
        if mb.askyesno("Confirm Deletion", "Are you sure you want to delete the selected Record ?", parent=self.top):
            self.tv.delete(selected)
            for i in self.candidate_info_list:
                if values[0] == i['id']:
                    self.candidate_info_list.remove(i)
            mb.showinfo("Info", "Record Deleted!", parent=self.top)
            self.tv.delete(*self.tv.get_children())
            self.insert_values_table(self.candidate_info_list)
        if not self.candidate_info_list:
            print("EMpty")
            self.cancel()

    def update(self):
        selected = self.tv.focus()
        if selected:
            values = self.tv.item(selected, 'values')
            if self.name_entry.get() != "" and self.email_entry.get() != "" and self.contact_entry.get() != "" and self.skill_field.get("1.0","end") != "":
                self.tv.item(selected, text="", values=(values[0], self.name_entry.get(), self.email_entry.get(), self.contact_entry.get(), self.skill_field.get("1.0","end")))
                values = self.tv.item(selected, 'values')
                for i in self.candidate_info_list:
                    if values[0] == i['id']:
                        i['name'] = values[1]
                        i['email'] = values[2]
                        i['mobile_number'] = values[3]
                        i['skills'] = values[4]
                        print('updated candidate',i)
                mb.showinfo("Info", "Record Updated!", parent=self.top)
            else:
                mb.showwarning("Warning", "Pls fill all the fields", parent=self.top)
        else:
            mb.showwarning("Warning", "Pls select a row to update the values", parent=self.top)
        self.clear()

    def add_candidate_id(self):
        self.id += 1
        return '0' + str(self.id)

    def candidate_table(self, ):
        """
             method responsible in displaying all the candidates in a table format
        """
        print('Inside CandidateTable method')

        # candidate_frame = tk.Frame(self.top, bg=self.bg_frame)
        # candidate_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.label = tk.Label(self.top, text="Uploaded Resume Details", font=('', 12, 'bold'), bg=self.bg_frame)
        self.label.place(x=230, y=20, relwidth=0.30)

        self.tabel_frame = tk.Frame(self.top, bg=self.bg_frame)
        self.tabel_frame.place(x=40, y=70, relwidth=0.9, relheight=.4)

        self.tv = ttk.Treeview(self.tabel_frame, columns=(1, 2, 3, 4, 5), height="5")
        self.tv.place(relx=0, rely=0.05, relwidth=1, relheight=1)

        # Constructing vertical scrollbar
        verscrbar = ttk.Scrollbar(self.tabel_frame, orient="vertical", command=self.tv.yview)
        verscrbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Horizontal Scrollbar
        # horscrbar = ttk.Scrollbar(self.tabel_frame, orient="horizontal", command=self.tv.xview)
        # horscrbar.pack(side=tk.BOTTOM, fill=tk.X)

        # self.tv.configure(yscrollcommand=verscrbar.set, xscrollcommand=horscrbar.set)
        self.tv.configure(yscrollcommand=verscrbar.set)

        style = ttk.Style(self.tv)
        style.configure("Treeview", rowheight=45)
        style.configure("Treeview.Heading", font=(None, 10, 'bold'))
        style.configure("Treeview.Heading", height=40)

        style.theme_use("default")

        style.configure("Treeview",
                        background="white",
                        rowheight=45,
                        foreground="black",
                        fieldbackground="white")

        #Change selected Color
        style.map('Treeview',
                  background=[('selected', '#0080ff')])

        self.tv.tag_configure('oddrow', background='white')
        self.tv.tag_configure('evenrow', background='#b3d9ff')

        self.columns = ("#0", "#1", "#2", "#3", "#04","#05")
        column_text = ("","No", "Name", "Email", "Contact No.","Skills")

        for x in range(len(self.columns)):
            self.tv.heading(self.columns[x], text=column_text[x])

        self.tv.column('#0', minwidth=0, width=0, anchor='center')
        self.tv.column('#1', minwidth=0, width=75, anchor='c')
        self.tv.column('#2', minwidth=0, width=200, anchor='c')
        self.tv.column('#3', minwidth=0, width=200, anchor='c')
        self.tv.column('#4', minwidth=0, width=150, anchor='c')
        self.tv.column('#5', minwidth=0, width=0, anchor='c')

        self.insert_values_table(self.candidate_info_list)

        #self.tv.bind('<Double 1>', self.toggle_check) # toggle_check method is called when double click event occurs

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

            tags = list(self.tv.item(rowid, "tags")) # returns all the items of the selected row
            #tags.remove(tag) # removes the tag of the selected row
            self.tv.item(rowid, tags=tags) # sets no tags to the selected row's item
            self.item = self.tv.item(self.tv.focus())

            if tag == "checked":
                self.tv.item(rowid, tags="unchecked")
                self.candidate_id.remove(self.item['values'][0])
                print(self.candidate_id)
            else:
                self.tv.item(rowid, tags="checked")
                self.candidate_id.append(self.item['values'][0])
                print(self.candidate_id)

        except IndexError as e:
            print(e)
        self.set_cell_value(event)

    def set_cell_value(self, event):  # Double click to enter the edit state
        for element in self.tv.selection():
            print('element',element)
            item_text = self.tv.item(element, "values")

        column = self.tv.identify_column(event.x)  # column
        row = self.tv.identify_row(event.y)  # row
        print(column, row)
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))

        entryedit = tk.Entry(self.tabel_frame, width=10 + (cn - 1) * 16)
        entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)
        cell_value = self.selectItem(event)
        col = self.tv.identify_column(event.x)
        if col != '#0':
            entryedit.insert(tk.END, cell_value)

        def saveedit():
            x = list(item_text)
            self.candidate_id.remove(x[0])
            print(self.candidate_id)
            self.tv.set(element, column=column, value=entryedit.get())
            update_item_set = self.tv.item(element, "values")
            print('After update set', update_item_set)
            updated_values = list(update_item_set)
            self.candidate_id.append(update_item_set[0])
            print(self.candidate_id)
            for id in self.candidate_id:
                for i in self.candidate_info_list:
                    candidate_id = i['id']
                    print("candidate id", candidate_id)
                    if id == candidate_id:
                        print('matched:', i, candidate_id, self.vendor_label)
                        # ra().save_new_candidate_resume(i, self.vendor_label)

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

    def save(self):
        self.updating_info_list = []
        for i in self.candidate_info_list:
            self.updating_info_list.append(i)

        for data in self.candidate_info_list:
            print("inside save", data['name'])
            check_duplicate = ra().json_validation(data)
            if check_duplicate:
                print('x')
                matched_desc = ra().get_matched_desc(data)
                if mb.askyesno('Duplicate Existing', 'Candidate ' + matched_desc['name'] +
                                                     ' \'s resume is already existing!\n\n''Last Updated on ' +
                                                     matched_desc[
                                                         'date'] + '\n\n' 'Do you want to save updated Resume version??',
                               parent=self.top):
                    data['date'] = self.get_date_time()
                    ra().replace_candidate_resume(data, matched_desc)
                    mb.showinfo('Yes', 'Saved updated Resume', parent=self.top)
                    self.handle_table_display(data)
            else:
                data['date'] = self.get_date_time()
                ra().save_new_candidate_resume(data, self.vendor_label)
                mb.showinfo('Saved', 'Saved candidate '+ data['name'])
                self.handle_table_display(data)

        self.candidate_info_list = []
        for i in self.updating_info_list:
            self.candidate_info_list.append(i)

    def get_date_time(self):
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def handle_table_display(self, data):
        self.updating_info_list.remove(data)
        self.tv.delete(*self.tv.get_children())
        if self.updating_info_list:
            self.insert_values_table(self.updating_info_list)
        else:
            self.cancel()

    def insert_values_table(self, info_list):
        self.count = 1
        for i in info_list:
            if self.count % 2 == 0:
                self.tv.insert('', 'end', tags="evenrow", iid=self.count,
                               values=(i['id'], i['name'], i['email'], i['mobile_number'], i['skills']))
            else:
                self.tv.insert('', 'end', tags="oddrow", iid=self.count,
                               values=(i['id'], i['name'], i['email'], i['mobile_number'], i['skills']))
            self.count += 1


root = tk.Tk()
CandidateTable(root, 'testlable','kjbckj').candidate_table()
root.mainloop()