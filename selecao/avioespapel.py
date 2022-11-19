import math

competidores, folhasdiretora, folhascompetidor=[int(w) for w in input().split()]

folhas_por_competidor=folhasdiretora/folhascompetidor

if round(folhas_por_competidor)%competidores==0:
    print('S')
else:
    print('N')



