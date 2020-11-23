"""
 Author : Varsha
 Date   : 31/10/2020
"""
from configparser import ConfigParser

# create a file to save the path of .ini file and create a config .

file = r'D:\Bolgaty\Git Repo\vertigo-talent-hub\src\config\talenthunt.ini'
config = ConfigParser()
config.read(file)


# Read the values from the .ini file for the section jira_connect and fetch the values for server,user_name and api_token.
print(config.sections())
print(config['jira_connect'])
print(config['jira_connect']['server'])
print(config['jira_connect']['user_name'])
print(config['jira_connect']['api_token'])
print(config['jira_connect']['project'])

# Add a new section in .ini file using write 'w' option from talent_hunt_config file and add the values.
    #config.add_section('Label')
    #config.set('Label','vendor id','222')
    #config.set('Label','vendor label','test')
    #config.set('Label','candidate key','333')

    #with open(file, 'w') as configfile:
    #   config.write(configfile)


