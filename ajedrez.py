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