__author__ = 'wangxiaodong'

import urllib.response

#1
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()

#2
req = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(req)
the_page = response.read()

#3 发送数据
import urllib.pase
import urllib.request

url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT'
values = {
    'act':'login',
    'login[email]':'yzhang@i9i8.com',
    'login[password]':'123456'
}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://www.python.org')
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))

#4 http   错误
req = urllib.request.Request('http://www.python.org')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode('utf8'))

#5 异常处理
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError

req = Request('http://twitter.com')
try:
    response  = urlopen(req)
except HTTPError as e:
    print('the server is could\'t fulfill the request.')
    print('Error code :', e.code)
except URLError as e:
    print('We failed to reach as server.')
    print('Reason:',e.reason)
else:
    print('good!')
    print(response.read().decode('utf8'))
