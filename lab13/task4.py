class Point():
    def __init__(self):
        print("new point created")
    x=0
    y=0
    def get(self):
        print("point - ("+str(self.x)+","+str(self.y)+")")
    def set(self,NNEWX, newY):
        self.x=NNEWX
        self.y=newY
    def sumofPoint(self):
        print(self.x+self.y)
    
p=Point()
p.get()  
