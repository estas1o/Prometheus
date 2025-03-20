file_name = input("Enter file:")
if len(file_name) < 1: file_name = "clown.txt"
file_handler = open(file_name)
many = dict()
for line in file_handler:
    line = line.rstrip()
    words = line.split()
    for word in words:
        many[word] = many.get(word, 0) + 1
 
biggest = None
biggest_word = None
for word, value in many.items():
    if biggest is None or value > biggest:
        biggest = value
        biggest_word = word
print(biggest_word, biggest)