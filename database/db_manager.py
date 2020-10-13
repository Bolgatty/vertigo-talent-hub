"""
author: Femy, Padma
Date : 09/10/2020
"""
from tools.json_parser import JsonParser as js
from database.JIRA_wrapper import JIRAWrapper as jw


class DatabaseManager:

    def check_duplicates(self, candidate_dict):
        """
        called from ResumeParser class for duplicate resume check
        :return: return true or false to Resume Parser aas per value from the traverse_list method
        """
        encoded_string = self.get_encoded_summary(candidate_dict)
        summary_list = jw().get_all_resumes()
        check_existence = self.traverse_list(summary_list, encoded_string)
        print(check_existence)
        return check_existence

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
        called from add_new_candidate_db() to convert  json to dictionary
        :param data_dict: details of the candidate to be converted to dictionary
        :return: the converted dictionary item
        """
        # resume_dict = json.loads(json_string)
        # resume_dict = json.dumps(json_string, sort_keys=True, indent=3)
        json_string = js().serialization(data_dict)
        return json_string

    def get_encoded_summary(self, resume_dict):
        """
        method called from add_new_candidate_db() for encoded string for summary
        :param resume_dict: details of the candidate
        :return: encoded summary
        """
        name=resume_dict["name"]
        email=resume_dict["email"]
        phone_no = resume_dict["mobile_number"]
        encoded_summary = name+"#"+email+"#"+phone_no
        return encoded_summary

    def add_new_candidate_db(self, dict):
        """
        method called from the Resume Parser class to add new candidate to JIRA if for the first time
        call the method of wrapper class to add new task to jira
        :param dict: details of the candidate
        :return: issue key if needed
        """
        json_string = self.convert_to_json_string(dict)
        encoded_summary = self.get_encoded_summary(dict)
        label = "candidate"
        print("inside db_manager", encoded_summary)
        candidate_key =jw().add_new_issue_JiraDB(json_string, encoded_summary, ["candidate"])
        return candidate_key


# json_string = '{ "name":"Padma", "email":"pad@abc.com ", "phone_no":"0641435687"}'

# #
# # candidate_dict = json.loads(json_string)
# # print(candidate_dict)
#
# db_manager = DatabaseManager()
# #db_manager.add_new_candidate_db(json_string)
# candidate_dict=db_manager.convert_to_json_string(json_string)
# ret =db_manager.check_duplicates(candidate_dict)

