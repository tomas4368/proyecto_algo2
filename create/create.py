from create.path.path import getFile
from create.read.read import read
from create.save.save import seve
from create.tf_idf.index import tf_idf

def create(localPath):

  # extraer directorios
  files = getFile(localPath)

  # read devuelve lista de documentos
  listDocumentTrie = read(files)

  # calculamos el tf de cada documento y el idf general
  data = tf_idf(listDocumentTrie)
  # guardar

  seve(data)

  # una vez terminado escribe lo siguiente en la consola
  print('document data-base created successfully')