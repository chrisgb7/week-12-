list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2]
print(nested_list)
print(nested_list[1][2])
fruits =    ["apple", "orange", "banana", "coconut"]
vegetables =     ["celary", "carrot", "potatoes"]
meats =     ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]
print(groceries [2][2])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print(collection)
num_pad = ((1, 2, 3), 
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end="")
# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][1])
print(matrix[0][0])
example_list = [row[0] for row in matrix]
# for row in matrix
#       print(row[0])
print(example_list)
# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
lmatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(".")
# Print the first list.
print(lmatrix [0])
print(".")
# Print the second item from the third list.
print(lmatrix [2][1])
# Use a list comprehension to extract the last item from each sub-list.
comprehension_list = [row[0] for row in matrix]
print(comprehension_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squared_numbers = [x**2 for x in range(1,11)]
# for x in range (1,11):
#   squared = x**2
#   print(squared)
print(squared_numbers)