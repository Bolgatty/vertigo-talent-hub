"""
author : Femy
date: 25/9/2020
"""
from jira import JIRA

class JiraTasks:
    """
     class that defines the methods for handling the JIRA functions like creation of issues..
    """
    def __init__(self, user_name, api_token, server):
        self.jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})

    def create_issue(self, test_data):
        issue_key = self.jira.create_issue(fields=test_data)
        return issue_key

    def update_issue_fields(self, issue_key, updated_test_data):
        issue = self.jira.issue(issue_key)
        issue.update(fields=updated_test_data)

    def delete_issue(self, issue_key):
        issue = self.jira.issue(issue_key)
        issue.delete()

    def fetch_all_resumes(self):
        summary_list = []
        key_list = []
        resumes = self.jira.search_issues('project=TH')
        for issues in resumes:
            summary_list.append(issues.fields.summary)
        print(summary_list)
        return summary_list

    def create_new_candidate(self, new_candidate_data):
        issue_key = self.jira.create_issue(fields=new_candidate_data)
        return issue_key
