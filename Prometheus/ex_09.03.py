# # counts = dict()
# # print('Enter a line of text:')
# # line = input('')
# # words = line.split()
# # print('Words:', words)
# # print('Counting...')
# # for word in words:
# #     counts[word] = counts.get(word, 0) + 1
# # print('Counts:', counts)


file_name = input('Enter the file name: ')
counts = dict()
# added for error handling
if len(file_name) < 1: 
    file_name = 'mbox-short.txt'
try:
    file_handler = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit() 
for line in file_handler:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) 


# jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
# print(jjj)
# for key in jjj:
#     print(key, jjj[key]) # this is the same as the below for loop
# for aaa, bbb in jjj.items():# this is the same as the above for loop
#     print(aaa, bbb)

