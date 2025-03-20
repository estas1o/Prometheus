# # def greet(lang):
# #     if lang == 'es':
# #         return 'Hola'
# #     elif lang == 'fr':
# #         return 'Bonjour'
# #     else:
# #         return 'Hello'
 
# # print(greet('es'),'Michael')

# # def addtwo(a, b):
# #     added = a + b
# #     return a
 
# # x = addtwo(2, 7)
# # print(x) 

# import random
# import math

# # # print(math)
# # print(math.pi)
# # text = str(math.pi)
# # print(len(text))

# # for i in range(10):
# #     x = ran()
# #     print(x)

# # # endless loop
# # def ffs():
# #     n = 1
# #     while n > 0:
# #         n = n + 1
# #         print(f"i have a dog! {n}")
        
# # ffs()

# # for i in range(random.randrange(1, 10)):
# #     # x = random.randrange(1, 10)
# #     print(i)


# largest_so_far = -1
# print('Before:', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
    
# print('After:', largest_so_far)

# zork = 0
# print('Before:', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
    
# print('After:', zork)

# total = 0
# print('Before:', total)
# for thing in [9, 41, 12, 3, 74, 15]:
#     total = total + thing
#     print(total, thing)
    
# print('After:', total)

# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large number', value)
# print('After')

# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)

# smallest_so_far = 100
# print('Before:', smallest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print(smallest_so_far, the_num)
    
# print('After:', smallest_so_far)

# smallest = None
# print('Before:')
# for value in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After:', smallest)

stuff = dict()
print(stuff.get('candy',-1))