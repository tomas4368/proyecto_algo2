import math

class TF:
  def __init__(self, localPath):
    # Inicializa el diccionario
    self.localPath = localPath
    self.diccionario = {}

  def agregar_palabra(self, palabra, countElement, countElementRoot):
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      self.diccionario[palabra] = (countElement/countElementRoot)
    
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
      docIndex = []
      count = 0
      for docTRIE in documentsTRIE:
        # si existe la palabra
        if palabra in docTRIE.diccionario:
          docIndex.append(docTRIE.index)
          count += 1
      # add
      auxIDF = math.log(len(documentsTRIE)/count)
      if auxIDF > 0:
        self.diccionario[palabra] = {'IDF': auxIDF, 'docIndex': docIndex}
  
  def search(self, palabra):
    # Trasformar a minúscula
    palabra = palabra.lower()
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      return None
    #
    return self.diccionario[palabra]

class Trie:
  def __init__(self, localPath, index):
    self.localPath = localPath
    self.diccionario = {}
    self.index = index
    self.element = 0

  def agregar_palabra(self, palabra):
    # Trasformar a minúscula
    palabra = palabra.lower()
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