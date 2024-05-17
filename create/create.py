from math import erf
import os
import pickle
import PyPDF2 # type: ignore
from create.trie import Trie, insert, print_trie



class Page:
    def __init__(self, index, trie):
        self.index = index
        self.trie = trie

class Document:
    def __init__(self, local_path):
        self.local_path = local_path
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)


def create(local_path):
  # check local path
  if not checkLocalPath(local_path):
    exit
  #
  file(local_path)

def checkLocalPath(local_path):
  #
  contenido = []
  # obtener archivos
  try:
    contenido = os.listdir(local_path)
  except OSError as e:
    print(f"Error al listar el contenido de '{local_path}': {e}")
    return False
  # verificar si hay archivos
  if len(contenido) == 0:
    print(f"Error al listar el contenido de '{local_path}': No hay documentos")
    return False
  return True


def file(local_path):
  archivos = os.listdir(local_path)

  # Imprimir los nombres de los archivos
  for archivo in archivos:
      read(local_path+'\\'+archivo)

def read(local_path):
  # Abrir el archivo PDF en modo de lectura binaria
  with open(local_path, 'rb') as f:
    # Crear un objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(f)
    
    # Obtener el número total de páginas en el PDF
    num_paginas = len(pdf_reader.pages)
    
    # Crear instancias de la clase Page
    document = Document(local_path)
    
    pageIndex = 1

    # Iterar sobre todas las páginas y extraer el texto
    for pagina in pdf_reader.pages:
      texto = pagina.extract_text()
      # Divide el texto en palabras usando espacios como delimitador
      palabras = texto.split()
      
      #
      page = Page(pageIndex, Trie())
      #

      # Itera sobre cada palabra e imprímela
      for palabra in palabras:
        print(palabra)
        insert(page.trie, palabra)
      
      pageIndex = pageIndex + 1

      # Agregar las instancias de la clase Page a la lista de páginas en Document
      document.add_page(page)

    save(document)


def save(file):
  print(file.pages)
  # Serializar el objeto y guardarlo en un archivo
  with open('db.pkl', 'wb') as f:
    pickle.dump(file, f)