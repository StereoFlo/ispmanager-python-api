from isp_manager.func import func


class GetSoa(func.Func):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        func.Func.__init__(self, elid, plid)
        pass

    funcName = 'soa.edit'
