class Rule:
    def __init__(self, pos_tags, pattern):
        self.pos_tags = pos_tags
        self.pattern = pattern

class RuleSet:
    def __init__(self, rules_file):
        self.rules = []
        self.pos_tags = []
        self.load_rules(rules_file)

    # load rules from rules .txt
    def load_rules(self, rules_file):
        with open(rules_file, 'r') as file:
            # First line contains POS tags
            self.pos_tags = file.readline().strip().split()
            # Following lines contain patterns
            for line in file:
                pattern = line.strip().split()
                rule = Rule(self.pos_tags, pattern)
                self.rules.append(rule)

    def validate_structure(self, pos_sequence):
        # Check for S -> NP VP .ie needs to have 2 pos tagy
        if len(pos_sequence) < 2:
            return False  

        # Try to match against the top-level rule
        np_pos = pos_sequence[:2]
        vp_pos = pos_sequence[2:]
        
        if self.validate_np(np_pos) and self.validate_vp(vp_pos):
            return True
        
        return False

    def validate_np(self, np_sequence):
        # Check if NP matches any of the rules
        if np_sequence in [['DET', 'N'], ['DET', 'ADJ', 'N']]:
            return True
        return False

    def validate_vp(self, vp_sequence):
        # Check if VP matches the rules
        if len(vp_sequence) >= 2 and vp_sequence[0] == 'V':
            return self.validate_np(vp_sequence[1:])
        return False