from create.path.path import getFile
from create.read.read import read
from create.save.save import seve

def create(localPath):
  # extraer directorios
  files = getFile(localPath)
  # read devuelve lista de documentos
  listDocument = read(files)
  # guardar
  seve(listDocument)
  #
  print('document data-base created successfully')