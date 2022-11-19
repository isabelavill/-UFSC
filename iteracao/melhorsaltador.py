qtdd_saltadores=int(input())
contador=1
maior=0
vencedor=''
while contador<=qtdd_saltadores:
    salto1,salto2,salto3,nome=input().split()
    s1=float(salto1)
    s2=float(salto2)
    s3=float(salto3)
    if s1>maior:
        maior=s1
        vencedor=nome
    elif s2>maior:
        maior=s2
        vencedor=nome
    elif s3>maior:
        maior=s3
        vencedor=nome
    contador+=1
print(vencedor)
    