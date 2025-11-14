# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#list are ordered collections of items
#list are mutable meaning you can change their content
# list are created using square brackets []
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(type(my_list)) # <class 'list'>
#insteaad of creating seperate variables
# for each item, we can store them in a list
#this makes our job easier
#when we need to manage multiple related items
#performance task maker
# print(my_list)
# print(type(my_list))
# print(my_list[0]) #access first item
# print(my_list[1:4]) #access second item
# print(my_list[0:]) # [1, 2, 3, 4, 5]
# my_list.append(6) 
# print(my_list) # [1, 2, 3, 4, 5
# my_list.extend([10,11,12,13,14]) 
# #add 500 more numbers to the list
# my_list.extend(range(15,999))
# print(my_list)
# Examples:
new_list = ['a', 'b', 'c']
print(new_list)
new_list.append('d')
print(new_list)
removed_item = new_list.pop(1)  #removes item at index 1
print(removed_item)
print(new_list)
#sortinmg the list 
numbers = [4, 2, 5, 1, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
#inserting an item at a specific positoin
# 2 10
numbers.insert(2, 101000)
print (numbers)
third_list = [7, 8, 9]
third_list[0]=6
print(third_list)
third_list[-1]
print(third_list)
import random
random_list = random.sample(range(1, 1000), 100)
print(random_list)
print(sorted(random_list))
sorted_list = sorted(random_list)
print(sorted_list)
#reverse the list
#rem,ove every third item form the list 
#summary of the list of functions
#.append(item) - adds an item to the end of the list
# .pop(index) - removes and retrurns the item at the specified index
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.