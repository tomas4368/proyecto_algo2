class Search:
  def __init__(self):
    self.oration = {}

  def addWord(self, idf, listTF, palabra):
    # busca la palabra en idf
    searchDATA = idf.search(palabra)
    # verifica su existencia
    if searchDATA == None:
      return
    # 
    for id_doc in searchDATA['id_doc']:
      # verificar si existe la oracion
      if id_doc not in self.oration:
        # establece la ubicación del archivo
        localPath = listTF[id_doc].localPath
        # crear oracion con key id del documento
        self.oration[id_doc] = WordsTF_IDF(localPath, id_doc)
      # en las siguientes 3 lineas se agrega la palabra a la oracion
      idfWords = searchDATA['IDF'] # extrae IDF correspondiente          
      tfWords = listTF[id_doc].diccionario[palabra] # extrae TF correspondiente al documento        
      tf_idfWords = tfWords * idfWords # calcula la relación de TF con respecto al IDF 
      # agregamos la palabra a la oración
      self.oration[id_doc].add_words(tf_idfWords)
        

class WordsTF_IDF:
  def __init__(self, localPath, id_doc):
    self.localPath = localPath
    self.id_doc = id_doc
    self.tf_idf = []

  def add_words(self, tf_idf):
    self.tf_idf.append(tf_idf)
  
  def getTF_IDF_oration(self):
    tf_idf = 0
    for data in self.tf_idf:
      tf_idf += data
    return tf_idf