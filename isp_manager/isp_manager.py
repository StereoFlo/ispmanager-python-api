import requests


class IspManager:

    def __init__(self):
        pass

    server = ''
    user = ''
    format_name = 'json'
    func = ''
    url = ''
    urlParts = {}

    def set_server(self, server):
        self.server = server
        return self

    def set_user(self, user):
        self.user = user
        return self

    def set_format(self, format_name):
        self.format_name = format_name
        return self

    def set_func(self, func):
        self.func = func
        return self

    def execute(self):
        self.build_url()
        if self.func.get_issaveaction():
            req = requests.post(self.url, self.urlParts)
        else:
            req = requests.get(self.url, self.urlParts)

        print(req.content)
        return self

    def build_url(self):
        self.url = self.server.scheme + '://' + self.server.host
        self.prepare_url_port()
        self.prepare_url_user()
        self.prepare_url_format()
        self.prepare_url_func()
        self.prepare_additional()
        return self

    def prepare_url_port(self):
        if self.server.port:
            self.url += ':' + str(self.server.port) + '/?'
        else:
            self.url += '/?'
        return self

    def prepare_url_user(self):
        self.urlParts['authinfo'] = str(self.user.login) + ':' + str(self.user.password)
        return self

    def prepare_url_format(self):
        self.urlParts['out'] = self.format_name
        return self

    def prepare_url_func(self):
        self.urlParts['func'] = self.func.get_func()
        if self.func.get_elid():
            self.urlParts['elid'] = self.func.get_elid()
        if self.func.get_plid():
            self.urlParts['elid'] = self.func.get_plid()
        return self

    def prepare_additional(self):
        if self.func.additional:
            self.urlParts.update(self.func.additional)
        return self
