massa=float(input())
segundos=0
nova_massa=0
if massa==0.5:
    segundos=50
elif massa==1:
    segundos=100
while massa>0.5 and massa!=1:
        nova_massa=massa*0.5
        segundos+=50
        massa=nova_massa
        if massa<0.5:
            break
        elif massa>=0.5:
            nova_massa=massa*0.5
print(segundos)