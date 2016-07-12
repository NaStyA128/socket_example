# поддерж. HTTP, UDP и все
# мы не можем подменить заголовки запросов (в urllib)
# может подменить заголовки запросов (в urllib2) - useragent, contenttype
# менее высокоуровневая библ.
from urllib import request, response, error

# более высокоур. библиотека
import requests

if __name__ == '__main__':
    # 2 пар-р - словарь (если передаем data, то становится POST. по умолч. - GET)
    r = request.urlopen('http://python.org', data=b'a=1&b=2')
    print(r.read())
