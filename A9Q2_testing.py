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
treenode.subst(root, 2, 8)

# the tree will become like this:
#       1
#     /   \
#    8     5
#   / \   / \
#  3   4 6   7

# creating a tree to test copy
root = treenode(1,
               left=treenode(2,
                             left=treenode(3),
                             right=treenode(4)),
               right=treenode(5,
                              left=treenode(6),
                              right=treenode(7)))

# create a copy of the tree
new_root = treenode.copy(root)

# the new tree is completely independent from the original tree
root.left.right.data = 100
print(new_root.left.right.data)  # prints 4, not 100

# creating a tree to test collect data in order
root = treenode(1,
               left=treenode(2,
                             left=treenode(3),
                             right=treenode(4)),
               right=treenode(5,
                              left=treenode(6),
                              right=treenode(7)))

# collect the data values in in-order sequence
data_list = treenode.collect_data_inorder(root)

# print the data values
print(data_list)  # prints [3, 2, 4, 1, 6, 5, 7]
