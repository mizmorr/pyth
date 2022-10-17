#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import datetime

def sql_connection():
    try:
        con = sqlite3.connect('lab15.db')
        return con
    except Error:
        print(Error)

def Init(con):
    curs = con.cursor()
    curs.execute("""CREATE TABLE Faculties(ID INTEGER 
                 primary key autoincrement,
                 name text NOT NULL,
                 descript text)""")
    curs.execute(""" create table Specialities(ID INTEGER 
                 primary key autoincrement,
                 name text NOT NULL,
                 descript text,
                 faculty_id integer,
                 constraint spec_facult_id foreign key (faculty_id) references Faculties (ID) on delete cascade 
                 )
                 """)
    curs.execute("""create table Sets(ID integer    primary key autoincrement,
                 name text NOT NULL,
                 year int,
                 speciality_id integer,
                 constraint spec_sets_id foreign key
                 (speciality_id) references Specialities (ID) on delete cascade                 
                 )
                 """)
    curs.execute("""create table Groups(ID INTEGER 
                 primary key autoincrement,
                 name text NOT NULL,
                 set_id integer,
                 constraint sets_groups_id foreign key (set_id)
                 references Sets (ID) on delete cascade 
                 ) 
                 """)
    curs.execute(""" create table Students(ID integer 
                 primary key autoincrement,
                 name text,
                 surname text,
                 birthday date,
                 phone text,
                 group_id integer,
                 constraint group_stud_fk foreign key (group_id) 
                 references Groups (ID) on delete cascade) 
                 """)
    con.commit()
def insert_faculties(con,entities):
    curs=con.cursor()
    for ent in entities:
        curs.execute('insert into Faculties(name,descript) values (?,?) ',ent)
    con.commit()
def insert_specialities(con,entities):
    curs=con.cursor()
    for ent in entities:
            curs.execute('''insert into Specialities (name,descript,faculty_id)
                         values(?,?,?)''',ent)
def insert_sets(con,entities):
    curs=con.cursor()
    for ent in entities:
            curs.execute('insert into Sets (name,year,speciality_id) values (?,?,?)',ent)
con=sql_connection()
entities=[('Apply Math','apply'),('Geography','geogr'),('Historical','about history')]
insert_faculties(con,entities)  
con.close()
Init(con)
