"""Author : Vidhya Gayathri
Date : 08/10/2019
Program : This program converts a pdf/docx file into JSON string"""

from pyresparser import ResumeParser
from tools.json_parser import JsonParser
from src.db_manager import DatabaseManager


class ResumeAnalyser:

    def __init__(self):
        self.json_string = None

    def parse_resume(self, file_path):
        """
        method called from ImportResumeGUI().import_resume() for parsing the given file
        :param file_path: the file to be parsed
        :return: parsed file in dict object
        """
        print(file_path)
        dict_data = ResumeParser(file_path).get_extracted_data()
        # self.dict = resumeparse.read_file(file_path)
        return dict_data

    def create_new_candidate(self, data):
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
        result = DatabaseManager().check_duplicates(data)
        return result

    def save_candidate(self, data):
        """
        method called from ImportResumeGUI().import_resume() to save the new candidate in JIRA
        which again calls DatabaseManager's class method add_new_candidate_db()
        :param data: dict object
        """
        DatabaseManager().add_new_candidate_db(data)