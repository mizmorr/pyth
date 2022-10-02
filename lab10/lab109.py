def polyglot():
    n=int(input("count students: "))
    alang = int(input("lang count of 1 student: "))
    flist = list()

    for i in range(alang):
        lang = input("type "+str(i+1)+" lang: ")
        flist.append(str.strip(lang))
    unionlang=flist
    intersectlang=flist
    for i in range(1,n):
        alang = int(input("lang count of "+str(i+1)+" student: "))
        prelang=list()
        for i in range(alang):
            lang = input("type "+str(i+1)+" lang: ")
            prelang.append(str.strip(lang))
        unionlang=list(set.union(set(prelang),set(unionlang)))
        intersectlang=list(set.intersection(set(prelang),set(unionlang)))

    print(len(intersectlang))  
    for leng in sorted(intersectlang):
        print(leng) 
    print(len(unionlang))
    for leng in sorted(unionlang):
        print(leng)
    input()

polyglot()