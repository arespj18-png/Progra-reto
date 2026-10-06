#Crear un menu en el que te pida que quieres(ia modo cooperativo o ia para mejorar en juegos competitivos)
#crear una lista de juegos en los que tenemos disponible la ia y hacer al usuario que escriba uno de los juegos y si elige uno que no este en la lista que le de error y vuelva a pedir
#dar opcion a terminar el programa poniendo exit o alguna cosa asi para cuando quieras dejar de usarlo
#en el modo de juegos competitivos un submenu para elegir la dificultad del bot(facil,normal,dificil y dar opcion a aleatorio de entre esas tres)
#en el modo cooperativo no hay dificultades debido a que el programa va segun tu ritmo te analiza tal y entonces adecua le nivel, en cambio en competitivo como es para practicar eliges tu la dificultad que quieres

import juegos

#Esta funcion se encarga de mostrar la info del juego usando los def que creamos en juegos.py
def mostrar_informacion_juego(nombre_juego):
    #Uso .lower() para pasar lo que escriba el usuario a minusculas y asi si pone "VaLoRanT" el programa lo entienda igual
    nombre = nombre_juego.lower()
    if nombre == "valorant":
        juegos.info_valorant()
    elif nombre == "cs2":
        juegos.info_cs2()
    elif nombre == "fortnite":
        juegos.info_fortnite()
    elif nombre == "rocket league":
        juegos.info_rocket_league()
    elif nombre == "it takes two":
        juegos.info_it_takes_two()
    elif nombre == "helldivers 2":
        juegos.info_helldivers_2()
    elif nombre == "overcooked 2":
        juegos.info_overcooked_2()
    else:
        print("Información no disponible para este juego.")

#Estoy creando una funcion aqui para despues en el m
# enu principal llamar a esta funcion y que se ejecute
def sub_menu_de_juegos_competitivos():
    #Uso while True para crear un bucle infinito que no parara de repetirse hasta que se ejecute un break o return
    while True:
        print("Juegos disponibles:")
        for juego in lista_juegos_disponibles_competitivo_string:
            print("-", juego)
        
        opcion_string = input("Elige un juego(0 para salir): ")

        if opcion_string == "0":
            print("Saliendo")
            return "0"

        #Compruebo si el juego que ha escrito esta dentro de la lista de juegos que tenemos usando "in"
        elif opcion_string in lista_juegos_disponibles_competitivo_string:
            print("Juego seleccionado correctamente")
            resultado_string = sub_menu_dificultades_juegos_competitivos()
            #Si al elegir dificultad decide pulsar 0, uso continue para volver al inicio de este bucle y pedir de nuevo un juego
            if resultado_string == "0":
                continue
            #Si no pulso 0 y eligio bien, el break sirve para salir de este bucle infinito y continuar con el menu principal
            break
        else:
            print("El juego intrducido no esta en la lista, intentalo de nuevo")


def sub_menu_de_juegos_cooperativos():
    while True:
        print("Juegos disponibles")
        for juego in lista_juegos_disponibles_cooperativos_string:
            print("-", juego)
        opcion_string = input("Elige un juego(0 para salir): ")

        if opcion_string == "0":
            print("Cerrando programa")
            return "0"

        elif opcion_string in lista_juegos_disponibles_cooperativos_string:
            print(" Listo para jugar")
            break
        else:
            print("Opcion no valida, intentalo de nuevo")


#Despues del submenu anterior creo otro que sea para elegir la dificultad de la ia 

def sub_menu_dificultades_juegos_competitivos():
    while True:
        print("Opciones:\n1. Dificultad Facil\n2. Dificultad Intermedia\n3. Dificultad Dificil\n4. Salir al menu anterior")
        opcion_input = input("Elige la dificultad del bot/ia: ")
        
        if opcion_input == "0":
            print("Cerrando programa...")
            return "0"
            
        elif opcion_input == "1":
            print("Dificultad facil")
            print("Programa en ejecucion")
            break
            
        elif opcion_input == "2":
            print("Dificultad intermedia")
            print("Programa en ejecucion")
            break

        elif opcion_input == "3":
            print("Dificultad dificil")
            print("Programa en ejecucion")
            break
        
        elif opcion_input == "4":
            print("Saliendo al menu anterior")
            break
        else:
            print("Opcion no valida intentalo de nuevo")


#Creo unas listas con los nombres de los juegos usando corchetes, asi si luego quiero añadir mas juegos solo los escribo aqui
lista_juegos_disponibles_competitivo_string = ["Valorant", "CS2", "Fortnite", "Rocket League"]
lista_juegos_disponibles_cooperativos_string = ["It takes two", "Helldivers 2", "Overcooked 2"] #F   altan juegos por añadir
#Importo la funcion creada en gestor_archivos.py y recogo la informacion necesaria al final llamo a la funcion para guardar la infor
from gestor_archivos import guardar_informacion

#Aqui preguntamos si el usuario ya esta registrado para pedirle la contraseña o mandarlo al formulario de registro
tiene_cuenta_string = input("¿Tienes cuenta? (si/no): ")
if  tiene_cuenta_string == "si":
    contraseña_str = input("Introduce la contraseña \n")
    if contraseña_str == "1234":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
        #El exit() sirve para forzar al programa a cerrarse por completo inmediatamente si se equivoca de contraseña
        exit()
else:
    print("Formulario de registro")
    nombre_string=input("Introduce tu nombre: ")
    edad_int=int(input("Introduce tu edad: "))
    objetivos_string=(input("Cuales son tus objetivos con nuestro servicio: "))
    guardar_informacion(nombre_string,edad_int,objetivos_string)

print("¡Hola!")

while True:
    print("Que tipo de IA quieres usar?")
    print("1. Ia para juegos cooperativos\n2. Ia para practicar en juegos competitivos\n3. Mostrar informacion de juegos\n0. Salir")
    
    opcion_input = input("Elige una opcion: ")
    
    if opcion_input == "0":
        print("Adios")
        break

    elif opcion_input == "1":
        sub_menu_de_juegos_cooperativos()

    elif opcion_input == "2":
        sub_menu_de_juegos_competitivos()
            
    elif opcion_input == "3":
        nombre = input("Introduce el nombre del juego para ver su informacion: ")
        mostrar_informacion_juego(nombre)
    
    else:
        print("Opcion no valida, intentalo de nuevo")   