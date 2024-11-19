from lexicon import Lexicon
from rule import RuleSet
from parser import Parser

lexicon = Lexicon("lexicon.txt")
rule_set = RuleSet("rules.txt")
parser = Parser(lexicon, rule_set)

sentence = "A person dislikes the white dog"
parser.parse_sentence(sentence)