"""
 author : Padmavathi V
 date   : 10/10/2020
"""

import configparser

class TalentConfig:
    # A class which is responsible for the config values
    config = configparser.ConfigParser()

    def __init__(self):
        configFilePath = r'C:\Users\jobs4\PycharmProjects\SmartHomeFramework\config\talenthunt.ini'
        self.config.read(configFilePath)

    def get_server_url(self):
        return self.config['jira_connect']['server']

    def get_server_user_name(self):
        return self.config['jira_connect']['user_name']

    def get_api_token(self):
        return self.config['jira_connect']['api_taken']
