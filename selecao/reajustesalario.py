import math

salario_atual=float(input())
salario_minimo=float(input())

if salario_atual<=(3*salario_minimo):
    reajuste=1.2
elif salario_atual<=(5*salario_minimo):
    reajuste=1.15
else:
    reajuste=1.1
    
novo_salario=salario_atual*reajuste
if novo_salario<(salario_minimo*1.5):
    novo_salario=salario_minimo*1.5
elif novo_salario>(salario_minimo*20):
    novo_salario=salario_minimo*20
    
print("%.2f" % novo_salario)
#print(round(novo_salario,2)) não mostra o zero
#print(f"{novo_salario:.2f}") mostra o zero