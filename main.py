#
# country = input("What country are you from?")
# print(f"{country} is a beautiful country.")
import math


# number = 4
# for i in range(11):
#     product = number * i
#     print(f"{number} multiplied by {i} equals {product}.")

# # Exercise 1.4
# row = 1
# column = 1
# max_multiplier = 10
# for r in range(row, max_multiplier + 1):
#     products = []
#     for c in range(column, max_multiplier + 1):
#         products.append(f"{r * c}")
#
#     print("\t".join(products))

# # Exercise 1.4 Option 2
# row = 1
# column = 1
# max_multiplier = 10
# for r in range(row, max_multiplier + 1):
#     products = []
#     for c in range(column, max_multiplier + 1):
#         products.append('{:4d}'.format(r * c))
#
#     print("".join(products))


# Exercise 1.5
# dice_one_values = [1,2,3,4,5,6]
# dice_two_values = [1,2,3,4,5,6]
#
# for x in dice_one_values:
#     for y in dice_two_values:
#         print(f"({x},{y})")


# # Exercise 1.6
# def triple(x):
#     result = 3 * x
#     return result
#
# def square(x):
#     result = x**2
#     return result
#
# for i in range(1,10+1):
#     triple_result = triple(i)
#     square_result = square(i)
#     if square_result <= triple_result:
#         print(f"triple({i})=={triple_result} square({i})=={square_result}")
#     else:
#         break


# # Exercise 1.7
# def calculate_triangle_area(base,height):
#     result = (base * height) / 2
#     return result
#
# def calculate_circle_area(radius):
#     result = 3.14 * radius**2
#     return result
#
# def calculate_rectangle_area(width,height):
#     result = width * height
#     return result
#
# while True:
#     shape = input("Choose a shape (triangle, rectangle, circle): ")
#
#     if shape == "":
#         break
#     elif shape == "circle":
#         r = int(input("Give the radius of the circle: "))
#         print(calculate_circle_area(r))
#     elif shape == "triangle":
#         b = int(input("Give the base of the triangle: "))
#         h = int(input("Give the height of the triangle: "))
#         print(calculate_triangle_area(base=b, height=h))
#     elif shape == "rectangle":
#         w = int(input("Give the width of the rectangle: "))
#         h = int(input("Give the height of the rectangle: "))
#         print(calculate_rectangle_area(width=w, height=h))
#     else:
#         print("Unknown shape!")


# # Exercise 1.8
# def solve_quadratic(a, b, c):
#     solution_one = (-b + math.sqrt((b**2) - 4*a*c))/(2 * a)
#     solution_two = (-b - math.sqrt((b**2) - 4*a*c))/(2 * a)
#
#     return (solution_one, solution_two)
#
# print(solve_quadratic(1, 2,1))

# L=[11,13,22,32]
# print(L)
# L[2]=10
# print(L)
# L[1:3]=[4]
# print(len(L))


# Exercise 1.9
#
# def merge(list_one,list_two):
#     new_list = list_one + list_two
#     return new_list
#
#
# l1 = [1,3,5,7,9]
# l2 = [2,4,6,8,10]
# l3 = sorted(merge(l1,l2))
# print(l3)
# print(f"{len(l1)} + {len(l2)} = {len(l3)}")

# Exercise 1.10
# def detect_ranges(int_list):
#     int_list.sort()
#
#     new_list = []
#     i = 0
#     range_start = int_list[0]
#     range_end = int_list[0]
#     range_length = 1
#     for m in int_list:
#         if (m + 1 in int_list) and (range_length == 1):
#             range_start = m
#             range_length += 1
#         elif (m + 1 in int_list) and (range_length > 1):
#             range_length += 1
#         elif (m + 1 not in int_list) and (range_length > 1):
#             range_end = m + 1
#             new_list.append(tuple([range_start, range_end]))
#             range_length = 1
#         elif (m + 1 not in int_list) and (range_length == 1):
#             new_list.append(m)
#
#
#     return new_list
#
# print(detect_ranges([2,5,4,8,12,6,7,10,13]))

# Exercise 1.11
# def interleave (*args):
#     zip_list = []
#     for members in zip(*args):
#         zip_list.extend(members)
#     return zip_list
#
# print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))

# Exercise 1.12
# def distinct_characters(string_list):
#     result_dict = {}
#     for string in string_list:
#         result_dict.update({string: len(string)})
#
#     return result_dict
# print(distinct_characters(["check", "look", "try", "pop"]))

# Exercise 1.13
# def reverse_dictionary(old_dictionary):
#     new_dictionary = {}
#     for key, values in old_dictionary.items():
#         word_list = []
#         for value in values:
#             if value not in new_dictionary.keys():
#                 new_dictionary.update({value: [key]})
#             else:
#                 new_dictionary[value].append(key)
#
#     return new_dictionary
#
#
#
# d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
# print(reverse_dictionary(d))

# Exercise 1.14
# def find_matching(string_list,search_string):
#     results_list = []
#
#     for i, string in enumerate(string_list):
#         if search_string in string:
#             results_list.append(i)
#
#     return results_list
#
#
# print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))