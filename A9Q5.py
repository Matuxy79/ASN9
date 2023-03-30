#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def ordered(tnode):
    """
    Returns True if the binary tree rooted at tnode is ordered, and False otherwise.
    """
    if tnode is None:
        return True  # An empty tree is ordered by definition.

    # Check if the left and right subtrees are ordered.
    left_ordered = ordered(tnode.left)
    right_ordered = ordered(tnode.right)

    # If either subtree is not ordered, the whole tree is not ordered.
    if not left_ordered or not right_ordered:
        return False

    # Check if all data values in the left subtree are less than the root's data value.
    if tnode.left is not None:
        if max_value(tnode.left) >= tnode.data:
            return False

    # Check if all data values in the right subtree are greater than the root's data value.
    if tnode.right is not None:
        if min_value(tnode.right) <= tnode.data:
            return False

    # If all checks pass, the tree is ordered.
    return True


def max_value(tnode):
    """
    Returns the maximum data value in the binary tree rooted at tnode.
    Assumes that the tree is non-empty.
    """
    while tnode.right is not None:
        tnode = tnode.right
    return tnode.data


def min_value(tnode):
    """
    Returns the minimum data value in the binary tree rooted at tnode.
    Assumes that the tree is non-empty.
    """
    while tnode.left is not None:
        tnode = tnode.left
    return tnode.data
