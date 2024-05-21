class Search:
  def __init__(self):
    self.oration = {}

  def addWord(self, idf, listTF, palabra):
    #
    searchDATA = idf.search(palabra)
    #
    if searchDATA == None:
      return
    #
    for index in searchDATA['docIndex']:
      # Si la palabra no está en el prayer, la agrega con la información de la words
      if index not in self.oration:
        #
        localPath = listTF[index].localPath
        #
        self.oration[index] = WordsTF_IDF(localPath, index)
      #
      idfWords = searchDATA['IDF']
      tfWords = listTF[index].diccionario[palabra]
      tf_idfWords = tfWords * idfWords
      #
      self.oration[index].add_words(tf_idfWords)
        

class WordsTF_IDF:
  def __init__(self, localPath, index):
    self.localPath = localPath
    self.index = index
    self.tf_idf = []

  def add_words(self, tf_idf):
    self.tf_idf.append(tf_idf)

  def getTF_IDF_oration(self):
    tf_idf = 0
    for data in self.tf_idf:
      tf_idf += data
    return tf_idf