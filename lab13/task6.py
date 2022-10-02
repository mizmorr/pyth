class Animal():
    name="null"
    def eat(self):
        print("namnem")
    def makenoise(self):
        print(self.name+" says grr")
    def __init__(self): print("new animal was born")
    def getName(self):
        print (self.name)
    def setName(self,newName):
        self.name=newName
        
class Dog(Animal):
    name=""
    def makenoise(self):
        print(self.name, " says woof!")
    def __init__(self):
        print("new dog was born")
        Animal.__init__(self)
        
dog=Dog()
dog.setName("bobik")
dog.getName()
