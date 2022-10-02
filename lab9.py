

def somematr(n):
    a = [[0]*n for i in range(n)]
    for i in range(n-1,-1,-1):
        a[n-1-i][i]=1
        for j in range(0,i):
            a[i][j-i]=2
    for row in a:
        print(''.join([str(elem) for elem in row]))
        

# for row in a:
#         print(''.join([str(elem) for elem in row]))
        
somematr(4)
input()
