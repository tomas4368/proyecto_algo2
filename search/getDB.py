import pickle

def getDB():
  with open('db.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    return loaded_data