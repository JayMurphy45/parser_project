from lexicon import Lexicon
from rule import RuleSet
from parser import Parser
from binarytree import BinaryTree

# Load lexicon and rules
lexicon = Lexicon("lexicon.txt")
rule_set = RuleSet("rules.txt")
parser = Parser(lexicon, rule_set)

sentence = "A person dislikes the white dog"

# Parse the sentence to get its POS tags
words = sentence.split()
pos_sequence = []
word_objects = []

for word_text in words:
    word = lexicon.get_word(word_text)
    if word:
        pos_sequence.append(word.pos)
        word_objects.append((word_text, word.pos))
    else:
        print(f"Word '{word_text}' not found in lexicon.")
        exit()



# Check validity using the rule set
if rule_set.validate_structure(pos_sequence):
    parser.parse_sentence(sentence)


    # Generate and display the tree using BinaryTree
    tree = BinaryTree.construct_tree(word_objects)
    BinaryTree.display_tree(tree)
else:
    print("Invalid sentence structure.")