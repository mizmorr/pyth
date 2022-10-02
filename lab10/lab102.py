nlist = list(map(int,input("Input:  ").split()))

nlist2 = list(map(int,input("Input:  ").split()))

print(len(set(nlist)&set(nlist2)))