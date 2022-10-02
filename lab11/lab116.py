#!/usr/bin/python
n = int(input('count strings = '))
strl=list()
for i in range(n):
    s = input("input "+str(i+1)+" string: ")
    strl.append(s.split(' '))
D={}
for strg in strl:
    for substr in strg:
        if list(D.keys()).count(substr)==0:
            D[substr]=1
        else: D[substr]+=1
l2=list()
for key, val in D.items():
    l2.append((val,key))
for val,word in list(reversed(sorted(l2))):
    print(word)
input()
# print(sorted(l2))
# for key, val in A.items():
#     l2.append((val,key))
# print(A['a'])
# input()

