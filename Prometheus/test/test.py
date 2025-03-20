file_name = input("Enter file:")
if len(file_name) < 1: file_name = "mbox-short.txt"
try:
    file_handle = open(file_name)
except:
    print("File not found")
    quit()
count = dict()
biggest = None
biggest_email = None
for line in file_handle:
    if not line.startswith("From "): continue
    words = line.split()
    email = words[1]
    count[email] = count.get(email, 0) + 1
    
for email, value in count.items():
    if biggest is None or value > biggest:
        biggest = value
        biggest_email = email
print(biggest_email, biggest)