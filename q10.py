# Function to insert an element into the queue
def enqueue(queue, item):
    queue.append(item)

# Function to remove an element from the front
def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Removed element:", queue.pop(0))

# Function to display the queue
def display(queue):
    print("Queue:", queue)

# Main program
queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
enqueue(queue, 40)

print("Original Queue:")
display(queue)

dequeue(queue)

print("Updated Queue:")
display(queue)