# Function to insert an element into the queue
def enqueue(queue, item):
    queue.append(item)

# Function to display the front element
def front(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

# Main program
queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
enqueue(queue, 40)

print("Queue:", queue)

front(queue)