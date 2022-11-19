import math

inteiro=int(input("Valor inteiro:"))
inicio=int(input("Inicio do intervalo:"))
fim=int(input("Fim do intervalo:"))

'''
if inteiro>=inicio and inteiro<=fim:
    dentro_intervalo=True
else:
    dentro_intervalo=False
'''

dentro_intervalo = inicio<=inteiro and fim>=inteiro
print(dentro_intervalo)