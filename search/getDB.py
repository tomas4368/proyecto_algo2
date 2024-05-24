import pickle

def getDB():
  try:
    with open('db.pkl', 'rb') as f:
      loaded_data = pickle.load(f)
      return loaded_data
  except OSError as e:
    # salir por error
    print(f"Error reading database: {e}")
    exit(0)