import math
from function.clearSpecialCHAR import lista_sufijos, lista_stopwords

class TF:
  def __init__(self, localPath):
    # Inicializa el diccionario
    self.localPath = localPath
    self.diccionario = {}

  def agregar_palabra(self, palabra, countElement, countElementRoot):
    # Incrementa la frecuencia de la palabra
    self.diccionario[palabra] = (countElement/countElementRoot)

class IDF:
  def __init__(self):
    # Inicializa el diccionario
    self.diccionario = {}

  def agregar_palabra(self, palabra, documentsTRIE):
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      # buscar por documento
      id_doc = []
      # cuenta la cantidad de documentos en los que aparece la palabra
      count = 0
      for docTRIE in documentsTRIE:
        # si existe la palabra
        if palabra in docTRIE.diccionario:
          id_doc.append(docTRIE.id_doc)
          count += 1
      # add
      auxIDF = math.log(len(documentsTRIE)/count)
      self.diccionario[palabra] = {'IDF': auxIDF, 'id_doc': id_doc}
  
  def search(self, palabra):
    # Transformar a minúscula
    palabra = palabra.lower()
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      return None
    #
    return self.diccionario[palabra]

class Trie:
  def __init__(self, localPath, id_doc):
    self.localPath = localPath
    self.diccionario = {}
    self.id_doc = id_doc
    self.element = 0

  def agregar_palabra(self, palabra):
    # Transformar a minúscula
    palabra = palabra.lower()
    if lista_stopwords.get(palabra):
      return
    if len(palabra) - 3 >= 9:
        n = 9
    else:
      n = len(palabra) - 3
      if n < 0:
        n = 0
    for i in range(n, 0, -1):
      if lista_sufijos.get(palabra[-i:]):
        palabra = palabra[:-i]
        break
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      self.diccionario[palabra] = 0
    # Incrementa la frecuencia de la palabra
    self.diccionario[palabra] += 1
    # Incrementa elementos
    self.element += 1

class DATA:
  def __init__(self, idf, listTF):
    self.idf = idf
    self.listTF = listTF

