

escala_original=input("Escala original (c, f, k, r): ")
temperatura_original=float(input("Temperatura original:"))
escala_destino=input("Escala de destino (c, f, k, r): ")

if escala_original=='c':
    if escala_destino=='f':
        temp_f=(temperatura_original*(9/5))+32
        print(temp_f)
    elif escala_destino=='k':    
        temp_k=(temperatura_original+273.15)
        print(temp_k)
    elif escala_destino=='r':   
        temp_r=((temperatura_original*(9/5))+491.67)
        print(temp_r)      
        
elif escala_original=='f':
    if escala_destino=='c':
        temp_c=((temperatura_original - 32)*(5/9))
        print(temp_c)
    elif escala_destino=='k':    
            temp_k=(((temperatura_original - 32)*(5/9))+273.15)
            print(temp_k)
    elif escala_destino=='r':   
            temp_r=(temperatura_original+ 459,67)
            print(temp_r)
        
elif escala_original=='k':
        if escala_destino=='c':
            temp_c=(temperatura_original - 273,15)
            print(temp_c)
        elif escala_destino=='f':    
            temp_f=(((temperatura_original- 273.15)*9/5)+32)
            print(temp_f)
        elif escala_destino=='r':   
            temp_r=(temperatura_original*1.8)
            print(temp_r)
        
elif escala_original=='r':
            if escala_destino=='c':
                temp_c= ((temperatura_original - 491.67) * 5/9)
                print(temp_c)
            elif escala_destino=='f':    
                temp_f=(temperatura_original - 459.67)
                print(temp_f)
            elif escala_destino=='k':   
                temp_r=(temperatura_original*5/9)
                print(temp_r)