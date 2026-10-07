#Voy a hacer lo de pasar a txt en un archivo separado y luego lo ejecuto en el principal para que no hayan muchisimas lineas en el principal y no se entienda


def guardar_informacion(nombre_string,edad_int,objetivos_string):
    #El nombre del txt que se va a crear va a tener de nombre el nombre intrducido por el usuario.txt
    nombre_archivo_string=f"{nombre_string.strip()}.txt"
#Esta funcion de aqui lo que hace es abrir nombre archivo con el metodo"w" de write y lo de encoding utf 8 es para que si hay alguna tilde alguna ñ el archivo no se corrompa
    with open(nombre_archivo_string,"w",encoding="utf-8")as archivo:
        #archivo.write lo que hace es escribir lo que le pongas dentro de archivo
        archivo.write("INFORMACION DE USUARIO\n")
        archivo.write(f"Nombre:{nombre_string}\n")
        archivo.write(f"Edad:{edad_int}\n")
        archivo.write(f"Objetivos:{objetivos_string}\n")

    print(f"Archivo:{nombre_archivo_string} guardado correctamente")
