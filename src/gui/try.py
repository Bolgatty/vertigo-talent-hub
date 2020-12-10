from src.tools.json_parser import JsonParser as js
from src.db.JIRA_wrapper import JIRAWrapper as jw
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk


# label1 = [{'key':'a'}, {'key':'b'}, {'key':'c'}]
# label2 = [{'key':'a'}, {'key':'b'}, {'key':'d'}]
#
# label3 = [{'key':'g'}, {'key':'h'}, {'key':'a'}]
# label4 = [{'key':'u'}, {'key':'l'}, {'key':'g'}]

#label_list=[label1,label2,label3,label4]

root = tk.Tk()
root.geometry('740x510+0+0')

im_checked = ImageTk.PhotoImage(Image.open("images/icons/check.png"))
im_unchecked = ImageTk.PhotoImage(Image.open("images/icons/uncheck.png"))
skill_list = []

filter_button = tk.Button(root, text='Filter', command=lambda:get_matched_candidates(skill_list))
filter_button.place(x=200, y=400)

def treeview():
    label = tk.Label(root, text="Match Resumes", font=('', 12, 'bold'))
    label.place(x=230, y=20, relwidth=0.30)

    tabel_frame = tk.Frame(root)
    tabel_frame.place(x=100, y=70, relwidth=0.5, relheight=.5)

    tv = ttk.Treeview(tabel_frame, columns=(1), height="5")
    tv.place(relx=0, rely=0.05, relwidth=1, relheight=1)

    # Constructing vertical scrollbar
    verscrbar = ttk.Scrollbar(tabel_frame, orient="vertical", command=tv.yview)
    verscrbar.pack(side=tk.RIGHT, fill=tk.Y)

    tv.configure(yscrollcommand=verscrbar.set)

    style = ttk.Style(tv)
    style.configure("Treeview", rowheight=45)
    style.configure("Treeview.Heading", font=(None, 10, 'bold'))
    style.configure("Treeview.Heading", height=40)

    tv.tag_configure('checked', image=im_checked)
    tv.tag_configure('unchecked', image=im_unchecked)

    columns = ("#0", "#1")
    column_text = ("", "Skills")

    for x in range(len(columns)):
        tv.heading(columns[x], text=column_text[x])

    tv.column('#0', minwidth=0, width=75, anchor='center')
    tv.column('#1', minwidth=0, width=200, anchor='c')

    skills = fetch_all_skill_labels()

    for i in skills['skillset']:
        tv.insert('', 'end', values=i, tags='unchecked')

    def toggle_check(event):
        """
             method responsible when row(jobs table) is selected
             :param event: double click event occurs
        """
        try:
            rowid = tv.identify_row(event.y)  # returns selected row
            tag = list(tv.item(rowid, "tags"))[0]  # returns the items first element of the selected row
            tags = list(tv.item(rowid, "tags"))  # returns all the items of the selected row
            # tags.remove(tag) # removes the tag of the selected row
            tv.item(rowid, tags=tags)  # sets no tags to the selected row's item
            item = tv.item(tv.focus())

            if tag == "checked":
                tv.item(rowid, tags="unchecked")
                skill_list.remove(item['values'][0])
                print(skill_list)
            else:
                tv.item(rowid, tags="checked")
                item = tv.item(tv.focus())
                skill_list.append(item['values'][0])
                print(skill_list)

        except IndexError as e:
            print(e)

    tv.bind('<Double 1>', toggle_check)

def filter_candidates(candidate_list):
    matached_candidates = []
    matached_candidates.append(candidate_list[0])

    for x in range(len(candidate_list)):
        for i in candidate_list:
            for z in matached_candidates:
                if i['name'] == z['name']:
                    break
            else:
                matached_candidates.append(i)
    return matached_candidates

def fetch_all_skill_labels():
    skill_str = jw().retrieve_spefic_issue_desc('TH-240')
    skill_list = js().deserialization(skill_str)
    return skill_list

def get_matched_candidates(skilllist):
    jira_skills = []
    dict_candidates_list = []

    for i in skilllist:
        jira_skills.extend(jw().retrive_label_desc('skill#'+i))

    for j in jira_skills:
        dict_candidates_list.append(js().deserialization(j))

    matched_candidates = filter_candidates(dict_candidates_list)

    for x in matched_candidates:
        print('Matched Candidates:', x['name'])
    return matched_candidates

def get_exact_candidates():
    match_candidates = get_matched_candidates(skill_list)
    print(match_candidates)

    jira_skills = []
    dict_candidates_list = []

    for i in match_candidates:
        jira_skills.extend(jw().retrive_label_desc('skill#'+i))



exact_button = tk.Button(root, text='Exact Match', command=get_exact_candidates)
exact_button.place(x=400, y=400)


treeview()
root.mainloop()


