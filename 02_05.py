from twisted.web import server, resource
from twisted.internet import reactor


class Simple(resource.Resource):
    isLeaf = True

    @staticmethod
    def render_GET(request):
        return 'Hello world!'


if __name__ == '__main__':
    site = server.Site(Simple())
    reactor.listenTCP(9000, site)
    reactor.run()
