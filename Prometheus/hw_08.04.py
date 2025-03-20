file_name = input('Enter the file name: ')
file_handler = open(file_name)
lst = list()
for line in file_handler:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)

lst.sort()
print(lst)