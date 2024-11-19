from lexicon import Lexicon
from rule import RuleSet

class Parser:
    def __init__(self, lexicon, rule_set):
        self.lexicon = lexicon
        self.rule_set = rule_set

    # parsing of sentence
    def parse_sentence(self, sentence):
        words = sentence.split()
        pos_sequence = []
        for word_text in words:
            word = self.lexicon.get_word(word_text)
            if word:
                pos_sequence.append(word.pos)
            else:
                print(f"Word '{word_text}' not found in lexicon.")
                return False
        
        # print sequence
        print(f"POS Sequence: {pos_sequence}")
        
        if self.rule_set.validate_structure(pos_sequence):
            print("Sentence structure is valid.")
            return True
        else:
            print("Invalid sentence structure.")
            return False