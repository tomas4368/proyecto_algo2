from function.clearSpecialCHAR import clearSpecialCHAR

def getList(text):
  
  listTEXT = []
  #
  for palabra in text.split():
    palabra = clearSpecialCHAR(palabra)
    # Transformar a minúscula
    palabra = palabra.lower()
    if palabra != '':
      listTEXT.append(palabra)
  #
  return listTEXT