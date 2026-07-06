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

# Count nodes
count = 0
temp = n1

while temp:
    count += 1
    temp = temp.next

print("Total number of nodes =", count)