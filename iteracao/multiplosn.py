multiplos_n=int(input())
fim_sequencia_m=int(input())

for i in range(1,fim_sequencia_m+1):
    multiplo=multiplos_n*i
    if multiplo<=fim_sequencia_m:
        print(multiplo , end=' ')