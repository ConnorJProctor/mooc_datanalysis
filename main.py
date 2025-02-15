#
# country = input("What country are you from?")
# print(f"{country} is a beautiful country.")

# number = 4
# for i in range(11):
#     product = number * i
#     print(f"{number} multiplied by {i} equals {product}.")

# Exercise 1.4
row = 1
column = 1
max_multiplier = 10
for r in range(row, max_multiplier + 1):
    products = []
    for c in range(column, max_multiplier + 1):
        products.append(f"{r * c}")

    print("\t".join(products))




