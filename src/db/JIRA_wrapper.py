"""
author : Ashwini
date: 25/9/2020
"""
from src.db.create_JIRA_task import JiraTasks
from src.config.talent_hunt_config import config


class JIRAWrapper:
    user_name = config['jira_connect']['user_name']
    api_token = config['jira_connect']['api_token']
    server = config['jira_connect']['server']
    project = config['jira_connect']['project']
    jira = JiraTasks(user_name, api_token, server)

    def JIRA_connect(self):
        self.jira = JiraTasks(self.user_name, self.api_token, self.server)

    def get_all_tickets_summary(self):
        resume_list = self.jira.fetch_all_summary()
        return resume_list

    def get_all_tickets_desc(self):
        resume_list = self.jira.fetch_all_desc()
        return resume_list

    def add_new_issue_JiraDB(self, json_string, summary, label):
        new_data = {
            "project": "SBT",
            "summary": summary,
            "description": json_string,
            "labels": label,
            "issuetype": {"name": "Task"}
        }
        ret = self.jira.create_issue(new_data)
        return ret

    def update_jira(self, key, data):
        self.jira.update_issue_fields(key, data)

    def delete_issue(self, issue_key):
        self.jira.delete_issue_jira(issue_key)

    def retrive_summary(self, label):
        summary_lists = self.jira.fetch_summary_basedon_label(label)
        return summary_lists

    def retrive_desc(self, label):
        desc_lists = self.jira.fetch_desc_basedon_label(label)
        return desc_lists

    def retrieve_spefic_issue_desc(self, issue_key):
        desc = self.jira.fetch_spefic_issue_desc(issue_key)
        return desc

    def attach_file_in_jira(self, issue_key, file):
        self.jira.attach_file_to_jira_issue(issue_key, file)

