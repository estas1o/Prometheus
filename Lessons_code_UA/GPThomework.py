# Завдання 1: Середнє значення списку
# # Напиши програму, яка обчислює середнє значення елементів у списку.


# numbers = [1, 2, 3, 4, 5]
# # Твій код тут


# sum_all = 0
# average = 0
# for x in numbers:
#     sum_all +=x
#     average = (sum_all / (len(numbers)))
    
# # # обчислити середнє значення
# print("Середнє значення:", average)

# # done
# # ***



# # Завдання 2: Пошук максимального і мінімального значення
# # Напиши програму, яка знаходить максимальне і мінімальне значення в списку.
# # python
# # Копіювати код
# numbers = [1, 2, 3, 4, 5]
# # Твій код тут
# # cheat version:
# maximum = min(numbers) # знайти максимальне значення
# minimum = max(numbers) # знайти мінімальне значення
# # newbie version:


# # maximum = 0
# # minimum = 0

# # for x in numbers:
# #     if x < numbers[0]:
# #         minimum = numbers[0]
# #     elif x >= numbers[0]:        
# #         maximum += x
    
# print("Максимальне значення:", maximum)
# print("Мінімальне значення:", minimum)

# done
# ***



# Завдання 3: Підрахунок кількості певного елемента
# Напиши програму, яка підраховує кількість входжень заданого елемента у список.
# python
# # Копіювати код
# elements = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
# element_to_count = 'apple'
# # # Твій код тут
# # count = 0 # підрахувати кількість входжень

# # for x in elements:
# #     if x == element_to_count:
# #         print(f"here is {x}")
# #         count +=1
# #     else:
# #         print(f"{x} doesn't count")
# # count = elements.count(element_to_count)  # pro version using built in "count" method
# print(f"Елемент '{element_to_count}' зустрічається {count} разів.")

# done
# ***

# Завдання 4: Зворотний порядок списку
# Напиши програму, яка виводить список у зворотному порядку.
# python
# # # Копіювати код
# numbers = [1, 2, 3, 4, 5]
# # # Твій код тут
# # reversed_list = numbers[::-1] # "slicing" feature # перевернути список
# # +++ 2 ways of pro using methods and functions:
# # +++ method:
# # numbers.reverse()
# # print("zvorotniy spysok, using meth:", numbers)
# # +++ function:
# reversed_list = list(reversed(numbers))
# print("zvorotniy spysok, using func:", reversed_list)

# print("Зворотний список:", reversed_list)




# done
# ***



# Завдання 5: Видалення дубльованих елементів
# # Напиши програму, яка видаляє дубльовані елементи зі списку.
# # python
# # # Копіювати код
# elements = [1, 2, 2, 3, 4, 4, 5]
# # # Твій код тут
# unique_elements = 0 # видалити дубльовані елементи
# +++ my solution isn't that right
# for x in elements:
#         if x != elements:
#                 unique_elements = x
#                 print(f"{x} is unique and used once")
#         else:
#                 elements.pop(x)

# # +++ gpt explained beeter way to do this task:
# '''
# Ваш код для п'ятого завдання має деякі помилки та не вирішує завдання видалення дублікатів зі списку.
# Правильний підхід полягає в тому, щоб використовувати множину (set) для автоматичного видалення дублікатів,
# а потім перетворити її назад у список. Ось кілька способів вирішення цього завдання:


# '''
# # +++ using 'set' 
# # unique_elements = list(set(elements))
# # print("spysok bez dublikativ", unique_elements)
# # ***
# # +++ using 'for' cycle for deleting non-unique elements (the real thing is that it's not actually deleting elements, rather that creating new list with unique elements instead):
# unique_elements = []
# for x in elements:
#     if x not in unique_elements:
#         unique_elements.append(x)
                 

# print("Список без дублікатів:", unique_elements)



# # Завдання 6: Сортування списку
# # Напиши програму, яка сортує список за зростанням.
# # python
# # Копіювати код
# numbers = [5, 3, 1, 4, 2]
# # # Твій код тут
# # # # easy cheat version:
# # numbers.sort()
# # # sorted_list = numbers # відсортувати список

# # +++ buble sort !!!
# n = len(numbers)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if numbers[j] > numbers[j+1]:
#             # elements swap
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            
# sorted_list = numbers
# print("Відсортований список:", sorted_list)

''''''
# learnx.org
# here ill test some cases
''''''

# Завдання 7: Знайти другу найменшу і другу найбільшу числа у списку
# Напишіть програму, яка знаходить друге найменше і друге найбільше числа у списку.

# Підказка: Використовуйте функції sorted() та індекси.

# python
# Копіювати код
# numbers = [4, 1, 7, 3, 8, 5, 6]
# # Твій код тут

# second_smallest = # знайти друге найменше число
# second_largest = # знайти друге найбільше число

# print("Друге найменше число:", second_smallest)
# print("Друге найбільше число:", second_largest)
# Завдання 8: Об'єднати два списки без дублікатів
# Напишіть програму, яка об'єднує два списки у один, видаляючи всі дублікати.

# python
# Копіювати код
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# # Твій код тут

# combined_list = # об'єднати списки без дублікатів

# print("Об'єднаний список без дублікатів:", combined_list)
# Завдання 9: Перевірити, чи є список паліндромом
# Напишіть програму, яка перевіряє, чи є список паліндромом (тобто чи читається він однаково зліва направо і справа наліво).

# python
# Копіювати код
# numbers = [1, 2, 3, 2, 1]
# # Твій код тут

# is_palindrome = # перевірити, чи є список паліндромом

# print("Список є паліндромом:", is_palindrome)
# Завдання 10: Знайти спільні елементи у двох списках
# Напишіть програму, яка знаходить всі спільні елементи у двох списках.

# python
# Копіювати код
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# # Твій код тут

# common_elements = # знайти спільні елементи

# print("Спільні елементи:", common_elements)
# Завдання 11: Знайти найбільш часто зустрічається елемент у списку
# Напишіть програму, яка знаходить елемент, що найчастіше зустрічається у списку.

# python
# Копіювати код
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# # Твій код тут

# most_frequent = # знайти найбільш часто зустрічається елемент

# print("Найбільш часто зустрічається елемент:", most_frequent)
# Завдання 12: Знайти всі парні числа у списку
# Напишіть програму, яка знаходить всі парні числа у списку.

# python
# Копіювати код
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Твій код тут

# even_numbers = # знайти всі парні числа

# print("Парні числа:", even_numbers)

n = int(input().strip())
if n % 2 == 0:
    if n >= 2:
        print(f" 2-5: {n} is not Weird")
    elif n > 5:
        print(f" 6-20: {n} is Weird")
    elif n > 20:
        print(f" 20 + Not Weird")
else:
    print(f"else !!!: {n} is Weird")


