import os

# Creamos el tablero:
tablero =[
    [' ','1','2','3','4','5','6','7','8'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' '],
    ['2',' ',' ',' ',' ',' ',' ',' ',' '],
    ['3',' ',' ',' ',' ',' ',' ',' ',' '],
    ['4',' ',' ',' ',' ',' ',' ',' ',' '],
    ['5',' ',' ',' ',' ',' ',' ',' ',' '],
    ['6',' ',' ',' ',' ',' ',' ',' ',' '],
    ['7',' ',' ',' ',' ',' ',' ',' ',' '],
    ['8',' ',' ',' ',' ',' ',' ',' ',' '],
]

# Representacion de las fichas blancas:
REY_BLANCO = chr(0x2654)
REINA_BLANCO = chr(0x2655)
TORRE_BLANCO = chr(0x2656)
ALFIL_BLANCO = chr(0x2657)
CABALLO_BLANCO = chr(0x2658)
PEÓN_BLANCO = chr(0x2659)

# Representacion de las fichas negras:
REY_NEGRO = chr(0x265A)
REINA_NEGRO = chr(0x265B)
TORRE_NEGRO = chr(0x265C)
ALFIL_NEGRO = chr(0x265D)
CABALLO_NEGRO = chr(0x265E)
PEÓN_NEGRO = chr(0x265F)

# Establecemos la posicion inicial de las fichas blancas y negras
(tablero[8])[5] = REY_BLANCO
(tablero[8])[4] = REINA_BLANCO
(tablero[8])[1] = TORRE_BLANCO
(tablero[8])[8] = TORRE_BLANCO
(tablero[8])[3] = ALFIL_BLANCO
(tablero[8])[6] = ALFIL_BLANCO
(tablero[8])[2] = CABALLO_BLANCO
(tablero[8])[7] = CABALLO_BLANCO
(tablero[7])[1] = PEÓN_BLANCO
(tablero[7])[2] = PEÓN_BLANCO
(tablero[7])[3] = PEÓN_BLANCO
(tablero[7])[4] = PEÓN_BLANCO
(tablero[7])[5] = PEÓN_BLANCO
(tablero[7])[6] = PEÓN_BLANCO
(tablero[7])[7] = PEÓN_BLANCO
(tablero[7])[8] = PEÓN_BLANCO
(tablero[1])[5] = REY_NEGRO
(tablero[1])[4] = REINA_NEGRO
(tablero[1])[1] = TORRE_NEGRO
(tablero[1])[8] = TORRE_NEGRO
(tablero[1])[3] = ALFIL_NEGRO
(tablero[1])[6] = ALFIL_NEGRO
(tablero[1])[2] = CABALLO_NEGRO
(tablero[1])[7] = CABALLO_NEGRO
(tablero[2])[1] = PEÓN_NEGRO
(tablero[2])[2] = PEÓN_NEGRO
(tablero[2])[3] = PEÓN_NEGRO
(tablero[2])[4] = PEÓN_NEGRO
(tablero[2])[5] = PEÓN_NEGRO
(tablero[2])[6] = PEÓN_NEGRO
(tablero[2])[7] = PEÓN_NEGRO
(tablero[2])[8] = PEÓN_NEGRO

def print_tablero(tablero):  # Creamos una funcion para printear el tablero
    for i in range(9):
        print(tablero[i])
        
print_tablero(tablero)  # Llamamos a la funcion para asi printear el tablero de ajedrez

def movimientos(tablero):   # Creamos la funcion movimientos
    while True:
        ficha = input("Elige la ficha que deseas mover seleccionando sus coordenadas por separado:")
        ficha = ficha.split()
        if len(ficha) == 2:
            filaI = ficha[0]
            columnaI = ficha[1]
            # De esta manera almacenamos la fila y la columna del movimiento por separado
            try:
                # Comprobamos que el dato introducido por el usuario es correcto
                # para ello han de ser numeros enteros
                filaI = int(filaI)
                columnaI = int(columnaI)  
            except:
                print("Elije unas coordenadas lógicas y posibles")
                pass
                # De esta manera se repite el bucle hasta que el usuario introduzca el movimiento correctamente
            else:
                # Cuando el valor de la fila y la columna es correcto, se cierra el bucle y continua el codigo
                if filaI > 0 and filaI < 9 and columnaI > 0 and columnaI < 9:
                    break 

    # Elaboramos un bucle que realizara el cambio de posicion            
    while True:
        recorrido = input("Elige las coordenadas a las que deseas mover tu ficha:")
        recorrido = recorrido.split()
        if len(recorrido) == 2:
            filaE = recorrido[0]
            columnaE = recorrido[1]
            try:   # Mismo bucle anterior para la comprobacion de los datos introducidos por el usuario
                filaE = int(filaE)
                columnaE = int(columnaE)
            except:
                print("Elije unas coordenadas lógicas y posibles")
                pass
            else:
                if 0 < filaE < 9 and 0 < columnaE < 9 and recorrido != ficha:
                    (tablero[filaE])[columnaE] = tablero[filaI][columnaI]
                    (tablero[filaI][columnaI]) = " "
                    break

# Creacion y apertura del fichero
fichero = input("Elige un nombre para el fichero: ")
f = open(fichero, "a+", encoding="utf-8")