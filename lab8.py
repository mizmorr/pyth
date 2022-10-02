def power(a,n):
    if n==1:
        return a
    else:
        return a*power(a,n-1)

def downpow(a,n):
    s = power(a,n)
    return 1/s

print(downpow(8,1))
input()