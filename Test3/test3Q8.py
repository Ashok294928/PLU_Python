# Step 1: Store the patient priority levels
priority = [2, 5, 1, 4, 3]

# Step 2: Display the original priority list
print("Original Priority List:", priority)
# Step 3: Bubble Sort (Descending Order)
n = len(priority)

for i in range(n):
    for j in range(n - i - 1):
        if priority[j] < priority[j + 1]:
            priority[j], priority[j + 1] = priority[j + 1],priority[j]
#display the sorted priority list
print("Sorted Priority List (Highest to Lowest):", priority)