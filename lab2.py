def div0(a,b):
    return a%b or b%a


a = int (input ('a = '))
b = int (input ('b = '))
i = int (input ('i = '))
j = int (input ('j = '))

if a == i or b == j or div0(a,i) or div0(b,j):
    print ('ye')
else: ('cannot')
input()