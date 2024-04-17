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

print(configuracion['DIR_INIT'])