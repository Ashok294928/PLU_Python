# Step 1: Store the list of student marks
student_marks = [45, 25, 35, 90, 100, 99]

# Step 2: Display the original list
print("List of Student Marks:", student_marks)

# Step 3: Bubble Sort
n = len(student_marks)

for i in range(n):
    for j in range(n - i - 1):
        if student_marks[j] > student_marks[j + 1]:
            student_marks[j], student_marks[j + 1] = student_marks[j + 1], student_marks[j]

# Step 4: Display the sorted list
print("List of Sorted Student Marks:", student_marks)