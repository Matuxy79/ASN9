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
            return

        if tnode.data == t:
            tnode.data = r

        subst(tnode.left, t, r)
        subst(tnode.right, t, r)
