from func_interface import FuncInterface


class Func(FuncInterface):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        pass

    isSaveAction = False

    funcName = ''

    elid = ''

    plid = ''

    additional = {}

    def set_additional(self, additional):
        self.additional = additional
        return self

    def get_func(self):
        return self.funcName

    def get_elid(self):
        return self.elid

    def get_plid(self):
        return self.plid

    def get_additional(self):
        return self.additional

    def get_issaveaction(self):
        return self.isSaveAction
