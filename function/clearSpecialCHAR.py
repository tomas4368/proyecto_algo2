import unicodedata

def clearSpecialCHAR(string):
  # Normalizar la cadena en forma NFD (descomposición canónica)
  nfkd_form = unicodedata.normalize('NFD', string)
  # Filtrar caracteres diacríticos y no alfabéticos
  cadena_sin_acentos_y_solo_letras = ''.join([char for char in nfkd_form if not unicodedata.combining(char) and char.isalpha()])
  # Re-normalizar en forma NFC para recomponer los caracteres
  return unicodedata.normalize('NFC', cadena_sin_acentos_y_solo_letras)

lista_stopwords = {
    "a": True,
    "al": True,
    "algo": True,
    "algunas": True,
    "algunos": True,
    "ante": True,
    "antes": True,
    "como": True,
    "con": True,
    "contra": True,
    "cual": True,
    "cuando": True,
    "de": True,
    "del": True,
    "desde": True,
    "donde": True,
    "durante": True,
    "e": True,
    "el": True,
    "ella": True,
    "ellas": True,
    "ellos": True,
    "en": True,
    "entre": True,
    "era": True,
    "erais": True,
    "eran": True,
    "eras": True,
    "eres": True,
    "es": True,
    "esa": True,
    "esas": True,
    "ese": True,
    "eso": True,
    "esos": True,
    "esta": True,
    "estaba": True,
    "estabais": True,
    "estaban": True,
    "estabas": True,
    "estad": True,
    "estada": True,
    "estadas": True,
    "estado": True,
    "estados": True,
    "estamos": True,
    "estando": True,
    "estar": True,
    "estaremos": True,
    "estará": True,
    "estarán": True,
    "estarás": True,
    "estaré": True,
    "estaréis": True,
    "estaría": True,
    "estaríais": True,
    "estaríamos": True,
    "estarían": True,
    "estarías": True,
    "estas": True,
    "este": True,
    "estemos": True,
    "esto": True,
    "estos": True,
    "estoy": True,
    "estuve": True,
    "estuviera": True,
    "estuvierais": True,
    "estuvieran": True,
    "estuvieras": True,
    "estuvieron": True,
    "estuviese": True,
    "estuvieseis": True,
    "estuviesen": True,
    "estuvieses": True,
    "estuvimos": True,
    "estuviste": True,
    "estuvisteis": True,
    "estuviéramos": True,
    "estuviésemos": True,
    "estuvo": True,
    "está": True,
    "estábamos": True,
    "estáis": True,
    "están": True,
    "estás": True,
    "fue": True,
    "fuera": True,
    "fuerais": True,
    "fueran": True,
    "fueras": True,
    "fueron": True,
    "fuese": True,
    "fueseis": True,
    "fuesen": True,
    "fueses": True,
    "fui": True,
    "fuimos": True,
    "fuiste": True,
    "fuisteis": True,
    "fuéramos": True,
    "fuésemos": True,
    "ha": True,
    "habida": True,
    "habidas": True,
    "habido": True,
    "habidos": True,
    "habiendo": True,
    "habremos": True,
    "habrá": True,
    "habrán": True,
    "habrás": True,
    "habré": True,
    "habréis": True,
    "habría": True,
    "habríais": True,
    "habríamos": True,
    "habrían": True,
    "habrías": True,
    "habéis": True,
    "había": True,
    "habíais": True,
    "habíamos": True,
    "habían": True,
    "habías": True,
    "hasta": True,
    "hay": True,
    "haya": True,
    "hayamos": True,
    "hayan": True,
    "hayas": True,
    "hayáis": True,
    "he": True,
    "hemos": True,
    "hube": True,
    "hubiera": True,
    "hubierais": True,
    "hubieran": True,
    "hubieras": True,
    "hubieron": True,
    "hubiese": True,
    "hubieseis": True,
    "hubiesen": True,
    "hubieses": True,
    "hubimos": True,
    "hubiste": True,
    "hubisteis": True,
    "hubiéramos": True,
    "hubiésemos": True,
    "hubo": True,
    "la": True,
    "las": True,
    "le": True,
    "les": True,
    "lo": True,
    "los": True,
    "me": True,
    "mi": True,
    "mis": True,
    "mucho": True,
    "muchos": True,
    "muy": True,
    "más": True,
    "mí": True,
    "mía": True,
    "mías": True,
    "mío": True,
    "míos": True,
    "nada": True,
    "ni": True,
    "no": True,
    "nos": True,
    "nosotras": True,
    "nosotros": True,
    "nuestra": True,
    "nuestras": True,
    "nuestro": True,
    "nuestros": True,
    "o": True,
    "os": True,
    "otra": True,
    "otras": True,
    "otro": True,
    "otros": True,
    "para": True,
    "pero": True,
    "poco": True,
    "por": True,
    "porque": True,
    "que": True,
    "quien": True,
    "quienes": True,
    "qué": True,
    "se": True,
    "sea": True,
    "seamos": True,
    "sean": True,
    "seas": True,
    "sentid": True,
    "sentida": True,
    "sentidas": True,
    "sentido": True,
    "sentidos": True,
    "seremos": True,
    "será": True,
    "serán": True,
    "serás": True,
    "seré": True,
    "seréis": True,
    "sería": True,
    "seríais": True,
    "seríamos": True,
    "serían": True,
    "serías": True,
    "seáis": True,
    "sido": True,
    "siendo": True,
    "sin": True,
    "sobre": True,
    "sois": True,
    "somos": True,
    "son": True,
    "soy": True,
    "su": True,
    "sus": True,
    "suya": True,
    "suyas": True,
    "suyo": True,
    "suyos": True,
    "sí": True,
    "también": True,
    "tanto": True,
    "te": True,
    "tendremos": True,
    "tendrá": True,
    "tendrán": True,
    "tendrás": True,
    "tendré": True,
    "tendréis": True,
    "tendría": True,
    "tendríais": True,
    "tendríamos": True,
    "tendrían": True,
    "tendrías": True,
    "tened": True,
    "tenemos": True,
    "tenga": True,
    "tengamos": True,
    "tengan": True,
    "tengas": True,
    "tengo": True,
    "tengáis": True,
    "tenida": True,
    "tenidas": True,
    "tenido": True,
    "tenidos": True,
    "teniendo": True,
    "tenéis": True,
    "tenía": True,
    "teníais": True,
    "teníamos": True,
    "tenían": True,
    "tenías": True,
    "ti": True,
    "tiene": True,
    "tienen": True,
    "tienes": True,
    "todo": True,
    "todos": True,
    "tu": True,
    "tus": True,
    "tuve": True,
    "tuviera": True,
    "tuvierais": True,
    "tuvieran": True,
    "tuvieras": True,
    "tuvieron": True,
    "tuviese": True,
    "tuvieseis": True,
    "tuviesen": True,
}

