
#valor=int(input())
#contador=valor
#fatorial=1
#while contador>1:
#    fatorial*=contador
#    contador-=1
#print(f'Fatorial de {valor} é igual a {fatorial}')

def fatorial(numero):
    fat=1
    for i in range(numero,1,-1):
        fat=fat*i
    return fat

n=int(input())
print(fatorial(n))