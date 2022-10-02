

def gener(a,b,c):
    res = set([elem for elem in range(b,a,c)])
    return res

def getpair(a:list,ind):
    return a[ind:ind+2]

def preresult(alist:list,b):
    A:list=[]
    if len(alist)%2!=0: return 0
    else:
        for i in range(0,len(alist),2):
            nlist = getpair(alist,i) 
            a,c = nlist[0],nlist[1] 
            preres= gener(b,a,c)
            A.append(preres)
        return result(A)

def sort(s:set):
    l=[]
    for elem in s:
        if elem%6==0 or elem%7==0:
            l.append(elem)
    return s.difference(set(l))
    
def result(l:list):
    A:set=l[0]
    for i in range(1,len(l)):
        B=l[i]
        A.update(B)
    return sort(A)

def resfunc(s,N):
    res=preresult(s,N)
    print(res)
    print(len(res))
    return "Complete!"
    
n = int(input('N = '))

nlist = list(map(int,input("Input:  ").split()))

# print(resfunc([2,3,3,5,9,8],19))

print(resfunc(nlist,n))
input("")

# A=set([elem for elem in range(5)])
# B=set([e for e in range(4,6)])
# print(A.symmetric_difference(B))
# print(len(nlist)%2==0)
# print(gener(19,6,2))
