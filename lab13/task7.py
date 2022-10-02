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
        
class Cat(Animal):
    name="noname"
    def __init__(self):
        print("new cat was born meow meow")
        Animal.__init__(self)
    def makeNoise(self):
        print(self.name, "says meow meow")
        
beast=Animal()
dog1=Dog()
dog2=Dog()
cat=Cat()
beast.setName("rex")
dog1.setName("bobik")
dog2.setName("ball")
cat.setName("koshka")
beast.eat()
beast.makenoise()
dog1.eat()
dog1.makenoise()
dog2.eat()
dog2.makenoise()
cat.eat()
cat.makeNoise()

