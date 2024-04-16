import os


path = os.path.basename('/home/x6474242h/PycharmProjects/proyecto_final/config.txt')
ggm_init = os.getcwd()

configuracion = {
    "DIR_INIT": f'{path}',
    "DIR_DST": "ggm_classificat",
    "MIDA_PETITA": 10,
    "MIDA_MITJANA": 17,
    "EXTENSIO_FILTRADA": ["bin", "pdf", "exe"],
    "DIR_QUARANTENA": "quarantena",
    "ZIP_FILE": "output.zip",
    "REPORT_FILE": "report.inf"
}


def Carregar_config():
    global configuracion
    archivo = input('Introduce el nombre del archivo: ')
    if archivo in configuracion:
        valor = configuracion[archivo]
        print('El archivo', valor, 'existe y sus valores son:')
        print(archivo, '=', valor)
    else:
        print('La clave', archivo, 'no existe en la configuración.')

    guardar_config()


def guardar_config():
    global configuracion
    with open('config.txt', 'w') as f:
        f.write(str(configuracion))

def cambiar_parametros():
    mostrar_configuraciones()

    clave = input("Quin paràmetre vols canviar? (Escriu el nom del paràmetre): ")
    if clave in configuracion:
        print("El valor actual de", clave, "és:", configuracion[clave])
        nou_valor = input("Introdueix el nou valor per a " + clave + ": ")

        if nou_valor:
            configuracion[clave] = nou_valor
            print("El valor de", clave, "s'ha canviat a:", configuracion[clave])
            mostrar_configuraciones()
            print("Cambiado correctamente")
    else:
        print("La clau", clave, "no existeix a la configuració.")



def mostrar_configuraciones():
    global configuracion
    print("Valors actuals de la configuració:")
    for clave, valor in configuracion.items():
        print(clave, "=", valor)

mostrar_configuraciones()