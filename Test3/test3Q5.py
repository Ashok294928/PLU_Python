# Step 1: Store the sorted list of book prices
book_prices = [150, 200, 250, 300, 350]

# Step 2: Display the original list
print("Book Prices:", book_prices)

# Step 3: Enter the new book price
new_price = int(input("Enter the new book price: "))

# Step 4: Find the correct position and insert
position = 0

while position < len(book_prices) and book_prices[position] < new_price:
    position += 1

book_prices.insert(position, new_price)

# Step 5: Display the updated list
print("Updated Book Prices:", book_prices)