#!/usr/bin/python
class DictBook():
    writings = list()
   
    def __init__(self,name):
        super().__init__()    
        self.name=name
        print("Dict "+str(name)+" was created!")
    def make_a_note(self,name,surname,birthday):
        self.writings.append((name,surname,birthday))
   
    def print_all_writings(self):
        for writing in self.writings:
            print("name: "+writing[0]+", surname: "+writing[1]+", birtday: "+writing[2])
   
    def print_particular_writing(self,index):
        if index>=len(self.writings): print("no such writing was found")
        else:
            s=self.writings[index]
            print("your writing is:\n name: "+s[0]+", surname: "+s[1]+", birthday: "+s[2])
    
    def sort_by_name(self):
        self.writings.sort(key=lambda tup: tup[0])
    
    def sort_by_surname(self):
        self.writings.sort(key = lambda tup: tup[1])
    def get_writing(self,name):
        for writing in self.writings:
            if writing[0]==name: return writing
    def remove_note_by_index(self,index):
        if index>=len(self.writings): print("no such writing was found")
        else:
            self.writings.remove(self.writings[index])
    def remove_note_by_name(self,name):
        self.writings.remove(self.writings.index(self.get_writing(name)))
    def clear(self):
        answer=input("are y sure?..\n")
        if answer == 'no': return
        elif answer == 'y':
            pasw=""
            while pasw!='y' :
                pasw=input("password:\n")
            self.writings.clear()       
            print("dict is clear..")
        else:
            return
d=DictBook('first')
d.make_a_note('ivan','ivanov','02,02,2002')
d.make_a_note('ivan2','ivanov2','03,02,2002')
d.make_a_note('alex','alexsurn','02,04,05')
d.make_a_note('zednul','zedsurn','02,03,2005')
d.print_all_writings()
d.sort_by_name()
d.print_all_writings()
d.clear()
