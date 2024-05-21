# limpia y solo deja las letras
def clearSpecialCHAR(string):
  return ''.join([char for char in string if char.isalpha()])