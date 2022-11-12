#!/usr/bin/python
import sqlite3
from sqlite3 import *

def d_str(d:dict):
    s = ''
    for key, _ in d.items():
        s+=str(key)+"="+'"'+str(d[key])+'"'+','
    return s[:-1]

class Stud_table():
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Students')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin) 

    def insert(self, name,surname,birthday,phone,group_id):
        cursor = self.con.cursor()
        cursor.execute(f'insert into Students (name,surname,birthday,phone,group_id) values ("{name}","{surname}","{birthday}","{phone}",{group_id})')
        self.con.commit() 
        
    def update(self, updby,updparam, dict):
        cursor = self.con.cursor()
        sets = d_str(dict)
        cursor.execute(f'update Students set {sets} where {updby}="{updparam}"')
        self.con.commit()
        
    def delete(self,del_by,del_what):
        cursor = self.con.cursor()
        cursor.execute (f'delete from Students where {del_by}="{del_what}"')
        self.con.commit()

class Facult_table():
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Faculties')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin) 

    def insert(self, name,descript):
        cursor = self.con.cursor()
        cursor.execute(f'insert into Faculties (name,descript) values ("{name}","{descript}")')
        self.con.commit() 
        
    def update(self, updby,updparam, dict):
        cursor = self.con.cursor()
        sets = d_str(dict)
        cursor.execute(f'update Faculties set {sets} where {updby}="{updparam}"')
        self.con.commit()
        
    def delete(self,del_by,del_what):
        cursor = self.con.cursor()
        cursor.execute (f'delete from Faculties where {del_by}="{del_what}"')
        self.con.commit()
        
class Groups_table():
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Groups')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin) 

    def insert(self, name,set_id):
        cursor = self.con.cursor()
        cursor.execute(f'insert into Groups (name,set_id) values ("{name}","{set_id}")')
        self.con.commit() 
        
    def update(self, updby,updparam, dict):
        cursor = self.con.cursor()
        sets = d_str(dict)
        cursor.execute(f'update Groups set {sets} where {updby}="{updparam}"')
        self.con.commit()
        
    def delete(self,del_by,del_what):
        cursor = self.con.cursor()
        cursor.execute (f'delete from Groups where {del_by}="{del_what}"')
        self.con.commit()
        
class Sets_table():
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Sets')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin) 

    def insert(self, name,year,speciality_id):
        cursor = self.con.cursor()
        cursor.execute(f'insert into Sets (name,year,speciality_id) values ("{name}","{year}","{speciality_id}")')
        self.con.commit() 
        
    def update(self, updby,updparam, dict):
        cursor = self.con.cursor()
        sets = d_str(dict)
        cursor.execute(f'update Sets set {sets} where {updby}="{updparam}"')
        self.con.commit()
        
    def delete(self,del_by,del_what):
        cursor = self.con.cursor()
        cursor.execute (f'delete from Sets where {del_by}="{del_what}"')
        self.con.commit()
    
class Spec_table():
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Specialities')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin) 

    def insert(self, name,descript,faculty_id):
        cursor = self.con.cursor()
        cursor.execute(f'insert into Specialities (name,descript,faculty_id) values ("{name}","{descript}","{faculty_id}")')
        self.con.commit() 
        
    def update(self, updby,updparam, dict):
        cursor = self.con.cursor()
        sets = d_str(dict)
        cursor.execute(f'update Specialities set {sets} where {updby}="{updparam}"')
        self.con.commit()
        
    def delete(self,del_by,del_what):
        cursor = self.con.cursor()
        cursor.execute (f'delete from Specialities where {del_by}="{del_what}"')
        self.con.commit()
        
        
    
