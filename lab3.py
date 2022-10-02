from math import *


hours = int (input ('hours = '))
mins = int (input ('minutes = '))
sec = int (input ('seconds = '))

secres = hours*3600+mins*60+sec

preres = secres/43200

if preres > 1:
    print ('too much')
else: print(preres*360)
input()