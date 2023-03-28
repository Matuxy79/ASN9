#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

class treenode(object):

    def __init__(self, data, left=None, right=None):
        """
        Create a new treenode for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the treenode
            left:  Another treenode (or None, by default)
            right:  Another treenode (or None, by default)
        """
        self.data = data
        self.left = left
        self.right = right
        
    def subst(tnode, t, r):
        """
        Substitute all occurrences of target value t with replacement value r
        in the given tree.
        """
        if tnode is None:
            return None

        if tnode.data == t:
            tnode.data = r

        treenode.subst(tnode.left, t, r)
        treenode.subst(tnode.right, t, r)

    def copy(tnode):
        """
        Create a new copy of the given tree with the same structure and data values.
        """
        if tnode is None:
            return None

        # create a new treenode with the same data value
        new_node = treenode(tnode.data)

        # recursively copy the left and right subtrees
        new_node.left = treenode.copy(tnode.left)
        new_node.right = treenode.copy(tnode.right)

        return new_node

