from TreeNode import TreeNode

def insert(root, val, prev = None, direction = -1):
    #base case
    if not root:
        if direction == 0:
            prev.left = TreeNode(val)
        elif direction == 1:
            prev.right = TreeNode(val)
    #recursive case
    else:
        #direction parameter, 0 stands for left child 1 stands for right child
        if root.val < val:
            insert(root.right, val, root, 1)
        elif root.val > val:
            insert(root.left, val, root, 0)

def search(root, val):
    if not root:
        return False
    elif root.val == val:
        return True
    else:
        if root.val < val:
            return search(root.right, val)
        else:
            return search(root.left, val)
        

def delete(root, val):
    return None

def printTreeSideWay(root, prefix = ''):
    #base
    if not root:
        return 
    #recursive case
    else:
        printTreeSideWay(root.right, prefix + '    ')
        print(prefix + str(root.val))
        printTreeSideWay(root.left, prefix + '    ')

root = TreeNode(88)

insert(root, 5)
insert(root, 105)
insert(root, 104)
insert(root, 100)
printTreeSideWay(root)

print('Does 105 exist? ' + str(search(root, 105)))
print('Does 104 exist? ' + str(search(root, 104)))
print('Does 103 exist? ' + str(search(root, 103)))