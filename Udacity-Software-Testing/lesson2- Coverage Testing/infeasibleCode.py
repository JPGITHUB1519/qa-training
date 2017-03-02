"""
    Infeasible Code
        Is a code that is not alcanzable and we cannot cover it for the cover measuring
"""

class Node:
    def __init__(self):
        self.height = 5

class Tree:
    def __init__(self):
        self.left = Node()
        self.right = Node()

def balanced():
    arbol = Tree()
    if arbol.left.height != arbol.right.height:
        # Never reachable at least one error
        # this code will be no cover by the coverage framework
        return False # pragma: no cover

balanced()