from datetime import datetime

class User(object):

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")

    @classmethod
    def Laura_datetime(cls):
        new_username = "Laura_"
        new_username = new_username + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return cls(username="admin", password="admin")

