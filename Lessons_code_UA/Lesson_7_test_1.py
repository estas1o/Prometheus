a = 123
b = str(a)

print(f"type of a: {type(a)}")
print(f"type of b: {type(b)}")

c = "qwetrtu"
d = list(c)

print(d)

list_1 = []
list_2 = [None]

print(f"list_1: {bool(list_1)}")
print(f"list_2: {bool(list_2)}")

f = "wqeqwerqtqweqwe,.vbm,"
print(f"max: {max(f)}, min: {min(f)}")

# lambda arg1, arg2, ... argn: вираз, який використовує аргументи

g = lambda x, y, z: x + y * z

print(g(1, 2, 3))

l = [
    lambda x: pow(x, 0),
    lambda x: pow(x, 1),
    lambda x: pow(x, 2),
    lambda x: pow(x, 3),
    lambda x: pow(x, 4),
]

for i in l:
    print(i(5))
    
def l(x): return pow(x, 0)
def h(x): return pow(x, 1)
def t(x): return pow(x, 2)

ll = [l, h, t]

for i in ll:
    print(i(5))


