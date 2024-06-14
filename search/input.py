from function.clearSpecialCHAR import clearSpecialCHAR, lista_sufijos

def getList(text):
  
  listTEXT = []
  #
  for palabra in text.split():
    palabra = clearSpecialCHAR(palabra)
    # Transformar a minúscula
    palabra = palabra.lower()
    if palabra != '':
      if len(palabra) - 3 >= 9:
        n = 9
      else:
        n = len(palabra) - 3
        if n < 0:
          n = 0
      for i in range(n, 0, -1):
        if lista_sufijos.get(palabra[-i:]):
          palabra = palabra[:-i]
          break
      listTEXT.append(palabra)
  #
  return listTEXT