from isp_manager.func import func


class Add(func.Func):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        self.funcName = 'domain.edit'
        self.isSaveAction = True
        func.Func.__init__(self, elid, plid)
        pass

    def set_additional(self, additional):
        if 'ns' in additional:
            additional['ns'] = additional['ns'].replace(" ", "+")
        self.additional = additional
        return self
