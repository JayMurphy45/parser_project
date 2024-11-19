class Word:
    def __init__(self, text, pos, root, number):
        self.text = text
        self.pos = pos
        self.root = root
        self.number = number

    def __str__(self):
        return f"{self.text} ({self.pos}, root: {self.root}, number: {self.number})"