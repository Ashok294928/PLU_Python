# Function to insert an element into the queue
def enqueue(queue, item):
    queue.append(item)

# Function to display the queue
def display(queue):
    print("Queue:", queue)

# Main program
queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
enqueue(queue, 40)

display(queue)