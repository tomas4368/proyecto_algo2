def calcular_tf_idf(tf, idf):
    tf_idf = []
    for doc_tf in tf:
        doc_tf_idf = {}
        for palabra, tf_valor in doc_tf.items():
            if palabra in idf:
                doc_tf_idf[palabra] = tf_valor * idf[palabra]
        tf_idf.append(doc_tf_idf)
    return tf_idf

def calcular_tf(documentos):
    tf = []
    for doc in documentos:
        term_freq = {}
        total_palabras = len(doc)
        for palabra in doc:
            if palabra in term_freq:
                term_freq[palabra] += 1
            else:
                term_freq[palabra] = 1
        for palabra in term_freq:
            term_freq[palabra] /= total_palabras
        tf.append(term_freq)
    return tf

import math

def calcular_idf(documentos):
    num_docs = len(documentos)
    idf = {}
    for doc in documentos:
        for palabra in doc:
            if palabra in idf:
                idf[palabra] += 1
            else:
                idf[palabra] = 1
    for palabra in idf:
        idf[palabra] = math.log(num_docs / (1 + idf[palabra]))
    return idf

def vectorizar(tf_idf_dict, terminos):
    return [tf_idf_dict.get(termino, 0) for termino in terminos]

def similitud_coseno(vector1, vector2):
    dot_product = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    magnitude1 = math.sqrt(sum(vector1[i] ** 2 for i in range(len(vector1))))
    magnitude2 = math.sqrt(sum(vector2[i] ** 2 for i in range(len(vector2))))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0 
    return dot_product / (magnitude1 * magnitude2)