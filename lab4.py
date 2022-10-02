a = int (input ('A = '))
b = int (input ('B = '))

if a<b:
    for i in range (a,b+1):
        print (str(i)+'\t')
else: 
    for j in range(a,b-1,-1):
        print (str(j)+'\t')
print('Complete!\n')
input()