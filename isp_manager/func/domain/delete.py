from isp_manager.func import Func


class Delete(Func):
    def __init__(self, elid='', plid=''):
        if len(elid) != 0:
            self.elid = elid

        if len(plid) != 0:
            self.plid = plid

        Func.__init__(self, elid, plid)
        pass

    funcName = 'domain.delete'

    additional = {'webdomain': 'on', 'extop': 'on'}

    isSaveAction = True
