# 1. У реченні "Hello world" замінити всі літери "о" на "а", а літери "l" на "е". (hw do it using while)
# 2. Вивести у консоль перші 100 чисел Фібоначчі (гугол хелп!) 0 1 1 2 3 5 8 11 19 done
'''
hello = "Hello World"
print(hello)
repl = ""
for x in hello:
    if x == "o":
        repl += "a"
    elif x == "l":
        repl += "e"
    else:
        repl += x

print(repl)
'''
'''
#the fibonacci numbers
first_number = 0
second_number = 1
for x in range(100):
    if first_number < 100:
        print(first_number)
        fibonacci = first_number + second_number
        first_number = second_number
        second_number = fibonacci
    else:
        print(f"the next number is {first_number} is out of range")
        break
'''
#pycharm vs vscode

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list)
# revers = my_list[::-1]
# for x in reversed(my_list):
#     print(x)

# def divide(number1, number2):
#     if number2 != 0:
#         print(number1 / number2)
#     else:
#         print("you cant divide by 0")
#
# divide(10,20)
# divide(10,5)
# divide(10,0)

# password = input("Enter your password: ")
# if password == "1234":
#     print("access alowed")
# else:
#     print("wrong password")
# """
# Створити функцію, яка буде приймати як аргумент ім*я користувача Після чого виводитиме ("Congrats {name}")
# Викликати ф-ю декілька разів з різними аргументами
# """

# def congrats(name):
#     print(f"Congrats {name}!!!")
#
# congrats(input("enter name "))

# list_team = ["Vlod", "Skal", "Anroid","Stos","Vitalka"]
# print(list_team)
# rev = list_team[::-1]
# print(rev)

# def congrats(name):
#     print(f"Congrats, dalbaeb {name}")
    
# congrats("Dodik")
# congrats("eba")
# congrats("Android")

