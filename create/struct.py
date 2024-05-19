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