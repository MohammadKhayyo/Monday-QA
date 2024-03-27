from jira import JIRA
import os
from dotenv import load_dotenv
from Utils.configurations import ConfigurationManager

# Load environment variables
load_dotenv()


class JiraWrapper:
    def __init__(self):
        config_manager = ConfigurationManager()
        config_data = config_manager.load_settings("config_jira.json")
        TOKEN = os.getenv("JIRA_TOKEN")
        JIRA_USER = config_data["jira-user"]
        jira_url = config_data["jira_server"]
        # Authentication
        self.auth_jira = JIRA(basic_auth=(JIRA_USER, TOKEN), options={"server": jira_url})

    def create_issue(self, summery, description, project_key='KP', issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summery}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        print(f"Jira issue created: {new_issue}" if new_issue else "Failed to create Jira issue")
        return new_issue.key
