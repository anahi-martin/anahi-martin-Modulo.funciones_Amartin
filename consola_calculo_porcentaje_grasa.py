import calculadora_indices as calc

while True:
    try:
   
        while True:
            peso= float(input("Ingrese peso(kg): "))
            if peso< 40 or peso> 300: 
                print("El peso debe ser 40kg y 300 kg")
            else:
                break

        while True:
            altura =float(input("Ingrese altura (m): "))
            if altura< 1.40 or altura> 3:
                print("La altura debe ser 1.40m y 3m")
            else:
                break  
        
        
        while True:
            edad= int(input("Ingrese edad: "))
            if edad <18 or edad >102:
                print("La edad debe estar entre 18 y 102 años")
            else:
                break

        while True:
            valor_genero =float(input("Ingrese valor de género (10.8 para hombre, 0 para mujer): "))
            if valor_genero not in [0,10.8]:
                print("El valor de género debe ser 10.8 (hombre) o 0 (mujer)")
            else:
                break

        imc = calc.calcular_IMC(peso, altura)
        porcentaje= calc.calcular_porcentaje_grasa(imc, edad, valor_genero)

    except ValueError:
        print("***Error: Ingresó un valor no numérico ***")
    else:
        if porcentaje < 0:
            print("*** Error: El resultado del porcentaje de grasa no puede ser negativo ***")
        else:
            print("-----------------------------> Tu porcentaje de grasa es    : ", round(porcentaje, 2), "%")
        break