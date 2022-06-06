from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    def __init__(self, id, username, password, is_admin=False) -> None:
        self.id = id
        self.username = username
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


users = []


def get_user(username):
    for user in users:
        if user.username == username:
            return user
    return None
