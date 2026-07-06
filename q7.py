# Function to push elements into the stack
def push(stack, value):
    stack.append(value)

# Function to display the top element
def top(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# Main program
stack = []

push(stack, 5)
push(stack, 10)
push(stack, 15)
push(stack, 20)

print("Stack:", stack)

top(stack)