from create.struct import DATA, TF, IDF


def tf_idf(documentsTRIE):

  listTF = []
  idf = IDF()
  
  for docTRIE in documentsTRIE:
    # crear estructura
    documentTF = TF(docTRIE.localPath)
    # crear diccionario
    for palabra, count in docTRIE.diccionario.items():
      # agrega la palabra a la estructura TF
      documentTF.agregar_palabra(palabra, count, docTRIE.element)
      # agrega la palabra al IDF
      idf.agregar_palabra(palabra, documentsTRIE)
    # agregar
    listTF.append(documentTF)

  return DATA(idf, listTF)
