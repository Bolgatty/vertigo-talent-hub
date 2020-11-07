"""
author: Femy, Padma
Date : 09/10/2020
"""
from tools.json_parser import JsonParser as js
from database.JIRA_wrapper import JIRAWrapper as jw

class DatabaseManager:

    def __init__(self):
        self.label = "candidate"

    def check_duplicates(self, candidate_dict):
        """
        called from ResumeParser class for duplicate resume check
        :return: return true or false to Resume Parser as per value from the traverse_list method
        """
        encoded_string = self.get_encoded_summary(candidate_dict)
        summary_list = jw().retrive_summary(self.label)
        check_existence = self.traverse_list(summary_list, encoded_string)
        return check_existence

    def fetch_duplicate_resume(self, candidate_dict):
        """
        called from ResumeAnalyser().get_matched_desc() class to retrieve the
        duplicate resume data that is already existing in JIRA.
        :return: return matched resume
        """
        label = "candidate"
        desc_list = jw().retrive_desc(self.label)
        for desc in desc_list:
            desc_data = js().deserialization(desc)
            if desc_data['email'] == candidate_dict['email'] and desc_data['name'] == candidate_dict['name']:
                print('Name and Email Matching')
                return desc_data

    def traverse_list(self, resumes_summary, encoded_string):
        """
        method called from check_duplicates to traverse through the retrieved list from JIRA wrapper class
        for the existense of particular candidate
        :return: return true if any duplicates found else return false
        """
        for summary in resumes_summary:
            print("summary", summary)
            if summary == encoded_string:
                return True
        return False

    # can be replaced by JsonParsers deserilize() later
    def convert_to_json_string(self, data_dict):
        """
        called from add_new_candidate_db() to convert  dictionary to json
        :param data_dict: details of the candidate to be converted to json string
        :return: the converted json string item
        """
        json_string = js().serialization(data_dict)
        return json_string

    def get_encoded_summary(self, resume_dict):
        """
        method called from add_new_candidate_db() for encoded string for summary
        :param resume_dict: details of the candidate
        :return: encoded summary
        """
        name = resume_dict["name"]
        email = resume_dict["email"]
        phone_no = resume_dict["mobile_number"]
        encoded_summary = name+"#"+email+"#"+phone_no
        return encoded_summary

    def add_new_candidate_db(self, dict_data):
        """
        method called from add_issue_key method to add new candidate to JIRA if for the first time
        call the method of wrapper class to add new task to jira
        :param dict_data: details of the candidate
        :return: issue key if needed
        """
        json_string = self.convert_to_json_string(dict_data)
        encoded_summary = self.get_encoded_summary(dict_data)
        label_list = [self.label]
        print("inside db_manager", encoded_summary)
        candidate_key = jw().add_new_issue_JiraDB(json_string, encoded_summary, label_list)
        return candidate_key

    def add_issue_key(self, dict_data, file):
        """
        method called from the Resume Parser class to add new candidate
        and also it updates the issue key back to its description of the particular Issue
        :param file: contains path of the file that is selected
        :param dict_data: details of the candidate
        """
        issue_key = self.add_new_candidate_db(dict_data)
        dict_data['issue_key'] = str(issue_key)
        dict_string = self.convert_to_json_string(dict_data)
        update_data = {
            'description': dict_string
        }
        jw().update_jira(issue_key, update_data)
        print('Updated issue key in Jira')

    def update_new_resume(self, new_dict, old_dict):
        """
        method called from ResumeAnalyser's replace_candidate_resume() method to replace existing
        candidate's data in JIRA
        :param new_dict: contains new details
        :param old_dict: contains old details
        """
        new_dict['issue_key'] = old_dict['issue_key']
        issue_key = new_dict['issue_key']
        dict_string = self.convert_to_json_string(new_dict)
        update_data = {
            'description': dict_string
        }
        jw().update_jira(issue_key, update_data)
        print('Replaced new resume in Jira')