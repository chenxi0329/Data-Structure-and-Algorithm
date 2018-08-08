from TreeNode import TreeNode

def contains(node, val):
    if not node:
        return False
    elif node.val == val:
        return True
    else:
        return contains(node.left, val) or contains(node.right, val)

def printTreeSideWayHelper(root, prefix = ''):
    #base
    if not root:
        return 
    #recursive case
    else:
        printTreeSideWayHelper(root.right, prefix + '    ')
        print(prefix + str(root.val))
        printTreeSideWayHelper(root.left, prefix + '    ')    

def printTreeSideWay(root):
    print('------------------------------------')
    printTreeSideWayHelper(root)
    print('------------------------------------')

def printTree(root):
    if not root:
        return
    else:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

root = TreeNode(5)
n1 = TreeNode(7)
n2 = TreeNode(1)
n3 = TreeNode(2)
n4 = TreeNode(10)
n5 = TreeNode(15)
root.right = n1
n1.right = n2
n2.left = n3
root.left = n4
n4.right = n5
printTree(root)
printTreeSideWay(root)
print('Does it contain 10?')
print(contains(root, 10))
print('Does it contain 11?')
print(contains(root, 11))
print('Does it contain 12?')
print(contains(root, 12))