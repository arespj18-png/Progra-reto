#Crear un menu en el que te pida que quieres(ia modo cooperativo o ia para mejorar en juegos competitivos)
#crear una lista de juegos en los que tenemos disponible la ia y hacer al usuario que escriba uno de los juegos y si elige uno que no este en la lista que le de error y vuelva a pedir
#dar opcion a terminar el programa poniendo exit o alguna cosa asi para cuando quieras dejar de usarlo
#en el modo de juegos competitivos un submenu para elegir la dificultad del bot(facil,normal,dificil y dar opcion a aleatorio de entre esas tres)
#en el modo cooperativo no hay dificultades debido a que el programa va segun tu ritmo te analiza tal y entonces adecua le nivel, en cambio en competitivo como es para practicar eliges tu la dificultad que quieres

#Estoy creando una funcion aqui para despues en el m
# enu principal llamar a esta funcion y que se ejecute
def sub_menu_de_juegos_competitivos():
    while True:
        print("Juegos disponibles:")
        for juego in lista_juegos_disponibles_competitivo_string:
            print("-", juego)
        
        opcion_string = input("Elige un juego(o para salir escribe exit): ")

        if opcion_string == "exit":
            print("Saliendo")
            return "exit"

        elif opcion_string in lista_juegos_disponibles_competitivo_string:
            print("Juego seleccionado correctamente")
            resultado_string = sub_menu_dificultades_juegos_competitivos()
            if resultado_string == "exit":
                return "exit"
            break
        else:
            print("El juego intrducido no esta en la lista, intentalo de nuevo")


def sub_menu_de_juegos_cooperativos():
    while True:
        print("Juegos disponibles")
        for juego in lista_juegos_disponibles_cooperativos_string:
            print("-", juego)
        opcion_string = input("Elige un juego(exit para salir): ")

        if opcion_string == "exit":
            print("Cerrando programa")
            return "exit"

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
        
        if opcion_input == "exit":
            print("Cerrando programa...")
            return "exit"
            
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


lista_juegos_disponibles_competitivo_string = ["Valorant", "CS2", "Fortnite", "Rocket League"]
lista_juegos_disponibles_cooperativos_string = ["It takes two", "Helldivers 2", "Overcooked 2"] #F   altan juegos por añadir
#Importo la funcion creada en gestor_archivos.py y recogo la informacion necesaria al final llamo a la funcion para guardar la infor
from gestor_archivos import guardar_informacion

print("Formulario de registro")
nombre_string=input("Introduce tu nombre: ")
edad_int=int(input("Introduce tu edad: "))
objetivos_string=(input("Cuales son tus objetivos con nuestro servicio"))
guardar_informacion(nombre_string,edad_int,objetivos_string)

print("¡Hola!")

while True:
    print("Que tipo de IA quieres usar?")
    print("1. Ia para juegos cooperativos\n2. Ia para practicar en juegos competitivos\n0. Salir")
    
    opcion_input = input("Elige una opcion: ")
    
    if opcion_input == "exit" or opcion_input == "0":
        print("Adios")
        break

    elif opcion_input == "1":
        if sub_menu_de_juegos_cooperativos() == "exit":
            break

    elif opcion_input == "2":
        if sub_menu_de_juegos_competitivos() == "exit":
            break
    
    else:
        print("Opcion no valida, intentalo de nuevo")   