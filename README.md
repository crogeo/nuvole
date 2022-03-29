# nuvole
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/crogeo/nuvole/blob/master/LICENSE)

Nuvole is a simple wrapper of Python [tornado web framework ](https://www.tornadoweb.org)  - crogeo.org

## Installation
- From sources
```bash
git clone https://github.com/crogeo/nuvole.git
cd nuvole
pip install .
```
- From PyPi
```bash
pip install nuvole
```

## Documentation

- Usage
```python
from nuvole import Server, Service


class MyService(Service):

    PATH = r'/page/*'

    def get(self):
        self.write('Hello World')


if __name__ == '__main__':
    server = Server([MyService, ])
    server.run('localhost', 8080)
```


## License
Crogeo nuvole is [MIT licensed](./LICENSE).
