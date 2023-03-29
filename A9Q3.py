#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def expression(t):
    if t is None:
        return ''
    if t.left is None and t.right is None:
        return str(t.val)
    left_expr = expression(t.left)
    right_expr = expression(t.right)
    return f"({left_expr} {t.val} {right_expr})"
