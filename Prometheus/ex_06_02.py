random_string = 'Monty Python'
print(random_string[0:4])
print(random_string[6:7])
print(random_string[6:20])
testing_stuff = random_string.upper()
print(testing_stuff)
print(random_string.find('t'))
print(type(random_string))
print(dir(random_string))

data = 'From votetocomeback@gmail.com Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

for letter in 'banana':
    print(letter)
    
greet = 'Hello Ivy!'
print(greet.upper())

count = 0
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
for i in data:
    print(count, i)
    count += 1
    
print(data[pos:pos+3])
print(data.strip())