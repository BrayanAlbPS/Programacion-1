def nombre_mes(m):
    if m == 1:
        return "ENERO"
    elif m == 2:
        return "FEBRERO"
    elif m == 3:
        return "MARZO"
    elif m == 4:
        return "ABRIL"
    elif m == 5:
        return "MAYO"
    elif m == 6:
        return "JUNIO"
    elif m == 7:
        return "JULIO"
    elif m == 8:
        return "AGOSTO"
    elif m == 9:
        return "SEPTIEMRE"
    elif m == 10:
        return "OCTUBRE"
    elif m == 11:
        return "NOVIEMBRE"
    elif m == 12:
        return "DICIEMBRE"

def bisiesto(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0: 
        return True
    else:
        return False

def dias_mes(mes, año):
    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            if bisiesto(año):
                return 29
            else:
                return 28
            
def calcular_dia_semana(dia, mes, año):
    a = (14 - mes) // 12
    b = año - a
    c = mes + 12 * a - 2
    indicador = dia + b + b // 4 - b // 100 + b // 400 + (31 * c) // 12
    residuo = indicador % 7
    
    dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
    return dias[residuo]

while True:
    try:
        año = int(input("Escribe un año que sea mayor que 1582:"))
        if año > 1582:
            break
        print("El año debe ser mayor a 1582")
    except ValueError:
        print("Debes escribir un numero entero")

while True:
    try:
        mes = int(input("Escribe un mes entre [1-12]:"))
        if 1 <= mes <= 12:
            break
        else:
            print("Debes escribir un numero entero entre [1-12]")
    except ValueError:
        print("Debes escribir un numero entero")

numDias = dias_mes(mes, año)
nombreMes = nombre_mes(mes)

while True:
    try:
        dia = int(input(f"Escribe un día entre [1-{numDias}]:"))
        if 1 <= dia <= numDias:
            break
        else:
            print(f"Debes escribir un día válido entre [1-{numDias}]")
    except ValueError:
        print("Debes escribir un número entero")
diaSemana=calcular_dia_semana(dia, mes, año)
print(f"El mes de {nombreMes} del año {año} tiene {numDias} dias")
print(f"La fecha [{dia}|{mes}|{año}] caera o ya cayo un dia {diaSemana}")