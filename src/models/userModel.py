from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id='', email='', password=''):
        self._id = id
        self._email = email
        self._password = password

    def get_id(self):
        return str(self.id)

    def get_email(self):
        return str(self.email)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
