from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id='', email='', password=''):
        self.id = id
        self.email = email
        self.password = password

    def get_id(self):
        return str(self.id)

    def get_email(self):
        return str(self.email)
