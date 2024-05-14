import pickle
import create.trie

def search(text):
  with open('db.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    create.trie.print_trie(loaded_data.pages[0].trie.root)
    print(create.trie.search(loaded_data.pages[0].trie, text))

