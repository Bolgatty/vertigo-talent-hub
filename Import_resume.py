import tkinter as tk
from  tkinter import *
from pyresparser import ResumeParser
from tkinter import filedialog
from jira import JIRA


user_name = ""
api_token = ""
server = ""
jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})

print(jira)

root = tk .Tk()
root.title('FIle Explorer')
root.withdraw()

file_path = filedialog.askopenfilenames(initialdir = "/",title = "Select a File",filetypes =(("pdf files","*.pdf"),("all files","*.*")))
#file_doc= filedialog.askopenfilenames(initialdir = "/",title = "Select a File",filetypes =(("pdf files","*.docx"),("all files","*.*")))
file_save = filedialog.askdirectory()

print ("Folder selected",file_save)
print ("File name:",file_path[0])
#print ("File doc",file_doc)

for index in range(len(file_path)-1):
    print("File Path",file_path[index])
    data = ResumeParser(file_path[index]).get_extracted_data()
    #for x, y in data.items():
    test_data =[
        {
            "project": "TAL",
            "summary": data['name'],
            "description": data['skills'],
            "issuetype": {"name": "Task"}
        }]
    issue_key = jira.create_issues(field_list=test_data)
    print(issue_key)



   