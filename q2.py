class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# Link nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Create new node with 25
newNode = Node(25)

# Insert after node 20
newNode.next = n2.next
n2.next = newNode

# Display linked list
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")