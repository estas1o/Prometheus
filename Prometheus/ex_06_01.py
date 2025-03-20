word = 'prometheus'
index = 0
while index < len(word):
    letter = word[index]
    print(index, letter)
    index += 1
    
count = 0
for letter in word:
    if letter == 'e':
        count += 1
print(count)

for letter in word:
    print(letter)


for letter in word:
    if letter == 'e':
        word = word.replace('e', 'E')
        count += 1
print(word)
