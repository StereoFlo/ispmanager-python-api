from isp_manager.func import Func


class List(Func):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        self.funcName = 'domain'
        Func.__init__(self, elid, plid)
        pass
