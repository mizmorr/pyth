#!/usr/bin/python
from nltk.corpus import stopwords
def IsInList(l,word):
    if list(map(lambda x: x.lower(), l)).count(word.lower())==0:
        return 0
    else: return 1
notnecessarywords = stopwords.words('russian')
notnecessarywords.extend([',','-','.'])
file=input("input filename: ")
inp=open(file+".txt","r")
out=open("out.txt","w")
pre=inp.readlines()
strl=list()
for strs in pre:
    strl.append((strs.rstrip()).split(' '))

D={}
for strg in strl:
    for substr in strg:
        if IsInList(list(D.keys()),substr)==0:
            D[substr]=1
        else: D[substr]+=1

for val, key in sorted(D.items(),key=lambda x:x[1],reverse=True):
    t = str(val)+" "+str(key)+"\n"
    out.write(t)
    
out.close()
