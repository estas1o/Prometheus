dct = dict()
tpl = list()

file_name = input("Enter file: ")
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
file_handler = open(file_name)
for line in file_handler:
    if not line.startswith("From "): continue
    line = line.rstrip()
    # print(line)
    words = line.split()
    separator = line.find(":")
    # print(separator)
    time = line[separator- 2:separator]
    # print(time)
    dct[time] = dct.get(time, 0) + 1
    # print(dct)
    # print(dct.keys())
    # print(dct.values())
    # print(dct.items())
    # here is bad sort, need to fix it 01.02.2025
for keys, values in dct.items():
    tpl.append((keys, values))
# print(f"this is dict{tpl}")
tpl = sorted(tpl)
dct = tpl
for k, v in dct:
    print(k, v)
    
    
# ffs i did it


    