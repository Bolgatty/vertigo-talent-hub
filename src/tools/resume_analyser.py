"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : This program converts a pdf/docx file into JSON string"""

from pyresparser import ResumeParser
from src.tools.json_parser import JsonParser
from src.db.db_manager import DatabaseManager as db


class ResumeAnalyser:

    def __init__(self):
        self.json_string = None

    def parse_resume(self, file_path):
        """
        method called from ImportResumeGUI().import_resume() for parsing the given file
        :param file_path: the file to be parsed
        :return: parsed file in dict object
        """
        dict_data = ResumeParser(file_path).get_extracted_data()
        return dict_data

    def candidate_data_to_string(self, data):
        """
        method called from ImportResumeGUI().import_resume() for encoded string
        converts a dict to a JSON string
        :param data: dict object
        :return: encoded JSON String
        """
        json_string = JsonParser().serialization(data)
        return json_string

    def json_validation(self, data):
        """
        method called from ImportResumeGUI().import_resume() to check if there is any duplicates found
        which again calls DatabaseManager's class method check_duplicates()
        :param data: dict object
        :return: return true if any duplicates found else return false
        """
        result = db().check_duplicates(data)
        return result

# --------------
    def get_matched_desc(self, data):
        """
        method called from ImportResumeGUI().save_candidate() to get matched candidate resume from JIRA
        which again calls DatabaseManager's class method fetch_duplicate_resume()
        :param data: dict object
        :return: return the matched resume from JIRA
        """
        matching_desc = db().fetch_duplicate_resume(data)
        return matching_desc
# --------------------

    def save_new_candidate_resume(self, data, file):
        """
        method called from ImportResumeGUI().save_candidate() to save the new candidate in JIRA
        which again calls DatabaseManager's class method add_issue_key()
        :param file: resume's file path
        :param data: dict object
        """
        db().add_issue_key(data, file)

    def replace_candidate_resume(self, new_data, old_data):
        """
        method called from ImportResumeGUI().save_candidate() to replace candidate's existing resume in JIRA
        which again calls DatabaseManager's class method update_new_resume()
        :param new_data: new dict object(new resume)
        :param old_data: dict object(Old resume)
        """
        db().update_new_resume(new_data, old_data)