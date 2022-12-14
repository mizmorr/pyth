#!/usr/bin/python   
import sys, os, html,cgi
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from  dbhandler import Groups_table
groups = Groups_table()


form = cgi.FieldStorage()
action = form.getfirst("action", "")

if action == 'Input':
  name = html.escape(form.getfirst("name",''))
  set_id = html.escape(form.getfirst("set_id",''))
  groups.insert(name, set_id)
  
elif action == 'remove':
  bywhat = html.escape(form.getfirst('selector',''))
  what = html.escape(form.getfirst('delete',''))
  groups.delete(bywhat,what)
  
elif action == 'Update':
  pred, res={},{}
  updateby= html.escape(form.getfirst('updselector'))
  updparam = html.escape(form.getfirst('updparam'))
  pred['name'] = html.escape(form.getfirst("uname",''))
  pred['set_id'] = html.escape(form.getfirst("uset_id",''))
  for key, val in pred.items():
    if val!='':
      res[key]=val
  groups.update(updateby,updparam,res)


strings2 = groups.all_writings()
pattern = '''
<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8" />
  <title>Groups table</title>
  <style type="text/css">
   body { margin: 0; }
   #sidebar, #input,#test,#botm,#update { position: absolute; } 
   #sidebar, #input,#test,#botm,#update { overflow: auto; padding: 10px; }
   #header {
    height: 80px;
    background:  #f2f3f4 ; border-bottom: 2px solid  #34495e ;
   }
   #header h1 { padding: 20px; margin: 0; }
   #sidebar { 
    background:#f2f3f4  ; border-right: 2px solid  #34495e ;
    top: 82px; 
    bottom:200px;
    width:150px;
   }
   #input {
    top: 82px; 
    left: 172px; 
    bottom:200px;
    width:356px;
    background: #e6d7f5 ;
    border-right: 2px solid #34495e ;
   }
   #update
   {
    top: 82px; 
    left: 550px; 
    bottom:203px;
    width:350px;
    background:  #e6d7f5 ;
     
   }
   #test{
    top: 82px; 
    left: 920px; 
    bottom:200px;
    background:  #e6d7f5 ;
    right:0px;
    border-left:2px solid #34495e ;
   }
   #botm{
     top:760px;
     bottom:0px;
     background:#e6d7f5 ;
     width:2000px;
     border-top:2px solid  #34495e;
   }
   #subm{
     
  width:14em; height:2em;
  font-family: Arial, Helvetica, sans-serif;

}
   #birtd {
  width:13.3em;
}
  #deleter{
    width:7em
  }
#updater
{
  width:10em;
font: italic small-caps bold 19px/1 cursive;}
#updateparam{
    width:6em;
}

  </style>
 </head>
 <body>
  <div id="header"><h1>Groups</h1></div>
  <div id="sidebar"><h2>Navigation</h2>
<a href="http://localhost:8000/cgi-bin/begin_page.py">Back home</a><br><br>
  Other pages:
  <ul>
            <li> <a href="http://localhost:8000/cgi-bin/students_page.py">Students</a></li>
            <li> <a href="http://localhost:8000/cgi-bin/sets_page.py">Sets</a></li>
            <li> <a href="http://localhost:8000/cgi-bin/specialities_page.py">Specialities</a></li>
            <li> <a href="http://localhost:8000/cgi-bin/faculties_page.py">Faculties</a></li>
        <ul>
  </div>
  <div id="input">
  <form>
<form action="/cgi-bin/groups_page.py">
<h3>Input</h3>
<fieldset>
<legend>Group data</legend>
Name:<br> <input type = "text" name = "name" placeholder="36/2"/><br>
Set_ID:<br> <input type name = "set_id" placeholder ="1"/><br><br>               
<input type = "submit" id =subm name = 'action' value = 'Input' /><br><br>
</fieldset>
<h3>Delete</h3>
<fieldset>
delete by<br>
<select name = 'selector'>
  <option>id</option>
  <option>name</option>
  <option>set_id</option>
</select>
<br><br>
<input type = "text" id = 'deleter' name = "delete"/> 
<input type = "submit" name = 'action' value = 'remove'/>
</fieldset>
  </form>
  </div>
  <div id = "test"> <h3>Output</h3>
<button onclick="output()">get all notes</button>
<br><br>
<ul id="li">
</ul>
<script>
function output() {
  var x = document.createElement("LI");
  var t = document.createTextNode("'''+strings2[1:len(strings2)-1]+'''");
  x.appendChild(t);
  document.getElementById("li").appendChild(x);
  
}
</script>
  </div>
    <div id = "botm"> <h4>BOTTOM</h4></div>
  <div id = "update">
  <h3>Update</h3>
  <form action="/cgi-bin/groups_page.py">
  update by<br> 
<select name = updselector>
  <option>id</option>
  <option>name</option>
  <option>set_id</option>
</select>
<input type = "text" id = "updateparam" name ='updparam'/> 
<br><br>
change column's value<br><br>
<fieldset>
<legend>Update data</legend>
Name:<br> <input type = "text" name = "uname" placeholder="36/2"/><br> <br>
Set_ID:<br> <input type ="text" name = "uset_id" placeholder = "1"/><br><br>
<input type = "submit" id = updater name = 'action' value = 'Update' /><br><br>
</fieldset>
  </form>
  </div>
 </body>
</html>
'''

print('Content-type: text/html\n')
print(pattern)


        

