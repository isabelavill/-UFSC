import math

valor_veiculo=float(input())
sexo=input()
idade=int(input())

premio_bruto=valor_veiculo*0.1

if sexo=='M':
    if idade<=24:
        desc_idade=0
    elif idade>=25 and idade<=33:
        desc_idade=0.1
    elif idade>33:
        desc_idade=0.2
    premio_liquido=premio_bruto*desc_idade
elif sexo=='F':
    if idade<=24:
        desc_idade=0.05
    elif idade>=25 and idade<=33:
        desc_idade=0.2
    elif idade>33:
        desc_idade=0.35
    premio_liquido=premio_bruto*desc_idade
    
print(premio_bruto-premio_liquido)