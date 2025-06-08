import calculadora_indices as calc

while True:
    try:
        
        while True:
            peso= float(input("Ingrese peso (kg): "))
            if peso <40 or peso > 300:
                print("El peso debe ser 40kg y 300 kg")
            else:
                break 
        
        while True:
            altura =float(input("Ingrese altura (cm): "))
            if altura<= 0:  # para que concuerde con prueba ejemplo
                print("La altura debe ser mayor a 0")
            else:
                break

       
        while True:
            edad =int(input("Ingrese edad: "))
            if edad< 18 or edad > 102:
                print("La edad debe estar entre 18 y 102 años")
            else:
                break

        while True:
            valor_genero=float(input("Ingrese valor de género (5 para hombre, -161 para mujer): "))
            if valor_genero not in [5,-161]:
                print("El valor de género debe ser 5 (hombre) o -161 (mujer)")
            else:
                break 
        
        while True:
            valor_actividad =float(input("Ingrese valor de actividad física (1.2, 1.375,1.55, 1.725,1.9): "))
            if valor_actividad not in [1.2, 1.375,1.55, 1.725,1.9]:  # en descrip 1.72 / en prueba ejemplo 1.725
                print("Valor de actividad inválido")
            else:
                break

   
        tmb = calc.calcular_calorias_en_reposo(peso, altura,edad, valor_genero)
        calorias_a= calc.calcular_calorias_en_actividad(tmb,valor_actividad)

    except ValueError:
        print("***Error: Ingresó un valor no numérico ***")
    else:
        print("-----------------------------> Gasto en actividad:", round(calorias_a, 2), "cal.")
        break