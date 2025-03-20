# basic list comprehensions

# # 1
# long version of list comprehensions

# values = []
# for x in range(10):
#     values.append(x)
# print(values)

# pro version:

# values = [x for x in range(10)] # creating list of values in range 10
# print(values)


# # 2
# comprehension condition

# evens = []
# for number in range(50):
#     is_even = number % 2 == 0
#     if is_even:
#         evens.append(number)
        
# print(evens)

# # pro version:

# evens = [number for number in range(50) if number % 2 == 0]
# print(evens)


# # 3
# comprehension with multiple condition

# options = ["any", "albany", "apple", "world", "hello", ""]
# valid_strings = []

# for string in options:
#     if len(string) <= 1:
#         continue
    
#     if string[0] != "a":
#         continue
    
#     if string[-1] != "y":
#         continue
    
#     valid_strings.append(string)
    
# print(valid_strings)

# # pro version:

# valid_strings = [
#     string
#     for string in options
#     if len(string) >= 2
#     if string[0] == "a"
#     if string[-1] == "y"
# ]

# print(valid_strings)


# # 4
# multiple (nested) list comprehensions:

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = []

# for row in matrix:
#     for num in row:
#         flattened.append(num)
        
# print(matrix)
# print(flattened)

# # pro version:

# flattened = [num for row in matrix for num in row]
# print(matrix)
# print(flattened)


# # 5
# if/else in a comprehension
# categorize numbers as even or odd

# categories = []

# for number in range(10):
#     if number % 2 == 0:
#         categories.append(f"{number}: Even")
#     else:
#         categories.append(f"{number}: Odd")
        
# print(categories)

# # # pro version:

# categories = [
#     "Even" if x % 2 == 0 else "Odd" for x in range(10)
# ]

# print(categories)


# # 6
# building a 3D list (now it's tought for me)

# import pprint

# printer = pprint.PrettyPrinter()

# lst = []

# for a in range(5):
#     l1 = []
#     for b in range(5):
#         l2 = []
#         for num in range(5):
#             l2.append(num)
#         l1.append(l2)
#     lst.append(l1)
    
# printer.pprint(lst)
# print("")
# print(" * ** *** ** *")

# # pro version

# lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
# printer.pprint(lst)


# # 7
# list comp with functions
# transformation in comprehensions

# def square(x):
#     return x**2

# print(square(9))

# squared_numbers = [square(x) for x in range(10)]

# print(square)


# # 8
# dictionary comprehension
# creating a dictionary

# pairs = [("a", 1), ("b", 2), ("c", 3)]

# my_dict = {k: v for k, v in pairs}
# print(my_dict)


# # 9
# set comprehensions
# removing duplicates from a list while applying a function

# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# unique_squares = {x**2 for x in nums}
# print(unique_squares)


# # 10
# generator comprehension

# sum_of_squares = sum(x**2 for x in range(100))
# print(sum_of_squares)