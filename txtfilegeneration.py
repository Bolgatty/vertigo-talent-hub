#File Objects
from jira import JIRA

user_name = ""
api_token = ""
server = ""
jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})
description_list=[]

issue = jira.issue('TAL-26')
description_list.append(issue.fields.description)

with open('test2.txt','r') as rf:
      with open('test_copy.txt', 'w') as wf:
         for line in rf:
             wf.write(line)
      with open('test_copy.txt','a') as af:
         af.write("\n")
         af.write("JOB ID:")
         af.write("\n")
         af.write("JOB DESCRIPTION:")
         af.write("\n")
         af.write(description_list[0])
  





    # rf.seek(0)
    #
    # f_contents = rf.read(size_to_read)
    # print(f_contents, end='')


    #     chunk_size = 40
    #     rf_chunk = rf.read(chunk_size)
    #     while len(rf_chunk) > 0:
    #         wf.write(rf_chunk)
    #         rf_chunk = rf.read(chunk_size)
    #

    #      print(line, end='')


 #print(f.tell())




 #print(f_contents, end='')
# print(f.closed)
