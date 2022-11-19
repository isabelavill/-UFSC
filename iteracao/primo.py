import math

n = int(input())

if n == 1:
    eh_primo = False
elif n != 2 and n % 2 == 0:
    eh_primo = False
else:
    eh_primo = True
    raiz = int(math.sqrt(n))
    for i in range(3, raiz+1, 2):
        if n % i == 0:
            eh_primo = False
            break
    
print(eh_primo)