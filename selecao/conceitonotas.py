import math

#nota1, nota2, nota3= [float(w) for w in input().split()]
nota1=float(input())
nota2=float(input())
nota3=float(input())

media=(nota1+nota2+nota3)/3

if media<6:
    print("Insuficiente")
elif media<=7.5:
    print("Satisfatório")
elif media<=9:
    print("Bom")
elif media<=10:
    print("Ótimo")