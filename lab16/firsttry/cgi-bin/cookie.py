#!/usr/bin/env python3
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
name = cookie.get('name')
if name is None:
    print('Set-cookie: name=test')
    print('Content-type: text/html\n')
    print('cookie-test1')
else:
    print('Content-type: text/html\n')
    print('cookie-test2')
    print(name.value)