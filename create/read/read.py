import PyPDF2

from create.read.trie import Trie, insert
from create.struct import Document, Page

def read(files):
  #
  listDocument = []
  #
  for file in files:
    listDocument.append(getData(file))
  #
  return listDocument

def getData(localPatchFile):
  # abrir el archivo PDF en modo de lectura binaria
  with open(localPatchFile, 'rb') as f:
    # crear un objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(f)
    # crear instancias 
    newDocument = Document(localPatchFile)
    #
    pageIndex = 1
    # iterar sobre todas las páginas y extraer el texto
    for pagina in pdf_reader.pages:
      # extraer texto
      texto = pagina.extract_text()
      # divide el texto en palabras usando espacios como delimitador
      palabras = texto.split()
      # crear pagina
      page = Page(pageIndex, Trie())
      # itera sobre cada palabra e inserta en trie de la pagina
      for palabra in palabras:
        insert(page.trie, palabra)
      #
      pageIndex = pageIndex + 1
      # Agregar las instancias de la clase Page a la lista de páginas en Document
      newDocument.add_page(page)
    #
    return newDocument