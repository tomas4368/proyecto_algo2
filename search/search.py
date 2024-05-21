import pickle

def search(text):
  with open('db.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data.listTF[loaded_data.idf.search(text)['docIndex'][0]].localPath)
