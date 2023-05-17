class emailModel():
    def __init__(self, email_to='', subject='', text='') -> None:
        self._email_to = email_to
        self._subject = subject
        self._text = text
        
    @property
    def email_to(self):
        return self._email_to

    @email_to.setter
    def email_to(self, value):
        self._email_to = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value