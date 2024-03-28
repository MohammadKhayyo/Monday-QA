import os

from dotenv import load_dotenv

load_dotenv()

authentic_users = [
    {"email": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")}
]


def get_all_valid_user():
    return authentic_users
