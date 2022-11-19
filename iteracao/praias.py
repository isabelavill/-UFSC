qtdd_praias=int(input())

contador=1
maior=0 
mais_longe=''
dist_centro=0
media=0

while contador<=qtdd_praias:
    praia,distancia= input().split(';')
    dist=int(distancia)
    media+=dist
    if dist>maior:
        maior=dist
        mais_longe=praia
    if dist>=15 and dist<=20:
        dist_centro+=1
    contador+=1
media_dist =media/qtdd_praias  
print(f'{mais_longe};{dist_centro};{round(media_dist,1)}')