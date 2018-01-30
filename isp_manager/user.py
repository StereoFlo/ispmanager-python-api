class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        pass

    login = ''
    password = ''

    def set_login(self, login):
        self.login = login
        return self
