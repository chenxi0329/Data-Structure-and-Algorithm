from TreeNode import TreeNode

def findMin(root):
    if not root:
        return None
    else:
        while root.left:
            root = root.left
        return root

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
    #two base cases here
    if not root:
        return False
    elif root.val == val:
        return True
    #recursive case
    else:
        if root.val < val:
            return search(root.right, val)
        else:
            return search(root.left, val)
        

def delete(root, val):
    if not root:
        return None
    else:
        if root.val < val:
            root.right = delete(root.right, val)
        elif root.val > val:
            root.left = delete(root.left, val)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNodeFromLeftSubtree = findMin(root.right)
                root.val = minNodeFromLeftSubtree.val
                delete(root.right, minNodeFromLeftSubtree.val)
    return root

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

root = TreeNode(3)
insert(root, 2)
insert(root, 0)
insert(root, 1)
insert(root, 6)
insert(root, 5)

printTreeSideWay(root)
print('Just inserted 0,1,2,3,4,5,6')
print('Does 5 exist? ' + str(search(root, 5)))
print('Does 6 exist? ' + str(search(root, 6)))
print('Does 7 exist? ' + str(search(root, 7)))
print('Does 8 exist? ' + str(search(root, 8)))


root = delete(root, 1)
printTreeSideWay(root)
print('Just deleted 1')
print('Does 1 exist? ' + str(search(root, 1)))

root = delete(root, 3)
printTreeSideWay(root)
print('Just deleted 3')
print('Does 3 exist? ' + str(search(root, 3)))

root = delete(root, 6)
printTreeSideWay(root)
print('Just deleted 6')
print('Does 6 exist? ' + str(search(root, 6)))

root = delete(root, 5)
printTreeSideWay(root)
print('Just deleted 5')
print('Does 5 exist? ' + str(search(root, 5)))

root = delete(root, 2)
printTreeSideWay(root)
print('Just deleted 2')
print('Does 2 exist? ' + str(search(root, 2)))

root = delete(root, 0)
printTreeSideWay(root)
print('Just deleted 0')
print('Does 0 exist? ' + str(search(root, 0)))