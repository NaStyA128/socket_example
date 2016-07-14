import falcon
from wsgiref.simple_server import make_server


class Resource:

    @staticmethod
    def on_get(req, res):
        # on_ - и метод, кот. хотим обрабатывать
        # (POST, PULL, DELETE)
        res.body = '{"message": "test"}'
        res.status = falcon.HTTP_200
        # req.params
        # req.stream


if __name__ == '__main__':
    api = falcon.API()
    resource = Resource()
    api.add_route('/', resource)

    serv = make_server('', 8080, api)
    serv.serve_forever()
    serv.shutdown()
