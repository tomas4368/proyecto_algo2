import os

def getFile(localPatch):
  # lista de archivos
  files = []
  # obtener archivos
  try:
    files = os.listdir(localPatch)
  # verificar en el sistema
  except OSError as e:
    # salir por error
    print(f"Error in path '{localPatch}': {e}")
    exit(0)
  # verificar archivos
  files = _filterFile(files)
  # comprobar los archivos
  if len(files) == 0:
    # salir porque no hay pdf
    print(f"Error al listar el contenido de '{localPatch}': No hay documentos *.pdf")
    exit(0)
  # default
  return files

def _filterFile(files):
  # Filtrar los elementos que terminan en '.pdf'
  return [file for file in files if file.endswith('.pdf')]