#!/usr/bin/python
def IsInList(l,word):
    if list(map(lambda x: x.lower(), l)).count(word.lower())==0:
        return 0
    else: return 1
file=input("input filename: ")
inp=open(file+".txt","r")
out=open("out.txt","w")
pre=inp.readlines()
letters=list()
for strs in pre:
    plist=((strs.rstrip()).split(' '))
    for word in plist:
        for letter in word:
            letters.append(letter)
            
D={}
for letter in letters:
    if IsInList(list(D.keys()),letter)==0:
        D[letter]=1
    else: D[letter]+=1
    
for val, key in sorted(D.items(),key=lambda x:x[1],reverse=True):
    t = str(val)+" "+str(key)+"\n"
    out.write(t)
print("Complete")