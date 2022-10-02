inp = input('input = ')
ct = inp.count('f')

if ct==0: 
    print()
elif ct==1:
    print('index of f - ', inp.find('f'))
else:
    print(inp.find('f'),inp.rfind('f'),sep =',', end ='.\n')
print('Complete!\n')
input()