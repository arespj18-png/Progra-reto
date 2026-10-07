# Documentación Proyecto Reto 1

## Por qué usamos distintos archivos
He separado el código en varios archivos (reto1.py, juegos.py, gestor_archivos.py) simplemente para tenerlo todo más ordenado y limpio.
- reto1.py: es el menú principal y donde arranca el programa.
- juegos.py: es donde guardo todos los textos de cada juego.
- gestor_archivos.py: se encarga de guardar los datos del registro.
Con el "import" llamo a las cosas de los otros archivos y así no me queda un solo archivo gigante y lioso.

## Qué es un "def"
Uso "def" para crear funciones. Básicamente empaqueto un trozo de código y le pongo un nombre. Ese código no hace nada hasta que yo lo llame en el programa. Me sirve para tener las cosas organizadas y no repetir código.

## Funciones en reto1.py
- mostrar_informacion_juego(nombre_juego): Esta función se encarga de mostrar la info del juego usando los def que creamos en juegos.py. Usa .lower() para que dé igual si el usuario escribe en mayúsculas o minúsculas.
- sub_menu_de_juegos_competitivos(): Crea un bucle infinito (while True) que muestra los juegos y pide elegir uno. Si pones 0, sale al menú anterior.
- sub_menu_de_juegos_cooperativos(): Hace lo mismo que la anterior pero usando la lista de los juegos cooperativos.
- sub_menu_dificultades_juegos_competitivos(): Después de elegir un juego competitivo, te manda aquí para elegir la dificultad del bot. Usa break para terminar una vez has elegido bien.

## Funciones en juegos.py
- info_valorant(), info_cs2(), etc: Son funciones básicas que solo tienen los print con el texto de cada juego. Esperan ahí hasta que el archivo principal las llama.

## Funciones en gestor_archivos.py
- guardar_informacion(nombre_string, edad_int, objetivos_string): Coge lo que el usuario ha escrito en el formulario del principio y lo guarda en los archivos de texto correspondientes para no perderlos.
