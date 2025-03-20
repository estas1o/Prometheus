file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "clown.txt"
    
file_handle = open(file_name)

many = dict()

for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        many[word] = many.get(word, 0) + 1
        
# find the top 5 most common words
# print(many.items())

temp = dict()
new_list = list()
for k, v in sorted(many.items()):
    tup = (v, k)
    new_list.append(tup)

cool = sorted(new_list, reverse=True)
for v, k in cool[:5]:
    print(k, v)
   