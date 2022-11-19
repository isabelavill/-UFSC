import math

tempoduracao=int(input()) 

minutos=tempoduracao//60
if minutos>59:
    horafloat=minutos/60
    horaint=minutos//60
    min=(horafloat-horaint)*60
    minutos2=round(min)
    horas=minutos//60
    segundos=((tempoduracao/60)-minutos)*60

    print(f"{horas}:{minutos2}:{round(segundos)}")
else:   
    horas=minutos//60
    segundos=((tempoduracao/60)-minutos)*60
    
    print(f"{horas}:{minutos}:{round(segundos)}")