import math

idade_dias=int(input("Sua idade em dias:"))

anos=idade_dias/365
meses=(idade_dias%365)/30
dias=(idade_dias%365)%30

print("Anos:",round(anos))
print("Meses:",round(meses))
print("Dias:",round(dias))