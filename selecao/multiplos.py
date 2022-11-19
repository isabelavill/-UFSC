import math

valor1, valor2=[int(w) for w in input().split()]

if valor1%valor2==0 or valor2%valor1==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")