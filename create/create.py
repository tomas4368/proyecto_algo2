from math import erf
import os

def create(local_path):
  # check local path
  if not checkLocalPath(local_path):
    exit



def checkLocalPath(local_path):
  #
  contenido = []
  # obtener archivos
  try:
    contenido = os.listdir(local_path)
  except OSError as e:
    print(f"Error al listar el contenido de '{local_path}': {e}")
    return False
  # verificar si hay archivos
  if len(contenido) == 0:
    print(f"Error al listar el contenido de '{local_path}': No hay documentos")
    return False
  return True
  