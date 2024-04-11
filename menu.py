import argparse

def veure_config():
    with open('config.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())


configuracion = {
    "DIR_INIT": "ggm_init",
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
        print("'archivo'", ':', valor)
    else:
        print('La clave', archivo, 'no existe en la configuración.')

    guardar_config()


def guardar_config():
    global configuracion
    with open('config.txt', 'w') as f:
        f.write(str(configuracion))


def cambiar_contraseña():
    print('Función para cambiar la contraseña')

def menu_configuración():
    while True:
        print('\n\tMENU configuración')
        print('1. veure_config')
        print('2. Carregar config')
        print('3. Canviar paràmetres')
        print('4. Desar config')
        print('5. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            veure_config()
        elif opcion == 2:
            Carregar_config()
        elif opcion == 3:
            break
        else:
            print('Opción no válida. Por favor, elige una opción válida.')

while True:
    print('\n\tMENU PRINCIPAL: \n')
    print('1. Configuración')
    print('2. creacio de directoris')
    print('3. classificacio arxius')
    print('4. filtratge')
    print('5. canvis de propietari i de permisos')
    print('6. comprovació')
    print('7. compressió')
    print('8. creació d’informe')
    print('0. Salir')
    opcion = -1
    while opcion not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        opcion = int(input('Opción: '))
    if opcion == 1:
        menu_configuración()
    else:
        break
