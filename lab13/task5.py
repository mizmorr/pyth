class Animal():
    name="null"
    def eat(self):
        print("namnem")
    def makenoise(self):
        print(self.name+" says grr")
    def __init__(self): print("new animal was born")
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
        
class Cat(Animal):
    name="noname"
    def __init__(self):
        print("new cat was born meow meow")
        Animal.__init__(self)
    def makeNoise(self):
        print(self.name, "says meow meow")
    
cat=Cat()
cat.makeNoise()