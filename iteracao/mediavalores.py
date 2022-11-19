tamanho_sequencia=int(input("Tamanho da sequência:"))
soma=0
'''
contador=1
while contador<=tamanho_sequencia:
    valor=float(input())
    soma+=valor
    contador+=1
media=soma/tamanho_sequencia
print(media)
    '''
for i in range(tamanho_sequencia):
    valor=float(input())
    soma+=valor
media=soma/tamanho_sequencia
print(media)