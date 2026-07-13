# Step 1: Store the timings of participants
timings = [15.8, 12.5, 14.2, 11.9, 13.6]

# Step 2: Display the original timings
print("Original Timings:", timings)
# Step 3: Bubble Sort
n = len(timings)
for i in range(n):
    for j in range(n - i - 1):
        if timings[j] > timings[j + 1]:
            timings[j], timings[j + 1] = timings[j + 1], timings[j]

# Step 4: Display the sorted timings
print("Sorted Timings:", timings)