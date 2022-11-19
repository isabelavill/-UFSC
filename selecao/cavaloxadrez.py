import math

x1=int(input("Digite o valor de x1:"))
y1=int(input("Digite o valor de y1:"))
x2=int(input("Digite o valor de x2:"))
y2=int(input("Digite o valor de y2:"))

pode_moverse=math.sqrt( (x1-x2)**2 + (y1-y2)**2)==math.sqrt(5)

print(pode_moverse)