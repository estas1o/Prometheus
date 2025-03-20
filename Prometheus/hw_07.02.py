# my solution to the exercise 7.2 of the book "Python for Everybody"
line_count = 0
total_spam_confidence = 0
searched_line = ('X-DSPAM-Confidence:')
file_name = input('Enter the file name: ')
try:
    file_handler = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()
for line in file_handler:
    if not line.startswith(searched_line):
        continue
    #print(line.rstrip())
    spam = searched_line.find(':')
    spam_confidence = float(line[spam + 1:]) # a
    total_spam_confidence += spam_confidence # b = a + a
    line_count += 1
print('Average spam confidence:', total_spam_confidence / line_count)
#print('Done')