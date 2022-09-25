def solve(root,key):
    floor = -1
    while root:
        if root.val == key :
            floor = root.val
            return floor
        if key > root.val:
            floor = root.val
            root = root.right
        else:
            root = root.left

    return floor
