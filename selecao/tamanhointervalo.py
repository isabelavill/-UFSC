import math

#primeiro,ultimo = [int(w) for w in input("Primeiro e último valor:").split()]
primeiro=int(input())
ultimo=int(input())

if ultimo>primeiro:
    intervalo=(ultimo-primeiro)+1
elif primeiro>ultimo:
    intervalo=(ultimo-primeiro)-1
elif ultimo==primeiro:
    intervalo=1

print(abs(intervalo))