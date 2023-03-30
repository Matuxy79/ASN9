#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#importing the complete tree
from A9Q4 import complete_tree
from A9Q4 import cmplt

#The below tree is a complete binary tree.
root = cmplt(1)
root.left = cmplt(2)
root.right = cmplt(3)
root.left.left = cmplt(4)
root.left.right = cmplt(5)
root.right.left = cmplt(6)
assert complete_tree(root) == True

#The below tree is not a complete binary tree because the right subtree of the second level is incomplete.
root = cmplt(1)
root.left = cmplt(2)
root.right = cmplt(3)
root.left.left = cmplt(4)
root.left.right = cmplt(5)
root.right.right = cmplt(7)
assert complete_tree(root) == False

#Test with a tree with only one node
root = cmplt(1)
assert complete_tree(root) == True
