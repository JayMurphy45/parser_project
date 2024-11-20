from nltk.tree import Tree

class BinaryTree:
    @staticmethod
    def construct_tree(word_objects):
        
        # Split into NP and VP
        np = Tree("NP", [Tree(pos, [word]) for word, pos in word_objects[:2]])
        vp = Tree("VP", [Tree(pos, [word]) for word, pos in word_objects[2:]])
        
        # sentence level
        tree = Tree("S", [np, vp])
        return tree

    @staticmethod
    def display_tree(tree):
        print("\nSyntax Tree:")
        tree.pretty_print()