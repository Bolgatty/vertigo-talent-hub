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

    def create_issue(self, data):
        issue_key = self.jira.create_issue(fields=data)
        return issue_key

    def update_issue_fields(self, issue_key, updated_test_data):
        issue = self.jira.issue(issue_key)
        issue.update(fields=updated_test_data)

    def delete_issue_jira(self, issue_key):
        issue = self.jira.issue(issue_key)
        issue.delete()

    def fetch_all_summary(self):
        summary_list = []
        all_issues = self.jira.search_issues('project=TES')
        for issues in all_issues:
            summary_list.append(issues.fields.summary)
        return summary_list

    def fetch_all_desc(self):
        desc_list = []
        all_issues = self.jira.search_issues('project=TES')
        for issues in all_issues:
            desc_list.append(issues.fields.description)
        return desc_list

    def fetch_desc_basedon_label(self, label):
        desc_list = []
        all_issues = self.jira.search_issues('project=TES')
        for issues in all_issues:
            labels = issues.fields.labels
            if labels and labels[0] == label:
                desc_list.append(issues.fields.description)
        return desc_list

    def fetch_summary_basedon_label(self, label):
        summary_list = []
        all_issues = self.jira.search_issues('project=TES')
        for issues in all_issues:
            labels = issues.fields.labels
            if labels and labels[0] == label:
                summary_list.append(issues.fields.summary)
        return summary_list

    def fetch_spefic_issue_desc(self, issue_key):
        issue = self.jira.issue(issue_key, fields='description')
        return issue.fields.description

    def attach_file_to_jira_issue(self, issue_key, file):
        print("Inside Create")
        issue = self.jira.issue(issue_key)
        print(issue)
        self.jira.add_attachment(issue=issue, attachment=file)


