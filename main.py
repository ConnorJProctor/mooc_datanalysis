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


# Exercise 1.8
def solve_quadratic(a, b, c):
    solution_one = (-b + math.sqrt((b**2) - 4*a*c))/(2 * a)
    solution_two = (-b - math.sqrt((b**2) - 4*a*c))/(2 * a)

    return (solution_one, solution_two)

print(solve_quadratic(1, 2,1))