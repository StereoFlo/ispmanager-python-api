from isp_manager.func import func


class List(func.Func):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        self.funcName = 'domain'
        func.Func.__init__(self, elid, plid)
        pass
