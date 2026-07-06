# Function to insert elements into the queue
def enqueue(queue, item):
    queue.append(item)

# Function to display the queue
def display(queue):
    print("Queue elements (FIFO):")
    for i in queue:
        print(i, end=" ")

# Main program
queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
enqueue(queue, 40)

display(queue)