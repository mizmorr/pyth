#!/usr/bin/python
import sqlite3
from sqlite3 import *
class Stud_DB():
    test = 'test.txt'
    def __init__(self) -> None:
        self.con = sqlite3.connect('/home/mzzmor/pyth/lab15/lab15.db')
        try:
            with open(self.test, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.test, 'w', encoding='utf-8') as f:
                f.write('test')
    def all_writings(self):
        curs = self.con.cursor()
        curs.execute('select * from Students')
        l=curs.fetchall()
        begin:list = []
        for strgs in l:
            s = ' '.join(map(str,strgs))
            begin.append(s)
        return str(begin)     
    def write_in_test(self, text):
        with open(self.test, 'w', encoding='utf-8') as f:
            f.write(text)
            f.close()
            


        
    
