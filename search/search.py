from search.getDB import getDB
from search.getList import getList
from search.struct import Search

def search(text):
  #
  listTEXT = getList(text)
  #
  dataDB = getDB()
  #
  search = Search()
  #
  for text in listTEXT:
    #
    search.addWord(dataDB.idf, dataDB.listTF, text)
  #
  result = {}
  for valor in search.oration.values():
    getTF_IDF = valor.getTF_IDF_oration()
    if getTF_IDF > 0:
      result[getTF_IDF] = valor.localPath
  
  
  # Ordenar por claves numéricas en orden descendente
  ordenadoResultado = {k: result[k] for k in sorted(result, reverse=True)}

  # Mostrar el diccionario ordenado por claves numéricas en orden descendente
  count = 1
  for valor in ordenadoResultado.values():
    print(f'{count}: {valor}')
    count += 1
