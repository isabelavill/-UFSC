import math

comprimento_estrada,distancia_pedagio=[int(w) for w in input().split()]
custo_km,valor_pedagio=[int(w) for w in input().split()]

qtdd_pedagio=comprimento_estrada/distancia_pedagio
custo_pedagio=valor_pedagio*round(qtdd_pedagio)
gasto_km=comprimento_estrada*custo_km

#print("Valor gasto com pedágios:",custo_pedagio)
#print("Valor gasto por km percorrido:",gasto_km)
print(custo_pedagio+gasto_km)
