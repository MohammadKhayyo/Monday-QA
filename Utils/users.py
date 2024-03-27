import os

from dotenv import load_dotenv

load_dotenv()

authentic_user = [
    {"email": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")}
]


def get_all_valid_user():
    return authentic_user
