from search.getDB import getDB
from search.getList import getList
from search.print import printResult
from search.struct import Search

def search(text):
  # separar en palabra el texto
  listTEXT = getList(text)
  # extraer db
  dataDB = getDB()
  # crear estructura
  search = Search()
  # buscar coincidencias
  for text in listTEXT:
    search.addWord(dataDB.idf, dataDB.listTF, text)
  # extraer resultados
  result = {}
  for valor in search.oration.values():
    getTF_IDF = valor.getTF_IDF_oration()
    result[getTF_IDF] = valor.localPath
  # imprimir en consola
  printResult(result)