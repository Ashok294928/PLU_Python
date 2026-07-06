# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count nodes
def countNodes(root):
    if root == None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

# Create the binary tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)

# Count and display total nodes
print("Total number of nodes:", countNodes(root))