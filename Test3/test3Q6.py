# Step 1: Store salaries of Branch 1
branch1 = [45000, 30000, 50000]

# Step 2: Store salaries of Branch 2
branch2 = [40000, 35000, 55000]

# Step 3: Combine both lists
all_salaries = branch1 + branch2

# Step 4: Display the combined list
print("Combined Salary List:", all_salaries)

# Step 5: Sort the salaries using Bubble Sort
n = len(all_salaries)

for i in range(n):
    for j in range(n - i - 1):
        if all_salaries[j] > all_salaries[j + 1]:
            all_salaries[j], all_salaries[j + 1] = all_salaries[j + 1], all_salaries[j]

# Step 6: Display the sorted salary list
print("Salaries in Ascending Order:", all_salaries)