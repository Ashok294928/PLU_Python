# Step 1: Create a list of roll numbers
roll_numbers = [101, 105, 109, 115, 120, 125]

# Step 2: Ask the user to enter the roll number
search = int(input("Enter the roll number to search: "))

# Step 3: Assume the student is not found
found = False

# Step 4: Check each roll number
for i in range(len(roll_numbers)):
    if roll_numbers[i] == search:
        print("Student Found at Position:", i + 1)
        found = True
        break

# Step 5: If not found
if found == False:
    print("Student Not Found")