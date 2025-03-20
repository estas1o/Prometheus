abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
word = len(stuff[0])
print(word)
for w in stuff:
    for l in w:
        print(l)
        
        
        
file_handler = open('mbox-short.txt')
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    pieces = words[1].split('@')
    print('done')
    
    