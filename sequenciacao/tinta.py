import math

areapintada=float(input())

areagalao=18*3.6

qtddgalao=areapintada/areagalao

if areapintada<18:
    valorfinal=25
    qtddgalao=1
else:
    valorfinal=round(qtddgalao)*25

print(f" - área de cobertura: {round(areapintada)}")
print(f" - número de galões: {round(qtddgalao)}")
print(f" - valor a ser pago: R$ {valorfinal:.2f}")

#ver como coloca min de 1