import random
import string


def create_secure_string(size=6):
    char_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    if size < 4:
        raise ValueError("String size must be at least 4 to ensure a mix of character types.")
    secure_str = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    secure_str += random.choices(char_pool, k=size - 4)
    random.shuffle(secure_str)
    return ''.join(secure_str)
