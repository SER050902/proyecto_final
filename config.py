import os


path = os.path.basename('/home/x6474242h/PycharmProjects/proyecto_final/config.txt')
ggm_init = os.getcwd()
path1 = os.path.dirname('/home/x6474242h/PycharmProjects/proyecto_final/prueba.txt')
configuracion = {
    "DIR_INIT": f'{path}',
    "DIR_DST": '',
    "MIDA_PETITA": '',
    "MIDA_MITJANA": '',
    "EXTENSIO_FILTRADA": ["bin", "pdf", "exe"],
    "DIR_QUARANTENA": "quarantena",
    "ZIP_FILE": "output.zip",
    "REPORT_FILE": "report.inf"
}


def Carregar_config():
    global configuracion
    archivo = input('Introduce el nombre del archivo: ')
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
            if archivo.endswith('.txt'):
                print('Contenido del archivo', archivo, ':')
            else:
                print('No se puede abrir el archivo',archivo)
            print(contenido)
    except FileNotFoundError:
        print('El archivo', archivo, 'no existe.')




def veure_config():
    with open('config.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())

def guardar_config():
    global configuracion
    with open('config.txt', 'w') as f:
        f.write(str(configuracion))

def cambiar_parametros():
    print('LA INFORMACION DE',path)
    veure_config()
    clave = input("Quin paràmetre vols canviar? (Escriu el nom del paràmetre): ")
    if clave in configuracion:
        print("El valor actual de", clave, "és:", configuracion[clave])
        nou_valor = input("Introdueix el nou valor per a " + clave + ": ")

        if nou_valor:
            configuracion[clave] = nou_valor
            print("El valor de", clave, "s'ha canviat a:", configuracion[clave])
            guardar_config()
            veure_config()
            print("Cambiado correctamente")
    else:
        print("La clau", clave, "no existeix a la configuració.")



def mostrar_configuraciones():
    global configuracion
    print("Valors actuals de la configuració:")
    for clave, valor in configuracion.items():
        print(clave, "=", valor)

cambiar_parametros()