def listaLineas():
    fichero = input("Introduce el nombre del fichero o exit para salir: ")
    if(fichero != "exit"):
        palabra=input("Introduce una palabra o exit para salir: ")
        while(palabra!="exit"):
            for linea in open(fichero):
                compararLineaYPalabra(linea,palabra)
            palabra=input("Introduce una palabra o exit para salir: ")
 

def compararLineaYPalabra(linea, palabra):
    datos = []
    datos.extend(linea.split())
    for i in range(len(datos)):
        if(datos[i]==palabra):
            print (linea)

listaLineas()
