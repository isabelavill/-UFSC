import math

salario_bruto=float(input())

if salario_bruto <= 720:
    perc_inss=salario_bruto*0.0765
elif salario_bruto <= 1200:
    perc_inss=salario_bruto*0.09
elif salario_bruto <= 2400:
    perc_inss=salario_bruto*0.11
else:
    perc_inss=2400*0.11
    
print(perc_inss)