# web serwer gateway interface
# PEP 333

from wsgiref.simple_server import make_server
# from cgi import parse_qs, escape
# парсит параметры в ссылке и превращает их в словарь
from urllib.parse import parse_qs


def form(env):
    cl = int(env.get('CONTENT_LENGTH', '0'))
    d = env['wsgi.input'].read(cl)
    d = parse_qs(d)
    return d.get(b'a', b'1')[0]

route = {'form': form}


def app(env, resp_start):
    # созд. сервер
    # 1 - все переменные окружения, доп. пар-ры запроса; 2 -

    resp_start('200 OK', [('Content-Type', 'text/html')])
    buf = [('%s: %s <br />' % (k, v)).encode('UTF-8')
           for k, v in env.items()]

    qs = env.get('QUERY_STRING', '')
    qs = parse_qs(qs)

    path = env.get('PATH_INFO', '/')[1:]
    parts = path.split('/')
    print(parts[0])
    result = None
    result = [b'']
    if len(parts) > 0 and parts[0]:
        fn = route.get(parts[0])
        if fn is not None:
            result = fn(env)
            with open('index.html', 'r') as f:
                result = [(f.read() % (result,)).encode('UTF-8')]
    else:
        with open('index.html', 'r') as f:
            result = [(f.read() % (qs.get('a'),)).encode('UTF-8')]

    return result


# if __name__ == '__main__':
    # 1 - host (по умолч. - localhost), 2 - port, 3 - application
    # serv = make_server('', 8081, app)
    # serv.serve_forever()

    # нам нужны (в основном):
    # QUERY_STRING - параметры в ссылке ?a=1&b=2
    # PATH
    # PATH_INFO - все, что после порта /add/book/
    # wsgi.input - файл-объект (хранит тело запроса)
    # CONTENT_LENGTH - чтобы правильно считать данные из wsgi.input