lista_sufijos = {
    "able": True,
    "ación": True,
    "ancia": True,
    "ante": True,
    "anza": True,
    "ario": True,
    "asco": True,
    "ato": True,
    "ble": True,
    "ción": True,
    "dor": True,
    "dura": True,
    "eño": True,
    "esco": True,
    "és": True,
    "ez": True,
    "fobia": True,
    "fono": True,
    "genio": True,
    "grafía": True,
    "ico": True,
    "idad": True,
    "iego": True,
    "iento": True,
    "ismo": True,
    "ista": True,
    "itis": True,
    "ivo": True,
    "logía": True,
    "mento": True,
    "ncia": True,
    "nte": True,
    "oide": True,
    "or": True,
    "oso": True,
    "sión": True,
    "ura": True,
    "voro": True,
    "zuelo": True,
    "iador": True,
    "iadora": True,
    "ar": True,
    "al": True,
    "ón": True,
    "ito": True,
    "ita": True,
    "ón": True,
    "ano": True,
    "ana": True,
    "ino": True,
    "ina": True,
    "aje": True,
    "aje": True,
    "oría": True,
    "ismo": True,
    "ístico": True,
    "ístico": True,
    "ificación": True,
    "icación": True,
    "era": True,
    "ero": True,
    "illo": True,
    "illo": True,
    "ura": True,
    "dad": True,
    "tud": True,
    "dumbre": True,
    "dad": True,
    "oría": True,
    "ería": True,
    "ez": True,
    "ez": True,
    "ería": True,
    "azo": True,
    "azo": True,
    "ito": True,
    "ita": True,
    "ero": True,
    "era": True,
    "oso": True,
    "osa": True,
    "illo": True,
    "illa": True,
    "ón": True,
    "or": True,
    "ora": True,
    "oso": True,
    "osa": True,
    "al": True,
    "al": True,
    "ento": True,
    "iento": True,
    "al": True,
    "il": True,
    "il": True,
    "ería": True,
    "ería": True,
    "érrimo": True,
    "érrimo": True,
    "azo": True,
    "azo": True,
    "acho": True,
    "acha": True,
    "aco": True,
    "aca": True,
    "ato": True,
    "ata": True,
    "cida": True,
    "cido": True,
    "cería": True,
    "cero": True,
    "cracia": True,
    "crata": True,
    "dad": True,
    "dor": True,
    "dora": True,
    "dumbre": True,
    "ear": True,
    "ear": True,
    "ería": True,
    "ero": True,
    "eria": True,
    "ero": True,
    "és": True,
    "ez": True,
    "eza": True,
    "filo": True,
    "fobia": True,
    "fobo": True,
    "grama": True,
    "grafo": True,
    "ícola": True,
    "ícola": True,
    "ico": True,
    "illa": True,
    "illo": True,
    "ina": True,
    "ino": True,
    "ismo": True,
    "ista": True,
    "izar": True,
    "izar": True,
    "mente": True,
    "mente": True,
    "ón": True,
    "ón": True,
    "ona": True,
    "or": True,
    "oso": True,
    "oso": True,
    "ote": True,
    "ote": True,
    "triz": True,
    "triz": True,
    "ulento": True,
    "ulenta": True,
    "undio": True,
    "undia": True,
    "ura": True,
    "uro": True,
    "uro": True,
    "uro": True,
    "zuela": True,
    "zuelo": True,
    "abas": True,
    "ábamos": True,
    "abais": True,
    "aban": True,
    "ada": True,
    "ado": True,
    "amos": True,
    "ando": True,
    "ar": True,
    "ara": True,
    "arais": True,
    "aran": True,
    "aras": True,
    "are": True,
    "aremos": True,
    "aréis": True,
    "aría": True,
    "aríais": True,
    "aríamos": True,
    "arían": True,
    "arías": True,
    "aron": True,
    "as": True,
    "ás": True,
    "ás": True,
    "aste": True,
    "asteis": True,
    "é": True,
    "emos": True,
    "éis": True,
    "en": True,
    "es": True,
    "és": True,
    "ido": True,
    "iendo": True,
    "imos": True,
    "ir": True,
    "iendo": True,
    "irá": True,
    "irán": True,
    "iría": True,
    "iríamos": True,
    "irían": True,
    "irías": True,
    "o": True,
    "ía": True,
    "ías": True,
    "íamos": True,
    "íais": True,
    "ían": True,
    "ió": True,
    "í": True,
    "éis": True,
    "én": True,
    "idez": True
}