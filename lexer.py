ESTADO_TRAMPA = "TRAMPA"

ESTADO_FINAL = "ACEPTADO"

ESTADO_NO_FINAL = "NO ACEPTADO"

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
    estados_finales = [1]

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
    if estado_actual in estados_finales:
            return ESTADO_FINAL
    else:
            return ESTADO_NO_FINAL


def automata_cte(cadena):
    simbolos = ["1","2","3","4","5","6","7","8","9","0"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        elif estado_actual == 1 and caracter in simbolos :
             estado_actual = 1

        else:
                estado_actual = -1
                break
                
    if estado_actual == -1:
            return ESTADO_TRAMPA
    if estado_actual in estados_finales:
            return ESTADO_FINAL
    else:
            return ESTADO_NO_FINAL


def automata_cerrar_parentesis(cadena):
    simbolos = [")"]

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
    else:
            return ESTADO_NO_FINAL

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
    else:
                return ESTADO_NO_FINAL

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
       else:
         return ESTADO_NO_FINAL

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
    if estado_actual in estados_finales:
                   return ESTADO_FINAL
    else:
                   return ESTADO_NO_FINAL

TOKENS_A = [ ("reservada_para", automata_para),("reservada_desde", automata_desde),("reservada_hasta", automata_hasta),("reservada_sino", automata_sino),("reservada_si", automata_si),("reservada_entonces", automata_entonces),("reservada_mostrar", automata_mostrar),("reservada_aceptar", automata_aceptar), ("numeros", automata_cte),("identificadores", automata_id), ("simbolos", automata_simbolos),("abrir_parentesis", automata_abrir_parentesis),("cerrar_parentesis", automata_cerrar_parentesis),("abrir_llaves", automata_abrir_llave),("cerrar_llaves", automata_cerrar_llave) ]

def lexer(cadena):

    global tokens_posibles_mas_caracter
    global var_aux_todos_trampa
    global inicio_lex  
    
    inicio_lex = 0
    tokens = []
    puntero_posicion = 0 
    cadena = cadena + " " # Con la sugerencia posterior, esto no sería necesario

    while puntero_posicion < len( cadena ) :
        inicio_lex = puntero_posicion
        while  puntero_posicion < len( cadena ) and not cadena[puntero_posicion].isspace() :
                puntero_posicion = puntero_posicion + 1

          
        tokens_posibles = []
        tokens_posibles_mas_caracter = []
        lexema = " "
        var_aux_todos_trampa = False

        if not var_aux_todos_trampa : # Esto una sugerencia es usarlo con un while, si lo hacen de este modo 
                                       # agregan en la condición "and puntero_posicion<len(cadena)+1":
            # PARA CONTROLAR EL CORRECTO PROCESAMIENTO DEL ULTIMO CARACTER 
            # COMO ANTES SE HACÍA CON EL ESPACIO, PERO SIN TENER QUE AGREGAR EL ESPACIO EXPLICÍTAMENTE Y CONTROLA 
            # QUE NO SE VAYA DE RANGO ANTE UN ERROR EN EL INTERIOR DEL CICLO
                var_aux_todos_trampa = True
                lexema = cadena[inicio_lex : puntero_posicion]
                tokens_posibles = tokens_posibles_mas_caracter   
                tokens_posibles_mas_caracter = []
        print (lexema)
        for( anyone_token, automata ) in TOKENS_A : # Si usan un while, esto estaria indentado dentro de ese while
        
                insertar_cadena = automata(lexema) 
                if insertar_cadena == ESTADO_FINAL : 
                        tokens_posibles.append( anyone_token )
                        var_aux_todos_trampa = False
                        break        
        
                if insertar_cadena == ESTADO_NO_FINAL :
                        var_aux_todos_trampa = False

        puntero_posicion = puntero_posicion + 1  # Si usan un while, esto estaria indentado dentro de ese while
                                                 # al nivel del for anterior

        if len( tokens_posibles ) == 0  : 
                print( " ERROR : TOKEN DESCONOCIDO " + lexema )

        #puntero_posicion  =puntero_posicion -1 
        # ESTA LINEA SE AGREGA PORQUE CUANDO SE BUSCA EL TOKEN CON UN CARACTER MAS, 										# EL INDICE SE QUEDA EN CON UN CARACTER EXTRA, Y SI LOS TOKENS EN EL CODIGO 									# FUENTE NO ESTAN SEPARADOS POR UN ESPACIO, EL LEXER RECONOCE BIEN EL TOKEN 									# PERO GUARDA MAL EL LEXEMA PORQUE EL AGREGA UN CARACTER EXTRA QUE EN
                        # REALIDAD CORRESPONDERÍA AL SIGUIENTE, QUE A SU VEZ COMIENZA CON UN 
                        # CARACTER MENOS. ES DECIR ESTO ES NECESARIO POR SI TENGO ALGO COMO 344aux
                        # QUE SON DOS TOKENS SEPARADOS SIN UN ESPACIO LO RECONOZCA COMO EL TOKEN 
                        # "CTE" Y LEXEMA 344 SEGUIDO DEL TOKEN "ID" Y LEXEMA aux. SIN ESTO 
                        # ERA NECESARIO EL ESPACIO "344 aux"
        anyone_token = tokens_posibles[0]
        token = ( anyone_token, lexema )
        # Con lo cambios, esto pasaría a 
        # token=(anyone_token, cadena[inicio_lex:puntero_posicion]) 
        # POR EL MOTIVO ANTERIOR, 
		# lexema CONTENÍA UN CARACTER DE MÁS, AHORA COMO A INDEX SE LE RESTÓ 1 GUARDA EL CORRECTO
        tokens.append( token )

    return tokens

print(lexer("aux= ¿"))
