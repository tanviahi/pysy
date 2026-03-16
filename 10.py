# Create a set
my_set = {10, 20, 30, 40}

# Print the set
print("Original Set:", my_set)

# Access set elements (using loop because sets are unordered)
print("Accessing elements of set:")
for item in my_set:
    print(item)

# Update set (add new elements)
my_set.add(50)
print("After adding 50:", my_set)

# Update set with multiple elements
my_set.update([60, 70])
print("After update:", my_set)

# Remove element from set
my_set.remove(20)
print("After removing 20:", my_set)

# Delete the set
del my_set
print("Set deleted")