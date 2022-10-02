def lclear (a):
    i = 0
    while a[i] ==' ':
        i+=1
    return a[i:]


def tosub(a:str):
    mas,strr,j=[],[],1
    mas.insert(0,0)
    a+=" "
    for i in range(len(a)):
        if a[i]==' ':
            mas.insert(j,i)
            j+=1
    for i in range (j-1):
        sbstr = lclear(a[mas[i]:mas[i+1]])
        strr.append(sbstr)
        # mas=[]
    # for i in range(len(strr)-1):
    #     if strr[i]==strr[i+1]: 
    #         mas.append(i)
    # for ind in mas:
    #     strr.remove(sstr[ind])
    return strr

def cleaner(a):
    str2 = tosub(a)
    mas=[]
    for i in range(len(str2)-1):
        if str2[i]==str2[i+1]: 
            mas.append(i)
    for ind in mas:
        del str2[ind]
    return (str2)

def res(input, output):
    try:
        inf = open(input,"r")
        outf = open(output,"w")
        lines = inf.readlines()
        lword,i="",0
        for line in lines:
            if i==len(lines)-1:
                prepreline=line[:-1]
                preline =cleaner(prepreline)
            else:
                preline=cleaner(line)
            
            if i>0 and preline[0]==lword:
                del preline[0]
            outf.write(' '.join(str(e)for e in preline))
            i+=1
            lword=(preline[len(preline)-1])[:-1]
        inf.close()
        outf.close()
        print("Complete")
    except FileNotFoundError:
        print("file not found")
        
filename = input("input filename1: ")
filename2=input("input filename2: ")
res("lab12/"+filename+".txt","lab12/"+filename2+".txt")


# inf = open(filename,"r")
# line=inf.readlines()
# while line !=" ":
#     print(line)
#     line=inf.readline()
# inf.close()
# for elem in line:
#     if elem == " ":
#         line.remove(elem)
# for elem in line:
#     print(elem)
# print(line[1],lclear(line[2]),line[3])
# asd=lclear(line[2])
# print(asd)
# print(lclear("   asd sd asd"))

input()