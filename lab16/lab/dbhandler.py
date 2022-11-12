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


    
