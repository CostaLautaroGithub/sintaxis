TOKENS = [ ("reservada_para", automata_para),("reservada_desde", automata_desde),("reservada_hasta", automata_hasta),("reservada_sino", automata_sino),
("reservada_si", automata_si),("reservada_entonces", automata_entonces), ("reservada_mostrar", automata_mostrar),("reservada_aceptar", automata_aceptar).
("identificadores", automata_id), ("llaves", automata_llaves), ("simbolos", automata_simbolos),
("abrir_parentesis", automata_abrir_parentesis),("cerrar_parentesis", automata_cerrar_parentesis),
("abrir_llaves", automata_abrir_llave),("cerrar_llaves", automata_cerrar_llave)]

def automata_para(cadena):

    estado_actual = 0
    estados_finales = [ 4 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "p":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "r" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "a" :
                estado_actual = 4

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_desde(cadena):

    estado_actual = 0
    estados_finales = [ 5 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "d":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "e" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "d" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "e" :
                estado_actual = 5

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_hasta(cadena):

    estado_actual = 0
    estados_finales = [ 5 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "h":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "t" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "a" :
                estado_actual = 5

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_sino(cadena):

    estado_actual = 0
    estados_finales = [ 4 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "n" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "o" :
                estado_actual = 4

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_si(cadena):

    estado_actual = 0
    estados_finales = [ 2 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i" :
                estado_actual = 2


        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_entonces(cadena):

    estado_actual = 0
    estados_finales = [ 8 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "n" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "t" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "o" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "n" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "c" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "e" :
                estado_actual = 7
        elif estado_actual == 7 and caracter == "s" :
                estado_actual = 8

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_mostrar(cadena):

    estado_actual = 0
    estados_finales = [ 7 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "m":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "o" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "t" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "r" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "a" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "r" :
                estado_actual = 7

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_aceptar(cadena):

    estado_actual = 0
    estados_finales = [ 7 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "a":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "c" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "e" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "p" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "t" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "a" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "r" :
                estado_actual = 7

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL



def automata_id(cadena):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    numeros = [ "0","1","2","3","4","5","6","7","8","9" ]

    estado_actual = 0
    estados_finales = [ 1 ]



        for caracter in cadena:
            if estado_actual == 0 and caracter in letras:
                estado_actual = 1
            elif estado_actual == 1 and caracter in letras or numeros :
                estado_actual = 1
            else:
                estado_actual == -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL


def automata_abrir_parentesis(cadena):
    simbolos = ["("]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
                estado_actual = -1
                break
                
if estado_actual == -1:
    return ESTADO_TRAMPA

else estado_actual in estados_finales:
    return ESTADO_FINAL





def automata_cerrar_parentesis(cadena):
    simbolos = ["("]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
                estado_actual = -1
                break
                
if estado_actual == -1:
    return ESTADO_TRAMPA

else estado_actual in estados_finales:
    return ESTADO_FINAL  

def automata_abrir_llave(cadena):
    simbolos = ["{"]
estado_actual = 0
estados_finales = [1]

for caracter in cadena:
    if estado_actual == 0 and caracter in simbolos:
        estado_actual = 1
    else:
            estado_actual = -1
            break
if estado_actual == -1:
    return ESTADO_TRAMPA
if estado_actual in estados_finales:
    return ESTADO_FINAL

def automata_cerrar_llave(cadena):
    simbolos = ["}"]
estado_actual = 0
estados_finales = [1]

for caracter in cadena:
    if estado_actual == 0 and caracter in simbolos:
        estado_actual = 1
    else:
            estado_actual = -1
            break
if estado_actual == -1:
    return ESTADO_TRAMPA
if estado_actual in estados_finales:
    return ESTADO_FINAL

def automata_simbolos(cadena):
    simbolos = ["*","+","=",";"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
                estado_actual = -1
                break

if estado_actual == -1:
    return ESTADO_TRAMPA
else estado_actual in estados_finales:
    return ESTADO_FINAL

_________________________________________________________________________________________________

def lexer( string ) :

tokens = []
puntero_posicion = 0 

while puntero_posicion < len( string ) : 
    while string[ puntero_posicion ].isspace() :
        puntero_posicion = puntero_posicion + 1

     inicio_lex = puntero_posicion   
     tokens_posibles = []
     tokens_posibles_mas_caracter = []
     lexema = **
     var_aux_todos_trampa = False

     while not var_aux_todos_trampa :
         var_aux_todos_trampa = True
         lexema = string[inicio_lex : puntero_posicion + 1 ]
         tokens_posibles = tokens_posibles_mas_caracter
         tokens_posibles_mas_caracter = []

         for( anyone_token, automata ) in TOKENS :
             insertar_cadena = afd(lexema) 
            if insertar_cadena == ESTADO_FINAL : 
                tokens_posibles_mas_caracter.append( anyone_token )
                var_aux_todos_trampa = False
                elif insertar_cadena == ESTADO_NO_FINAL :
                    var_aux_todos_trampa = False

                    puntero_posicion = puntero_posicion + 1

                    if len( tokens_posibles ) == 0  : 
                        print( " ERROR : TOKEN DESCONOCIDO " + lexema )

                    anyone_token = tokens_posibles(0)

                    token = ( anyone_token, lexema )
                    tokens.append( token )

                    return tokens

                    
                     
                    
hola mundo ! 



