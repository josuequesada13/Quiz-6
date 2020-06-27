class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#Insert
def insert(current, data):
    if current is None:
        return Node(data)
    if data < current.data:
        current.left = insert(current.left, data)
    else:
        current.right = insert(current.right, data)
    return current

#Remove
def removeNode(root, node):
    if root is not None:
        return root
    if node < root.data:
        root.left = removeNode(root.left, node)
    elif node > root.data:
        root.right = removeNode(root.right, node)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = findMinNode(root.right)
        root.data = temp.data
        root.right = removeNode(root.right, temp.data)

#Min node
def findMinNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

#Max node
def findMaxNode(node):
    current = node
    while (current.right is not None):
        current = current.right
    return current

#Print in order
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

#Print in preOrder
def preOrder(root):
    if root is not None:
        print(root.data)
        inOrder(root.left)
        inOrder(root.right)

#Print in postOrder
def postOrder(root):
    if root is not None:
        inOrder(root.left)
        inOrder(root.right)
        print(root.data)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
print("En orden")
inOrder(root)
print("En preorden")
preOrder(root)
print("En postorden")
postOrder(root)


