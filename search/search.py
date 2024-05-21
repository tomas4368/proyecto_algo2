"""
class Page:
  #
  def __init__(self, index, trie):
    self.index = index
    self.trie = trie

class Document:
  #
  def __init__(self, localPath):
    self.localPath = localPath
    self.pages = []
  #
  def add_page(self, page):
    self.pages.append(page)
"""


import pickle


def search(text):
  with open('db.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    for document in loaded_data:
      print(document.localPath)

  
