import math

comprimento=float(input())
largura=float(input())
num_gavetas=int(input())
madeira=input()

area=comprimento*largura
custo_mquadrado=area*100
custo_gavetas=num_gavetas*30


if area>2:
    acrescimo_area=50
else:
    acrescimo_area=0

if madeira=='mogno':
    acrescimo_madeira=150
elif madeira=='carvalho':
    acrescimo_madeira=125
else:
    acrescimo_madeira=0
    
custo_final=custo_mquadrado+custo_gavetas+acrescimo_area+acrescimo_madeira

print(f'{custo_final:2}')

#incompleto