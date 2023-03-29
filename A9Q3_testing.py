#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#Importing a9q3
from A9Q3 import expression

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example expression tree: ((4 + 13) * (9 - 5))
t = Node('*', Node('+', Node(4), Node(13)), Node('-', Node(9), Node(5)))
assert expression(t) == '((4 + 13) * (9 - 5))'

# Empty tree
t = None
assert expression(t) == ''

# Tree with just one node
t = Node(5)
assert expression(t) == '5'

# Balanced tree with depth 3
t = Node('*', Node('+', Node(4), Node(13)), Node('-', Node(9), Node(5)))
assert expression(t) == '((4 + 13) * (9 - 5))'

# Unbalanced tree with depth 3
t = Node('*', Node('*', Node(2), Node(3)), Node('+', Node(4), Node(5)))
assert expression(t) == '((2 * 3) * (4 + 5))'

# Balanced tree with depth 4
t = Node('*', Node('-', Node('+', Node(1), Node(2)), Node(3)), Node('/', Node('*', Node(4), Node(5)), Node(6)))
assert expression(t) == '(((1 + 2) - 3) * ((4 * 5) / 6))'

# Unbalanced tree with depth 4
t = Node('*', Node('*', Node(1), Node(2)), Node('*', Node(3), Node('*', Node(4), Node(5))))
assert expression(t) == '((1 * 2) * (3 * (4 * 5)))'

print("All tests pass")
