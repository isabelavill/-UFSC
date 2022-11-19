import math

a=int(input("Valor de a: " ))
b=int(input("Valor de b: "))
c=int(input("Valor de c: "))

delta=b**2-4*a*c
x1=(-b + math.sqrt(delta))/(2*a)
x2=(-b - math.sqrt(delta))/(2*a)

print("A raizes são:", x1, " e ", x2)