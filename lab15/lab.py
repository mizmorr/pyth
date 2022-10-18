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
    con.commit()
def insert_sets(con,entities):
    curs=con.cursor()
    for ent in entities:
            curs.execute('insert into Sets (name,year,speciality_id) values (?,?,?)',ent)
    con.commit()
def insert_groups(con,entities):
    curs=con.cursor()
    for ent in entities:
            curs.execute('insert into Groups (name,set_id) values (?,?)',ent)
    con.commit()
def insert_students(con,entities):
    curs=con.cursor()
    for ent in entities:
            curs.execute('insert into Students (name,surname,birthday,phone,group_id) values (?,?,?,?,?)',ent)
    con.commit()
con=sql_connection()
# entities=[('Apply Math','apply'),('Geography','geogr'),('Historical','about history')]
# insert_faculties(con,entities)
entsets = [('FIIT-20', 2020, 1),
('PMI-21',2021,2),
('PI-15',2015,3),
('PI-20',2020,3),
('FIIT-15',2015, 1),
('MSIS-16',2016,4),
('Geogr-18',2018,5),
('Hist-19',2019,6)
]
# insert_sets(con,entsets)
entitiesgroups=[('39/1',1),
('FIIT-15-a',5),
('PI-15-b',3),
('MSIS-16-a',6),
('Geogr-18-a',7)]  
entspec = [('FIIT','fmsc',1),
('PMI','pmi',1),
('PI', 'pi',1),
('MSIS','msis',1),
('Geogrp','geogr',2),
('Hist','hist',3)]
# insert_groups(con,entitiesgroups)
# insert_specialities(con,entspec)
entstud = [('Bob','Bobsurn',datetime.date(2004,2,2),'89601397602',1),
           ('John','Johnson',datetime.date(2004,4,24),'8960924692',1),
           ('Bot','Bot',datetime.date(1997,4,5),'8960814692',2),
           ('Stud2','Surn2',datetime.date(1997,4,15),'8918914692',3),
           ('Stud3','Surn3',datetime.date(1997,1,7),'8918303792',3),
           ('Stud2','Surn2',datetime.date(1998,4,15),'8918914692',4),
           ('Stud4','Surn4',datetime.date(1998,9,24),'8918914692',4),
           ('Ann','Bjorn',datetime.date(2000,3,12),'8918914882',5),
           ('Max','Doe',datetime.date(2000,5,7),'89188307602',5),
           ('Doe','Doe',datetime.date(1997,6,25),'89601397308',2),

]
# insert_students(con,entstud)
con.close()
# Init(con)
