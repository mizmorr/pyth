a = [int(s) for s in input('list = ').split()]

even = []

for symb in a:
        if str(symb).isdigit and symb%2==0:
            even.append(symb)

print (even)
print('Complete!\n')
input()