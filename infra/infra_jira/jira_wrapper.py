from jira import JIRA
import os
from dotenv import load_dotenv
from Utils.configurations import ConfigurationManager

# Load environment variables
load_dotenv("..\\..\\configs\\.env")


class JiraWrapper:
    def __init__(self):
        config_manager = ConfigurationManager()
        config_data = config_manager.load_settings("config_jira.json")
        TOKEN = os.getenv("JIRA_TOKEN")
        JIRA_USER = config_data["user"]
        jira_url = config_data["server"]
        # Authentication
        self.auth_jira = JIRA(basic_auth=(JIRA_USER, TOKEN), options={"server": jira_url})

    def create_issue(self, summery, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key


# if __name__ == "__main__":
#     jira = JiraWrapper()
#     print(jira.auth_jira)
#     print(jira.create_issue("this is a summery test1234", "this is a description test1234", 'KP'))
