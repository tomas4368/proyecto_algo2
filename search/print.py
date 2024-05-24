def printResult(data):
  if len(data) == 0:
    print("document not found")
  else:
    # Ordenar por claves numéricas en orden descendente
    ordenadoResultado = {k: data[k] for k in sorted(data, reverse=True)}
    # Mostrar el diccionario ordenado por claves numéricas en orden descendente
    count = 1
    for valor in ordenadoResultado.values():
      print(f'{count}: {valor}')
      count += 1