#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

from A9Q2 import treenode

# creating a tree to test subst
root = treenode(1,
               left=treenode(2,
                             left=treenode(3),
                             right=treenode(4)),
               right=treenode(5,
                              left=treenode(6),
                              right=treenode(7)))

# substitute all occurrences of 2 with 8
subst(root, 2, 8)

# the tree now looks like this:
#       1
#     /   \
#    8     5
#   / \   / \
#  3   4 6   7
