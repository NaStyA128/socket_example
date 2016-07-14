from werkzeug.wrappers import Request, Response
from wsgiref.simple_server import make_server


"""
def app(env, start_res):
    req = Request(env)
    # res = Response('Hello.', mimetype='text/html')
    # return res(env, start_res)
    print(req.args)
    print(req.form)
    print(req.session)
"""


@Request.application
def app(req):
    return Response('Hi')


if __name__ == '__main__':
    # 1 - host (по умолч. - localhost), 2 - port, 3 - application
    serv = make_server('', 8080, app)
    serv.serve_forever()
    serv.shutdown()

    # нам нужны (в основном):
    # QUERY_STRING - параметры в ссылке ?a=1&b=2
    # PATH
    # PATH_INFO - все, что после порта /add/book/
    # wsgi.input - файл-объект (хранит тело запроса)
    # CONTENT_LENGTH - чтобы правильно считать данные из wsgi.input
