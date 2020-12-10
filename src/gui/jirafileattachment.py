from jira import JIRA


server = "https://talent-jira.atlassian.net/"
user_name = "talent.bolgatty20@gmail.com"
api_token = "WFDMSsAdUw8nukLagC4a13D7"


j = JIRA(basic_auth=(user_name, api_token), options={"server": server})
project = 'project=TH'
# upload file from `/some/path/attachment.txt`
#j.add_attachment(issue='TH-246', attachment='D:\Test Directory\Gunther.pdf')
all_issues = j.search_issues(project)
for issues in all_issues:
    for attachment in j.issues.fields.attachment:
        print("Name: '{filename}', size: {size}".format(
            filename=attachment.filename, size=attachment.size))
        # to read content use `get` method:
        print("Content: '{}'".format(attachment.get()))




