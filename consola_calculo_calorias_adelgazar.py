import calculadora_indices as calc

while True:
    try:
      
        while True:
            peso= float(input("Ingrese peso (kg): "))
            if peso <40 or peso > 300: 
                print("El peso debe ser un valor entre 40 y 300 kg")
            else:
                break  
        
        while True:
            altura =float(input("Ingrese altura (cm): "))
            if altura<= 0: 
                print("La altura debe ser mayor a 0")
            else:
                break 

        while True:
            edad =int(input("Ingrese edad: "))
            if edad< 18 or edad >102:
                print("La edad debe estar entre 18 y 102 años")
            else:
                break

        while True:
            valor_genero= float(input("Ingrese valor de género (5 para hombre, -161 para mujer): "))
            if valor_genero not in [5,-161]:
                print("El valor de género debe ser 5 (hombre) o -161 (mujer)")
            else:
                break 

        tmb =calc.calcular_calorias_en_reposo(peso, altura,edad,valor_genero) 
       
        resultado = calc.consumo_calorias_recomendado_para_adelgazar(tmb)
 
        inferior = tmb*0.80
        superior = tmb* 0.85

        if inferior <0 or superior< 0:
            print("El rango ser negativo")
            continue 

    except ValueError:
        print("***Error: Ingresó un valor no numérico ***")
    else:
       
        print(f"Para adelgazar es recomendado que consumas entre: {inferior:.1f} y {superior:.2f} calorías al día. Siendo {inferior:.1f} el rango inferior y {superior:.2f} el rango superior")
        break
