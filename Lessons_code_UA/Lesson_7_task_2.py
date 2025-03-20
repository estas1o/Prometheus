a = 1

# LEGB

def square(base):
    result = base ** 2
    print(f"The square of {base} is {result}")
    
    
def cube(base):
    result = base ** 3
    print(f"The tripple of {base} is {result}")
    
square(3)
cube(9)

# from Lesson_7_test_1 import lll


# print(lll)

# var = 200
def outer_func():
    var = 100
    def inner_func():
        print(f"printing var from inner func: {var}")
        print(f"printing ")

    inner_func()
    print(f"printing from outer func: {var}")
    
outer_func()


