import os

def getFile(localPath):
  # lista de archivos
  files = []
  # obtener archivos
  try:
    files = os.listdir(localPath)
  # verificar en el sistema
  except OSError as e:
    # salir por error
    print(f"Error in path '{localPath}': {e}")
    exit(0)
  # verificar archivos
  files = _filterFile(files)
  # comprobar los archivos
  if len(files) == 0:
    # salir porque no hay pdf
    print(f"Error al listar el contenido de '{localPath}': No hay documentos *.pdf")
    exit(0)
  # extraemos el directorio completo
  files = _addLocalPatch(files, localPath)
  # devolvemos lista con los directorios de todos los pdf
  return files

def _addLocalPatch(files, localPath):
  files_con_ruta = [os.path.join(localPath, file) for file in files]
  return files_con_ruta

def _filterFile(files):
  # Filtrar los elementos que terminan en '.pdf'
  return [file for file in files if file.endswith('.pdf')]