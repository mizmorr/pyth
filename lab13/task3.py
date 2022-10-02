class StringVar():
    s_string="null"
    def get(self):
        print(self.s_string)
    def set(self,newstring):
        self.s_string=newstring
    
newstr=StringVar()
newstr.get()
newstr.set("new")
newstr.get()