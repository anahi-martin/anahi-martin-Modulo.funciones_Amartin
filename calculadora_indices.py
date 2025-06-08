# Parametros para adultos

def calcular_IMC(peso:float,altura:float)-> float:
    return peso/altura**2

def calcular_porcentaje_grasa(imc: float,edad:int,valor_genero:float)->float:
    return 1.2*imc +0.23 *edad- 5.4 -valor_genero

def calcular_calorias_en_reposo(peso:float,altura:float,edad:int,valor_genero:int) ->float:
    return 10 *peso + 6.25*altura - 5*edad+ valor_genero

def calcular_calorias_en_actividad(tmb:float,valor_actividad:float)->float:
    return tmb* valor_actividad

def consumo_calorias_recomendado_para_adelgazar(tmb:float) ->str:
    rango_inferior= tmb* 0.80
    rango_superior=tmb *0.85
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior:.2f}y {rango_superior:.2f} calorías al día    Siendo {rango_inferior:.2f} el rango inferior y {rango_superior:.2f} el rango superior"
