n = int(input('n = '))

d,i=1,0

while d<n and d*2<n:
    d*=2
    i+=1
    
print('degree , value = ', i,d)
input()