def gener(lst):
    dt=dict()
    for i in range(1,len(lst)):
        dt[str(lst[0])+str(i-1)]=lst[i]
    return dt

def preres(fkey,skey,ts,values):
    nlist=[]
    for i in range(len(ts)):
        if values.count(ts[i])!=0:
            nlist.append(str(fkey))
        else: nlist.append(str(skey))
    return nlist

def res(fdict:dict,sdict:dict,ts):
    fkey=str(fdict.keys())[0]
    skey=str(sdict.keys())[0]
    values=list(fdict.values())
    return preres(fkey,skey,ts,values)
    
fstlist = input("Input first dict:  ").split()
sndlist = input("Input second dict:  ").split()
towns = input("towns:  ").split()
# fl=['Russia','Moscow','Kaluga','Sp']
# sp=['Ukraine','Donetsk','Kiev']
# tws=['Donetsk','Sp','Kaluga']
# print(fl,sp,tws,sep='\n',end='\n')

fstdict=gener(fstlist)
snddict=gener(sndlist)
fkey=str(list(fstdict.keys())[0])[:-1]
skey=str(list(snddict.keys())[0])[:-1]
values=list(fstdict.values())
print(preres(fkey,skey,towns,values))
input()