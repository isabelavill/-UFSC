import math

distancia=float(input("Distancia percorrida:"))
combustivel=float(input("Combustível gasto:"))
# distancia,combustivel=[float(x) for x in input().split()]


consumo=distancia/combustivel

print(f"Consumo total: {consumo:2.5} Km/l ")
# print(round(consumo,3)) deixa só com 3 casas decimais 
#print(f"{consumo:.3f} km/l")