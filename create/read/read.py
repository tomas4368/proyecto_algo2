import PyPDF2

from create.struct import Trie

def read(files):
  #
  listDocument = []
  #
  index = 0
  for file in files:
    listDocument.append(getData(file, index))
    index += 1;
  #
  return listDocument

def getData(localPatchFile, index):
  # abrir el archivo PDF en modo de lectura binaria
  with open(localPatchFile, 'rb') as f:
    # crear un objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(f)
    # crear instancias 
    newDocument = Trie(localPatchFile, index)
    # iterar sobre todas las páginas y extraer el texto
    for pagina in pdf_reader.pages:
      # extraer texto
      texto = pagina.extract_text()
      # divide el texto en palabras usando espacios como delimitador
      palabras = texto.split()
      # itera sobre cada palabra e inserta en trie de la pagina
      for palabra in palabras:
        palabra = clear(palabra)
        if palabra != '':
          newDocument.agregar_palabra(palabra)
      #
    return newDocument

# limpia y solo deja las letras
def clear(string):
  return ''.join([char for char in string if char.isalpha()])