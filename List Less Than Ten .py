# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# 1. Instead of printing the elements one by one, make a new list that
# has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only
#  elements from the original list a that are smaller than that number given by the user.

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# list_2 = []
# list_3 = []
# for number in list:
#     if number < 5:
#         print(number)
#         list_2.append(number)
# print(list_2)
# ask_num= int(input("Enter a number"))
# for number in list:
#     if number < ask_num:
#         print(number)
#         list_3.append(number)
#
# print(list_3)

  # single line code
print([number for number in list if number<5])
limit = int(input('Enter a number'))
print([number for number in list if number <limit])