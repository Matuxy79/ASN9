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

    def collect_data_inorder(tnode):
        """
        Collect all the data values in the given tree in in-order sequence.
        Returns a list of data values.
        """
        result = []
        if tnode is not None:
            result.extend(treenode.collect_data_inorder(tnode.left))
            result.append(tnode.data)
            result.extend(treenode.collect_data_inorder(tnode.right))
        return result

    def count_smaller(tnode, target):
        """
        Count the number of data values in the given tree that are less than the given target value.
        Assumes that the given tree has data values that are numbers only.
        """
        count = 0
        if tnode is not None:
            if tnode.data < target:
                count += 1
                count += treenode.count_smaller(tnode.left, target)
                count += treenode.count_smaller(tnode.right, target)
            else:
                count += treenode.count_smaller(tnode.left, target)
        return count

