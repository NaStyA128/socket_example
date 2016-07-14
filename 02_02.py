from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from wsgiref.simple_server import make_server


url_map = Map([
    Rule('/', endpoint='index'),
    Rule('/form', endpoint='form'),
    Rule('/form1/<id>', endpoint='form1')
])


def form(req):
    return Response('Hi222')


def form1(req, **v):
    print(v)
    return Response('Hi222')

route = {'form': form,
         'form1': form1}


@Request.application
def app(req):
    urls = url_map.bind_to_environ(req.environ)
    return urls.dispatch(lambda e, v: route[e](req, **v))


if __name__ == '__main__':
    serv = make_server('', 8080, app)
    serv.serve_forever()
