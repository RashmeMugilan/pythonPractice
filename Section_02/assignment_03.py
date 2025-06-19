ra# Assignment 3:
"""
There is a list shown below titled original_list.

Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.

IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

# your code below:
# we cannot use sort() in a tuple, so first create it as a List, sort it and again create a new tuple with the sorted elements
tup1 = original_list[3][0]
tup2 = original_list[3][1]
tup3 = original_list[3][2]
new_list = [tup1, tup2, tup3]
new_list.sort()
new_tuple = (new_list[0], new_list[1], new_list[2])
new_list = [original_list[0], original_list[1], original_list[2], new_tuple]
print(new_list)
