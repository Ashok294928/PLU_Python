# Step 1: Store the players' scores
scores = [250, 500, 150, 400, 300]

# Step 2: Display the original scores
print("Original Scores:", scores)

# Step 3: Bubble Sort (Descending Order)
n = len(scores)

for i in range(n):
    for j in range(n - i - 1):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

# Step 4: Display the leaderboard
print("Leaderboard (Highest to Lowest):", scores)