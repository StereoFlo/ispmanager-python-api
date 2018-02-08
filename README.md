# ISPManager Python API

sorry, english version is not ready yet

Реализация клиента к API панели ISPManager на языке Python. PHP версию вы можете найти тут https://github.com/StereoFlo/ispmanager-php-api. Суть работы, та же, вы добавляете в isp_manager/func/Domain/ свою функцию и работаете с ней

##### Пример вызова приведен в файле app.py:

Необходимые импорты

```python

from isp_manager.credentials import Credentials
from isp_manager.server import Server
from isp_manager import IspManager
from isp_manager.func.domain import Add


```

Создаем объекты сервера и пользователя
У конструктора объекта Server могут быть дополнительные параметры: порт и схема работы (https/http)

```python

user = Credentials('user', 'password')
server = Server('delta.hoster.net')
```

Создаюм объект функции (в данном случае функция это добавление домена)

```python

func = Add()
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