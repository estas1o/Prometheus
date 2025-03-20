import re
# file_handler = open('mbox-short.txt')
# for line in file_handler:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)

# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y)
# y = re.findall('[AEIOU]+', x)
# print(y)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)