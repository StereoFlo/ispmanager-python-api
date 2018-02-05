class Credentials:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        pass

    login = ''
    password = ''

    def set_login(self, login):
        self.login = login
        return self

    def set_password(self, password):
        self.password = password
        return self
