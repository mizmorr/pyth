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
ent = [
('Faculty of Romance and Germanic Philology','rgp'),
('Faculty of Management and Psychology' , 'fmp'),
('Faculty of Chemistry and High Technology','fcht'),
('Faculty of Physics and Technology','fpt'),
('Art and Graphic Arts faculty','fag'),
('Economic faculty','econom'),
('Faculty of Law','flaw') ]
# insert_faculties(con,ent)
entsets =[('GP-20',2020,7),
          ('Management-19',2019,8),
          ('CT-22',2022,9),
          ('RPH-18',2018,10),
          ('Graphics-21',2021,11),
          ('BI-20',2020,12),
          ('CL-21',2021,13)
    
]
# insert_sets(con,entsets)
# [('FIIT-20', 2020, 1),
# ('PMI-21',2021,2),
# ('PI-15',2015,3),
# ('PI-20',2020,3),
# ('FIIT-15',2015, 1),
# ('MSIS-16',2016,4),
# ('Geogr-18',2018,5),
# ('Hist-19',2019,6)
# ]
# insert_sets(con,entsets)
entitiesgroups=[('39/1',1),
('FIIT-15-a',5),
('PI-15-b',3),
('MSIS-16-a',6),
('Geogr-18-a',7)]  

entgroups = [('PI-20-a',4),
             ('Hist-19-a',8),
             ('GP-20-a',9),
             ('Management-19-b',10),
             ('CT-22-a',11),
             ('RPH-18-c',12),
             ('Graphics-21-a',13),
             ('BI-20-b',14),
             ('CL-21-a',15)]
# insert_groups(con,entgroups)
entspec = [('GP','german',4),
           ('Management','man',5),
           ('CT','chemistry technology',6),
           ('Radiophysics','rph',7),
           ('Graphics','gr',8),
           ('Business Informatics','business',9),
           ('Civil law','law',10)]
# insert_specialities(con,entspec)
#[('FIIT','fmsc',1),
# ('PMI','pmi',1),
# ('PI', 'pi',1),
# ('MSIS','msis',1),
# ('Geogrp','geogr',2),
# ('Hist','hist',3)]
entgroups2 = []
# insert_groups(con,entitiesgroups)
# insert_specialities(con,entspec)
entstud = [('Bob','Bobsurn',datetime.date(2004,12,2),'89182368213',11),
           ('John','R',datetime.date(2004,1,21),'8918833581',11),
           ('Bot','Rob',datetime.date(2000,7,1),'8960823281',12),
           ('Stud2','Surn2',datetime.date(2000,5,15),'8918865261',12),
           ('Stud3','Surn3',datetime.date(2003,8,9),'8918414803',13),
           ('Richard','Gilmor',datetime.date(2003,2,28),'8918825583',13),
           ('Dave','Richardson',datetime.date(2002,7,17),'8918814591',14),
           ('Ann','Bjorn',datetime.date(2002,5,11),'8918888932',14),
           ('Arthur','Doe',datetime.date(2003,8,17),'89188228202',15),
           ('Ann','Smith',datetime.date(2003,11,11),'89608383217',15),]
def selfomstud(con,name):
    curs=con.cursor()
    curs.execute('select id from Students where name='+'"'+name+'"')
    print("select id students with name="+name)
    print(curs.fetchall())
selfomstud(con,'Bob')
selfomstud(con,'Dave')
def studentsbyid(con,id):
    curs=con.cursor()
    curs.execute('select surname,birthday from Students where id='+str(id))
    print("select surname and birthday student with id="+str(id))
    print(curs.fetchall())
# studentsbyid(con,10)
# studentsbyid(con,17)
def delbyid(con,id):
    curs = con.cursor()
    curs.execute('delete from Students where id='+str(id))
    print("student with id = "+str(id)+" was deleted")
    con.commit()
# delbyid(con,31)
# delbyid(con,25)

def upgrade(con,id,newdescript,):
    curs = con.cursor()
    curs.execute('update Faculties set descript ='+'"'+newdescript+'"'+" where id="+'"'+str(id)+'"')
    print("descript was updated")
    con.commit()

# upgrade(con,1,"appmath")
# upgrade(con,7,'FPT')


def updateName(con,name,newname):
    curs = con.cursor()
    curs.execute('update Students set name ='+'"'+newname+'"'+"where name="+'"'+name+'"')
    print('name was changed')
    
# updateName(con,"Bot","RealBot")
# updateName(con,"John","Sam")