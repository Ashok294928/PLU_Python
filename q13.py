# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create the binary tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)

# Display the nodes
print("Root Node:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)