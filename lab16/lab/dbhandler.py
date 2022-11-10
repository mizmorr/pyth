#!/usr/bin/python
import sqlite3
from sqlite3 import *
class Stud_DB():
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
    


        
    
