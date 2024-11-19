from word import Word

class Lexicon:
    # initialize lexicon
    def __init__(self, lexicon_file):
        self.entries = {}
        self.load_lexicon(lexicon_file)
    
    # load lexicon from lexicon .txt
    def load_lexicon(self, lexicon_file):
        with open(lexicon_file, 'r') as file:
            for line in file:
                text, pos, root, number = line.strip().split()
                # add word to lexicon
                self.entries[text.lower()] = Word(text, pos, root, number)
        print(self.entries)
    
    # get word from lexicon
    def get_word(self, text):
        return self.entries.get(text.lower())