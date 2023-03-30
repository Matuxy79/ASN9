#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

from A9Q5 import ordered
from A9Q5 import max_value
from A9Q5 import min_value

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Create some ordered binary trees.
ordered_tree1 = Node(1, Node(0), Node(2))
ordered_tree2 = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

# Create some unordered binary trees.
unordered_tree1 = Node(1, Node(2), Node(0))
unordered_tree2 = Node(4, Node(2, Node(3), Node(1)), Node(6, Node(7), Node(5)))

# Test the ordered function.
assert ordered(None) == True  # Empty tree is ordered.
assert ordered(ordered_tree1) == True
assert ordered(ordered_tree2) == True
assert ordered(unordered_tree1) == False
assert ordered(unordered_tree2) == False
