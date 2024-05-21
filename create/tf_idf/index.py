from create.struct import DATA, TF, IDF


def tf_idf(documentsTRIE):

  listTF = []
  idf = IDF()
  
  for docTRIE in documentsTRIE:
    # crear estructura
    documentTF = TF(docTRIE.localPath)
    # crear diccionario
    for palabra, count in docTRIE.diccionario.items():
      documentTF.agregar_palabra(palabra, count, docTRIE.element)
      idf.agregar_palabra(palabra, documentsTRIE)
    # agregar
    listTF.append(documentTF)
    count += 1

  return DATA(idf, listTF)
