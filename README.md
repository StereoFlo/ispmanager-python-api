# ISPManager Python API

sorry english version is not ready yet

Реализация клиента к API панели ISPManager на языке Python. PHP версию вы можете найти тут https://github.com/StereoFlo/ispmanager-php-api. Суть работы, та же, вы добавляете в isp_manager/func/Domain/ свою функцию и работаете с ней

##### Пример вызова приведен тут app.py:

Необходимые импорты

```python

from isp_manager.user import User
from isp_manager.server import Server
from isp_manager.isp_manager import IspManager
from isp_manager.func.Domain import add

```

Создаем объекты сервера и пользователя

```python

user = User('user', 'password')
server = Server('delta.hoster.net')
```

Создаюм объект функции (в данном случае - добавление домена)

```python

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

```

Создаем объект класса для работы со всеми данными установленными выше, работаем с ними и получаем результат

```python

isp_manager = IspManager()
isp_manager.set_server(server)
isp_manager.set_user(user)
isp_manager.set_func(func)
print(isp_manager.execute())

```