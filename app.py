from isp_manager.user import User
from isp_manager.server import Server
from isp_manager.isp_manager import IspManager
from isp_manager.func.Domain import add

user = User('user', 'password')
server = Server('delta.hoster.net')
func = add.Add()
func.set_additional({
    'name': 'domain.ru',
    'ip': '127.0.0.1',
    'ns': 'dns3.domain.net. dns1.domain.net. dns2.domain.net.',
    'ns_list': '',
    'mx': 'mail',
    'mx_list': '',
    'elid': '',
    'sok': 'ok',
})

isp_manager = IspManager()
isp_manager.set_server(server)
isp_manager.set_user(user)
isp_manager.set_func(func)
print(isp_manager.execute())
