import PyPDF2
from create.struct import Trie
from function.clearSpecialCHAR import clearSpecialCHAR

def read(files):
  # creamos una lista de documentos
  listDocument = []
  id_doc = 0 # id_docentifica cada documento
  # extraemos la información de cada documento
  for file in files:
    listDocument.append(getData(file, id_doc))
    id_doc += 1;
  # devolvemos una lista con la información de cada documento
  return listDocument

def getData(localPatchFile, id_doc):
  # abrir el archivo PDF en modo de lectura binaria
  with open(localPatchFile, 'rb') as f:
    # crear un objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(f)
    # crear instancias 
    newDocument = Trie(localPatchFile, id_doc)
    # iterar sobre todas las páginas y extraer el texto
    for pagina in pdf_reader.pages:
      # extraer texto
      texto = pagina.extract_text()
      # crea una lista con las palabras del texto
      palabras = texto.split()
      # itera sobre cada palabra e inserta en el trie de la pagina
      for palabra in palabras:
        # eliminamos los caracteres especiales
        palabra = clearSpecialCHAR(palabra)
        # verificamos que la palabra no sea vacia
        if palabra != '':
          # agregamos la palabra al trie 
          newDocument.agregar_palabra(palabra)
      # devuelve el trie
    return newDocument