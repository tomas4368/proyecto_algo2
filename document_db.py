import sys
from create.create import create

def error():
  print("error: no se especificó una operación (utilice -help para ayuda)")

def help():
  print(
"""uso:  document_db.py <operación> [...]
operaciones:
    document_db.py -create <local_path>
    document_db.py -search <"text">""")

def main():
  # cunado no se a agregado argumentos
  if len(sys.argv) == 1:
    return error()
  # Para la creación de la estructura se utilizará el siguiente comando: python document_db.py -create <local_path>
  if sys.argv[1] == '-create':
    # verificar si hay path
    if len(sys.argv) == 2 or len(sys.argv) > 3:
      return error()
    # llamar función
    create(sys.argv[2])
  #  Para la generación de consultas se utilizará el siguiente comando: python document_db.py -search <text>
  elif sys.argv[1] == '-search':
    # verificar si hay path
    if len(sys.argv) == 2 or len(sys.argv) > 3:
      return error()
    # llamar función
    # search(sys.argv[2])
  # consulta
  elif sys.argv[1] == '-help':
    return help()
  # default
  return error()

if __name__ == "__main__":
  main()

# La última parte del código es una convención común en Python para 
# garantizar que el código se ejecute solo si el script se está ejecutando 
# directamente y no se está importando como un módulo en otro script.

# `if __name__ == "__main__":`:
  # `__name__` es una variable especial en Python que representa el nombre 
  # del módulo actual.
  # Cuando un script Python se ejecuta, el valor de `__name__` es establecido
  # como `"__main__"`.
  # Entonces, esta condición se evalúa como verdadera solo cuando el script 
  # se está ejecutando directamente desde la línea de comandos o desde otro 
  # script principal.
# `main()`:
  # Esto llama a la función `main()` definida en el script cuando se ejecuta 
  # directamente.
  # Esta estructura asegura que el código en el bloque `if __name__ == "__main__":` 
  # solo se ejecute cuando el archivo "system.py" se ejecuta como un script 
  # principal y no cuando se importa como un módulo en otro archivo. Esto es 
  # útil para evitar que cierto código se ejecute cuando solo se está importando 
  # el script como una biblioteca en otro lugar.