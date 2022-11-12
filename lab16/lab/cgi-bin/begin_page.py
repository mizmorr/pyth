#!/usr/bin/env python3
pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Students data base</title>
<style type="text/css">
body { margin: 0; }

#header {
    height: 80px;
    background:  #f2f3f4 ; border-bottom: 2px solid  #34495e ;
   }
#header h1 { padding: 20px; margin: 0; }
</style>
</head>

<body>
  <div id="header"><h1>Students</h1></div>
<div id = "list_pages">
    <form action="/cgi-bin/begin_page.py">
        <ul>
            <li><a href="http://localhost:8000/cgi-bin/faculties_page.py">Faculties_SPage</a></li>
            <li><a href="http://localhost:8000/cgi-bin/students_page.py">Students_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/sets_page.py">Sets_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/groups_page.py">Groups_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/specialities_page.py">Specialities_Page</a></li>
        <ul>
    </form>
    </div>
</body>
</html>
'''

pattern2 = '''
<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8" />
  <title>Students data base</title>
  <style type="text/css">
   body { margin: 0; }  
   #header {
    height: 80px;
    background:  #f2f3f4 ; border-bottom: 2px solid  #34495e ;
   }
   #header h1 { padding: 20px; margin: 0; }
  </style>
 </head>
 <body>
  <div id="header"><h1>Students DB</h1></div>
        <ul>
            <li><a href="http://localhost:8000/cgi-bin/faculties_page.py">Faculties_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/students_page.py">Students_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/sets_page.py">Sets_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/groups_page.py">Groups_Page</a></li>
            <li><a href="http://localhost:8000/cgi-bin/specialities_page.py">Specialities_Page</a></li>
        <ul>
 </body>
</html>
'''

print('Content-type: text/html\n')
print(pattern2)


        


# pub = ''
# print('Content-type: text/html\n')
# print(pattern.format(publish=pub))
