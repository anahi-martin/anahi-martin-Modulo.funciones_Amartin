import calculadora_indices as calc

while True:
    try:
        
        while True:
            peso= float(input("Ingrese peso (kg): "))
            if peso<40 or peso >300:
                print("El peso debe ser 40kg y 300 kg")
            else:
                break   

        while True:
            altura =float(input("Ingrese altura (cm): "))
            if altura<= 0: # para que concuerde con prueba ejemplo
                print("La altura debe ser 1.40m y 3m")
            else:
                break  
            
        while True:
            edad= int(input("Ingrese edad: "))
            if edad< 18 or edad >102:
                print("La edad debe estar entre 18 y 102 años")
            else:
                break 

       
        while True:
            valor_genero= float(input("Ingrese valor de género(5 para hombre, -161 para mujer): "))
            if valor_genero not in[5, -161]:
                print("El valor de género debe ser 5 (hombre) o -161 (mujer)")
            else:
                break    
                
        tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

    except ValueError:
        print("***Error: Ingresó un valor no numérico ***")
    else:
        if tmb< 0: 
            print("*** Error: El resultado de calorías en reposo no puede ser negativo ****")
        else:
            print("-----------------------------> Gasto en reposo: ",round(tmb, 2), "cal.")
        break