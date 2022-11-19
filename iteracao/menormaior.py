sequencia=int(input())
contador=1
maior=0
posicao=1
while contador<=sequencia:
    for i in range(1,sequencia+1):
        n=int(input())
        if contador==1:
            maior=n
        else:
            if maior < n:
                maior=n
                posicao=contador
        contador+=1
        
print(maior, posicao)

