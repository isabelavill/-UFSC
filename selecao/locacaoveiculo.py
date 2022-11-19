
num_dias=int(input())
km_rodados=float(input())

custo_dia=45*num_dias

km_extra=km_rodados-60*num_dias

custo_km=km_extra*0.5

print(custo_dia+custo_km)