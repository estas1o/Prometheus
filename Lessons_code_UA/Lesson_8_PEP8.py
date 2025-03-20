# #the fibonacci numbers
# #using for cycle
# first_number = 0
# second_number = 1
# range_fibo = 9999999
# for x in range(range_fibo):
#     if first_number < range_fibo:
#         print(first_number)
#         fibonacci = first_number + second_number
#         first_number = second_number
#         second_number = fibonacci
#     else:
#         print(f"the next number is {first_number} is out of range")
#         break

#The fibonacci numbers
#using while !
# def fibonacci_while(n: int) -> int: 
#     fib1 = 1
#     fib2 = 1
#     counter = 0
#     while counter < n - 2:
#         fib_sum = fib1 + fib2
#         fib1, fib2 = fib2, fib_sum
#         counter += 1
#     return fib2


# #Using for vol.2
# def fibonacci_for(n):
#     fib1 = fib2 = 1
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#     return fib2


#Using recursion
def fibonacci_recursion(n):
    if n in (1, 2):
        print("i'm in simply part")
        return 1
    else:
        print(f"step: ")
    return fibonacci_recursion(n -1) + fibonacci_recursion(n -2)



n_str = input("enter number you interested in: ")
n = int(n_str)
print(fibonacci_recursion(n))

