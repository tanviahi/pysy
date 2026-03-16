# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# Print dictionary
print("Original Dictionary:", student)

# Access dictionary value
print("Name:", student["name"])

# Update dictionary
student["age"] = 21
student["city"] = "Pune"
print("After Update:", student)

# Delete element
del student["course"]
print("After Deleting 'course':", student)

# Looping through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# Create dictionary from list
keys = ["id", "name", "marks"]
values = [101, "Amit", 85]

new_dict = dict(zip(keys, values))
print("Dictionary created from list:", new_dict)