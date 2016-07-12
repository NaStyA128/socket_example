# расшир. модуль socket (высокоуровневый)
# реализ. баз. сервера HTTP, UDP...
# ВЫСОКОУРОВНЕВЫЙ СЕРВЕР
from socketserver import TCPServer, StreamRequestHandler
import socket


class Handler(StreamRequestHandler):

    # созд. несколько перем. объекта: self.request (наш сокет)
    # self.wfile - созд. файл для записи
    # self.rfile - созд. файл для чтения
    def handle(self):
        d = self.rfile.readline().strip()
        self.wfile.write(d)


if __name__ == '__main__':
    serv = TCPServer((socket.gethostname(), 1235), Handler)
    serv.serve_forever()
    serv.shutdown()
