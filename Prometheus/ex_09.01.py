cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)
print(cabinet['fall'])
cabinet['fall'] = cabinet['fall'] + 2
print(cabinet)

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)
for key in jjj:
    print(key, jjj[key])