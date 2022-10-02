def pluslist(a,b):
    for i in range(len(a)):
        a[i]+=b
def f(a:list):
        a.sort()
        realres,omore=[],[]
        j=0
        b=a[j+1:]
        pluslist(b,a[j])
        # print(b)
        c=a[j+1:]
        preres,prev,res=[],[],[]
        for i in range(len(c)):
            s = b.copy()
            s.remove(c[i]+a[j])
            # print(c[i])
            pluslist(s,c[i])
            # print(s)
            # print(a[0],s,c[i],i)
            preres=c.copy()
            preres.remove(c[i])
            preres.reverse()
            # print(preres)
            prev+=preres
            # if i<len(res):
            #     prev.append(res[i])
            res+=s
            # print(prev)
        # print(preres)
        # print(prev)
        # prev=c.copy()
        # print(prev)
        for i in range(len(res)):
            # s=preres.copy()
            # s.remove(a[0]+c[i]+prev[i])
            # print(s)
            # pluslist(s,prev[i])
            # res+=s
            # if (res[i]+prev[i])%9==0:
            #     omore.append(prev[i])
            #     omore.append(j)
                # omore.append(res[i])
            res[i]+=prev[i]

            # for i in range (len(res)):
            #     if res[i]%9==0:
            #         realres.append(res[i])
            realres+=res
        print(omore)
    # realres.sort()
        print(realres)

def getset(a,sm):
    for i in range(len(a)):
        if sum(a[i])==sm:
            return a[i]
def make_f(a):
   
        ressets=list()
        for i in range(len(a)):
            curlist = a[i+1:]
            if len(curlist)>4:
                curnum =a[i]
                curdoubles=pluslist(curlist,curnum)
                curtriples=list()
                for j in range(len(curdoubles)):
                    j+=1
            else: return ressets.sort()[0]


res,sums,a2=list(),list(),list()


def mincomb(num,last,inlist):
    if num == 4:
        pre=list()
        for i in range(4):
                pre.append(a2[i])
        if  sum(pre)%9==0:
                res.append(pre)
                sums.append(sum(pre))
    for i in range(last+1,len(inlist)):
        a2.append(inlist[i])
        mincomb(num+1,i,inlist)
        a2.pop(len(a2)-1)

def resfunc(a):
    if len(a)<4:
        print("cannot make that set")
    elif len(a)==4:
        if len(a)%9:
            print(sum(a))
        else:
            print("cannot make that set")
    else:
        mincomb(0,-1,a)
        print("min - ", min(sums))
        print("set - ", getset(res,min(sums)))
        print("all sets -", res)


            
filename = input("input filename: ")
flag = False
while flag==False:
    try:
        inf = open("itask1/"+filename+".txt","r")  
        line = inf.readline()
        flag=True
        inf.close()
        l =list(map(int,list(line.split(' '))))
        resfunc(l)
    except FileNotFoundError:
        print("file not found. try again...")
        filename = input("input filename: ")

input()