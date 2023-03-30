#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def complete_tree(tnode):
    def cmplt(tnode):
        if tnode is None:
            return True, 0
        else:
            left_flag, left_height = cmplt(tnode.left)
            right_flag, right_height = cmplt(tnode.right)
            if left_flag and right_flag and left_height == right_height:
                return True, left_height + 1
            else:
                return False, None

    flag, height = cmplt(tnode)
    return flag

"""the new cmplt() function uses recursive calls to check the completeness of the left and right subtrees. If both subtrees are complete and have the same height, then the entire subtree is complete, and we return True with the updated height of the subtree. Otherwise, the subtree is not complete, and we return False with None for the height."""