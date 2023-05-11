class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1

def rotate_left(x):
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    update_height(x)
    update_height(y)

    return y

def rotate_right(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    update_height(y)
    update_height(x)

    return x

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)

    balance_factor = get_balance_factor(root)

    if balance_factor > 1 and key < root.left.key:
        return rotate_right(root)

    if balance_factor > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance_factor < -1 and key > root.right.key:
        return rotate_left(root)

    if balance_factor < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def inorder_traversal(root):
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.key, end=" ")
    inorder_traversal(root.right)

root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

print("Inorder traversal:", end=" ")
inorder_traversal(root)
print()
