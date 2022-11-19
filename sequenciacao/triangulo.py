import math

lado1=float(input("Lado 1:"))
lado2=float(input("Lado 2:"))
lado3=float(input("Lado 3:"))

print((lado1>abs(lado2-lado3)) and (lado1<(lado2+lado3)))