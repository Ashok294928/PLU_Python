# Function to check if stack is empty
def isEmpty(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")

# Main program
stack = []

# Push elements
stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

# Check the stack
isEmpty(stack)