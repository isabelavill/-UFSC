import math
sequencia=int(input())

contador=1
menor_valor=-math.inf

while contador<=sequencia:
    valor=int(input())
    if contador==1:
        menor_valor=valor
    else:
        if valor < menor_valor:
            menor_valor=valor
    contador+=1
print(menor_valor)