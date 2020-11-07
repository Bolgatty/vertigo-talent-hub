"""Author : Vidhya Gayathri
Date : 15/10/2019
Program : This program manages the backend of JD GUI"""

from src.tools.json_parser import JsonParser as js
from src.db.JIRA_wrapper import JIRAWrapper as jw


class JDManager:

    def __init__(self):
        self.label = "jobs"
        self.issue_key = 'TES-74'

    def get_particular_desc(self, issue_key):
        particular_desc = jw().retrieve_spefic_issue_desc(issue_key)
        job_desc = js().deserialization(particular_desc)
        return job_desc

    def job_id_generator(self):
        job_id_tracker = jw().retrieve_spefic_issue_desc(self.issue_key)
        job_id_desc = js().deserialization(job_id_tracker)
        id = int(job_id_desc['id'])
        job_id = id+1
        return job_id

    def get_encoded_summary(self, job_dict):
        comp_name = job_dict['company_name']
        job_title = job_dict['job_title']
        encoded_summary = "#"+comp_name+'#'+job_title
        return encoded_summary

    def add_new_job_db(self, job_dict):
        json_string = js().serialization(job_dict)
        encoded_summary = self.get_encoded_summary(job_dict)
        label = [self.label]
        print("inside jd_manager", encoded_summary)
        job_key = jw().add_new_issue_JiraDB(json_string, encoded_summary, label)
        return job_key

    def add_issue_key(self, jb_dict):
        issue_key = self.add_new_job_db(jb_dict)
        jb_dict['issue_key'] = str(issue_key)
        dict_string = js().serialization(jb_dict)
        data = {
            'description': dict_string
        }
        jw().update_jira(issue_key, data)
        print('Updated issue key in Jira')

    def fetch_all_jobs(self):
        label = "jobs"
        jobs_list = jw().retrive_desc(label)
        job_dict = []
        for jobs in jobs_list:
            job = js().deserialization(jobs)
            job_dict.append(job)
        return job_dict

    def delete_job(self, issue_key):
        jw().delete_issue(issue_key)

    def update_job(self, issue_key, data):
        dict_string = js().serialization(data)
        update_data = {
            'description': dict_string
        }
        jw().update_jira(issue_key, update_data)
        print('Replaced new resume in Jira')

    def update_job_id_tracker(self, updated_id):
        dict = {}
        dict['id'] = updated_id
        job_id_string = js().serialization(dict)
        updated_desc = {
            'description': job_id_string
        }
        jw().update_jira(self.issue_key, updated_desc)
        print('Updated job_id tracker in Jira')

    def converttodict(self, data_list):
        #data_list = ['JD011', 'Java + Python Developer', 'LUXOFT INFORMATION TECHNOLOGY', '12/11/20', 'TES-90']
        dict_data = {
            'job_id':data_list[0] ,
            'job_title':data_list[1],
            'company_name':data_list[2],
            'application_deadline':data_list[3],
            'issue_key':data_list[4]
        }
        return dict_data



