# my solution to the exercise 7.1 of the book "Python for Everybody"
file_name = input('Enter the file name: ')
try:
    file_handler = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()
for line in file_handler:
    big_line = line.upper()
    print(big_line.rstrip())

