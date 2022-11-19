import math

#lado1, lado2, lado3=[int(w) for w in input().split()]
lado1=int(input())
lado2=int(input())
lado3=int(input())

if lado1==lado2 and lado1==lado3 and lado2==lado3:
    print("equilátero")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
    print("escaleno")
elif (lado1==lado2 and lado1!=lado3) or (lado2==lado3 and lado1!=lado2) or (lado1==lado3 and lado1!=lado2):
    print("isósceles") 