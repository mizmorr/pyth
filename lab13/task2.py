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
        
anim=Animal()
anim.getName()
anim.setName("first")
anim.eat()
anim.makenoise()

