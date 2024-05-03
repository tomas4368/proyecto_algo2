import sys
from create.create import create

def index():
  print("Menú de opciones:")
  print("1. Opción 1")
  print("2. Opción 2")
  print("3. Opción 3")


def main():
  print(sys.argv)
  if len(sys.argv) > 1:
    # Para la creación de la estructura se utilizará el siguiente comando: python document_db.py -create <local_path>
    if sys.argv[1] == '-create':
      # verificar si hay path
      if len(sys.argv) == 2:
        print('falta <local_path>')
        return
      create(sys.argv[2])
      print('OK')
    #  Para la generación de consultas se utilizará el siguiente comando: python document_db.py -search <text>
    elif sys.argv[1] == '-search':
      # verificar si hay path
      if len(sys.argv) == 2 or len(sys.argv) > 3:
        print('falta <local_path>')
        return
      # search(sys.argv[2])
      print('OK')
    else:
      index()
  else:
    index()

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