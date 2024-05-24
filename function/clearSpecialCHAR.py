import unicodedata

def clearSpecialCHAR(string):
  # Normalizar la cadena en forma NFD (descomposición canónica)
  nfkd_form = unicodedata.normalize('NFD', string)
  # Filtrar caracteres diacríticos y no alfabéticos
  cadena_sin_acentos_y_solo_letras = ''.join([char for char in nfkd_form if not unicodedata.combining(char) and char.isalpha()])
  # Re-normalizar en forma NFC para recomponer los caracteres
  return unicodedata.normalize('NFC', cadena_sin_acentos_y_solo_letras)