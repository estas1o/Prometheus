d = {'a':10, 'c':22, 'b':1}
tmp = []
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
tmp = sorted(tmp)
print(tmp)

