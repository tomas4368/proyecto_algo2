import math

class TF:
  def __init__(self, localPath):
    # Inicializa el diccionario
    self.localPath = localPath
    self.diccionario = {}

  def agregar_palabra(self, palabra, countElement, countElementRoot):
    # Incrementa la frecuencia de la palabra
    self.diccionario[palabra] = (countElement/countElementRoot)

class IDF:
  def __init__(self):
    # Inicializa el diccionario
    self.diccionario = {}

  def agregar_palabra(self, palabra, documentsTRIE):
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      # buscar por documento
      id_doc = []
      # cuenta la cantidad de documentos en los que aparece la palabra
      count = 0
      for docTRIE in documentsTRIE:
        # si existe la palabra
        if palabra in docTRIE.diccionario:
          id_doc.append(docTRIE.id_doc)
          count += 1
      # add
      auxIDF = math.log(len(documentsTRIE)/count)
      self.diccionario[palabra] = {'IDF': auxIDF, 'id_doc': id_doc}
  
  def search(self, palabra):
    # Transformar a minúscula
    palabra = palabra.lower()
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      return None
    #
    return self.diccionario[palabra]

class Trie:
  def __init__(self, localPath, id_doc):
    self.localPath = localPath
    self.diccionario = {}
    self.id_doc = id_doc
    self.element = 0

  def agregar_palabra(self, palabra):
    # Transformar a minúscula
    palabra = palabra.lower()
    if lista_stopwords.get(palabra):
      return
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
    # Si la palabra no está en el diccionario, la agrega con la información de la página
    if palabra not in self.diccionario:
      self.diccionario[palabra] = 0
    # Incrementa la frecuencia de la palabra
    self.diccionario[palabra] += 1
    # Incrementa elementos
    self.element += 1

class DATA:
  def __init__(self, idf, listTF):
    self.idf = idf
    self.listTF = listTF

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
}