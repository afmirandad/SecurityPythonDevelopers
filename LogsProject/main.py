import os
from FileProcessor import *
from AttackDetector import *

def listar_archivos(carpeta):
    if not os.path.isdir(carpeta):
        print(f"La carpeta {carpeta} no existe.")
        return
    
    archivos = os.listdir(carpeta)

    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(carpeta, archivo))]
    
    if archivos:
        print("Archivos encontrados:")
        for archivo in archivos:
            print(archivo)
    else:
        print("No se encontraron archivos en la carpeta.")

def principal():
    carpeta = "LogsProject/logsEvidences"
    listar_archivos(carpeta)

if __name__ == "__main__":
    principal()
    a = FileProcessor("LogsProject/logsEvidences/access_log")
    a.openFilesAndGenerators()
    a.regexExtractorDataFunction()
