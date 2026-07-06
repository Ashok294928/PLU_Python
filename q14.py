# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function for Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Create the binary tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)

# Perform Inorder Traversal
print("Inorder Traversal:")
inorder(root)