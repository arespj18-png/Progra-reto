#Crear un menu en el que te pida que quieres(ia modo cooperativo o ia para mejorar en juegos competitivos)
#crear una lista de juegos en los que tenemos disponible la ia y hacer al usuario que escriba uno de los juegos y si elige uno que no este en la lista que le de error y vuelva a pedir
#dar opcion a terminar el programa poniendo exit o alguna cosa asi para cuando quieras dejar de usarlo
#en el modo de juegos competitivos un submenu para elegir la dificultad del bot(facil,normal,dificil y dar opcion a aleatorio de entre esas tres)
#en el modo cooperativo no hay dificultades debido a que el programa va segun tu ritmo te analiza tal y entonces adecua le nivel, en cambio en competitivo como es para practicar eliges tu la dificultad que quieres

#Estoy creando una funcion aqui para despues en el m
# enu principal llamar a esta funcion y que se ejecute
def sub_menu_de_juegos_competitivos():
    while True:
        opcion_int=input("Elige un juego")
        if opcion_int==1:
            sub_menu_dificultades_juegos_competitivos()
def sub_menu_de_juegos_cooperativos():
    while True:
        opcion_int=input("Elige un juego")
        if opcion_int==1:
            print("Listo para jugar!")



#Despues del submenu anterior creo otro que sea para elegir la dificultad de la ia 


def sub_menu_dificultades_juegos_competitivos():
    while True:
        opcion_int=input("Elige la dificultad del bot/ia")
        print("Opciones:\n1. Dificultad Facil\n2. Dificultad Intermedia\n3. Dificultad Dificil\n4.Salir al menu anterior")
        if opcion_int==1:
            print("Dificultad facil")
            print("Programa en ejecucion")
            
        elif opcion_int==2:
            print("Dificultad intermedia")
            print("Programa en ejecucion")

        elif opcion_int==3:
            print("Dificultad dificil")
            print("Programa en ejecucion")
        
        elif opcion_int==4:
            print("Saliendo al menu anterior")
            break
        else:
            print("Opcion no valida intentalo de nuevo")


lista_juegos_disponibles_competitivo_string=["1.Valorant","2.CS2","3.Fortnite","4.Rocket League"]
lista_juegos_disponibles_cooperativos_string=["It takes two","Mas juegos"] #F   altan juegos por añadir
print("¡Hola!")
print("Que tipo de IA quieres usar?")
print("1. Ia para juegos cooperativos\n2. Ia para practicar en juegos competitivos")
opcion_int=int(input("Elige una opcion"))

while True:
    if opcion_int==1:
        sub_menu_de_juegos_competitivos()

    elif opcion_int==2:
        sub_menu_de_juegos_cooperativos()
    elif opcion_int==0:
        print("Adios")
        break
    
    else:
        print("Opcion no valida, intentalo de nuevo")






        


        
    

        
            




