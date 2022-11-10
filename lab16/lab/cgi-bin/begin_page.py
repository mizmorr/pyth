#!/usr/bin/env python3
pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Students data base</title>
</head>
<h>Test</h>
<body>
    <form action="/cgi-bin/handler.py">
    <a href="http://localhost:8000/cgi-bin/students_page.py">Std_Page</a>
        <p>Begin</p>
        <ul>

            <li>технологов</li>
            <li>мыслителей</li>
            <li>строителей</li>
        <ul>
       <p>работающих вместе ... </p>
    </form>
</body>
</html>
'''


pub = ''
print('Content-type: text/html\n')
print(pattern.format(publish=pub))
