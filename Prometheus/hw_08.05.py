
file_name = input('Enter the file name: ')
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
    
file_handler = open(file_name)
count = 0
unique_count = 0
originals = list()
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(words[1])
    count += 1
    if words[1] in originals:
        continue
    originals.append(words[1])
    for original in originals:
        unique_count += 1
        print(original)

print('There were', count, 'lines in the file with From as the first word')
print('There were', unique_count, 'unique lines in the file with From as the first word')