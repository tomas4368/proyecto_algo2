import pickle

def seve(data):
  # serializar el objeto y guardarlo en un archivo
  with open('db.pkl', 'wb') as f:
    pickle.dump(data, f)