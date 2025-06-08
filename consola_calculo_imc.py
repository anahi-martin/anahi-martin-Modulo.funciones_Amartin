import calculadora_indices as calc

while True:
    try:
      
        while True:
            peso =float(input("Ingrese peso (kg): "))
            if peso< 40 or peso>300:
                print("El peso debe ser 40kg y 300 kg")
            else:
                break
            
        while True:
            altura =float(input("Ingrese altura (m): "))
            if altura<1.40 or altura> 3:
                print("La altura debe ser 1.40m y 3m")
            else:
                break        
     
        imc = calc.calcular_IMC(peso, altura)

    except ZeroDivisionError:
        print("*** Error:División por cero. La altura no puede ser cero ***")
        continue
    except ValueError:
        print("*** Error:Ingresó un valor no numérico ***")
        continue
    else:
        if imc< 0:
            print("*** Error: El IMC no puede ser negativo ***")
            continue
        else:
            print("-----------------------------> El IMC es:", round(imc, 2))
            break
