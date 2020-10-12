"""
author : Ashwini
date: 25/9/2020
"""
from database.create_JIRA_task import JiraTasks


class JIRAWrapper:
    user_name = "username"
    api_token = "apitoken"
    server = "server"
    jira = JiraTasks(user_name, api_token, server)

    def JIRA_connect(self):
        self.jira = JiraTasks(self.user_name, self.api_token, self.server)

    def get_all_resumes(self):
        resume_list = self.jira.fetch_all_resumes()
        return resume_list

    def add_new_issue_JiraDB(self,json_string,summary,label):
        new_candidate_data = {
            "project": "TH",
            "summary": summary,
            "description": json_string,
            "labels":label,
            "issuetype": {"name": "Task"}
        }
        ret = self.jira.create_new_candidate(new_candidate_data)
        print(ret)



