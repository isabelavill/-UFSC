import math

largura,comprimento,altura=[int(w) for w in input().split()]
largura_navio,comprimento_navio,altura_navio=[int(w) for w in input().split()]

if altura > altura_navio:
    print(0)
elif comprimento > comprimento_navio:
    print(0)
elif largura > largura_navio:
    print(0)
else:
    area_container=comprimento*largura
    area_navio=comprimento_navio*largura_navio
    areamax=area_navio/area_container
    
    alturamax=altura_navio/altura
    
    qtdd_maxima_containers=round(alturamax)*areamax
    
    print(round(qtdd_maxima_containers))
    
#incompleto