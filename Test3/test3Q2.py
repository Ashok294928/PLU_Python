product_ids = [100,120,130,140,150,160]
search =int(input("Enter a product ids:"))
# Step 3: Initialize variables
low = 0
high = len(product_ids) - 1
found = False
# Step 4: Perform Binary Search
while low <= high:
    mid = (low + high) // 2

    if product_ids[mid] == search:
        print("Product Found at Index:", mid)
        found = True
        break

    elif product_ids[mid] < search:
        low = mid + 1

    else:
        high = mid - 1
        # Step 5: If product is not found
if found == False:
    print("Product Not Available")
