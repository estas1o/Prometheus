# fhandler = open('last.txt')
# count = 0
# for line in fhandler:
#     # count += 1
#     # print('wow:', count, line)
#     # line = line.rstrip()
#     # if line.startswith('he'):
#     #     continue
#     # print(line)
#     print(line.rstrip())

file_name = input('Enter the file name: ')
try:
    fhandler = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()
    
count = 0
for line in fhandler:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', file_name)
