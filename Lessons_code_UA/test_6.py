'''
Завдання 1.
Написати функцію, яка приймає 2 аргументи - цілі числа.
Всередині функції виконується перевірка типу.
Якщо хоч одне з них не int, то повертається 1, якщо обидва int,
то рахується їх сума. Якщо сума додатня, повертається 0, якщо від'ємна,
то -1.
Завдання 2.
Написати функцію, в яку передається аргументом інша функція. Всередині
приймаючої функції зробіть вивід у консоль "Кінець виклику". Для прикладу
можете написати функцію додавання 2 чисел і передати її в приймаючу функцію.
Завдання 3.
Написати функцію, яка повертатиме результат найбільшого спільного дільника 
двох чисел, переданих у параметри.'''

# # 1.
# def task_1(a: int, b: int) -> int:
#     if isinstance(a, int) and isinstance(b, int):
#         result = 0 if (a +b) > 0 else -1
#         return result
#     else:
#         return 1
    
# print(task_1(1, 3))

# print(task_1('dd', 2))

# print(task_1(-5, 0))

# # 2.
# def task_2(**kwargs):
#     kwargs = task_1
#     print("kinec' vyklyku")
    
# task_2()       

def qq():
    print(f"this is func from test_6.py")
 