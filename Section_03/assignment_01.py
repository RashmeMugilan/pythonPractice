# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:
def merge_lists(list1, list2):
    new_list = list1 + list2
    return new_list

list1 = ["apple", "banana", "orange"]
list2 = ["sweet", "sweetest", "tangerine"]
merged_list = merge_lists(list1, list2)
print(merged_list)

#can be done as below also
# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)
