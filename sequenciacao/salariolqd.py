import math


horaextra=12.5*1.2


hit=int(input())
het=int(input())

sbruto=hit*12.5+het*horaextra
sliquido=sbruto*0.78


print(f"- Salário Bruto : R$ {sbruto:.2f}")
print(f"- IR (13%) : R$ {sbruto*0.13:.2f}")
print(f"- INSS (9%) : R$ {sbruto*0.09:.2f}")
print(f"- Salário Líquido : R$ {sliquido:.2f}")