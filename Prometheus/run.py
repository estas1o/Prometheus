# x = 5
# if x > 2:
#     print("Bigger than 2")
#     print("Still bigger")
# print("Done with 2")
# for i in range(5):
#     print(i)
#     if i > 2:
#         print("Bigger than 2")
#     print(f"Done with {i}")
# print("All done")



astr = "Hello Bob"
try:
    istr  = int(astr)
except:
    istr = -1 # means ERROR
    
print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1 # means ERROR

print("Second", istr)



# astr = "Bob"
# try:
#     print("Hello")
#     istr = int(astr)
#     print("There")
# except:
#     istr = -1 # means ERROR
    
# print("Done", istr)



# rawstr = input("Enter a number: ")
# try:
#     ival = int(rawstr)
# except:
#     ival = -1 # means ERROR (idk but it seems like "-1" equals to red flag:D)
    
# if ival > 0:
#     print("Nice work")
# else:
#     print(f'"{rawstr}" is not a number')


# *** random HW solutions
# x = 0
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')

# x = -22
# if x < 2 :
#     print('Below 2')
# elif x >= 2 :
#      print('Two or more')
# else :
#     print('Something else')

# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1
    
# print(istr)



# *** my solution

# hours = input("How many hours can your work per week?: ")
# try:
#     mult = float(hours)
# except:
#     mult = -1

# money = input("How much money do you want to earn per hour?: ")
# try:
#     sal = float(money)
# except:
#     sal = -1

# if sal > 0:    
#     if mult > 0 and mult <= 40:
    
#         print(f"Your salary would be: {mult * sal} per week")
#     elif mult > 40:
#         print(f"Your salary would be: {(( 40) * sal + (mult - 40) * sal * 1.5)} per week")    
#     else:
#         print(f'ffs man, "{hours}" is not working hours')
# else:
#     print(f'ffs man, "{money}" is not money') 


# *** BETTER SOLUTION (pretty optimized)

# hours = input("How many hours can your work per week?: ")
# money = input("How much money do you want to earn per hour?: ")
# try:
#     mult = float(hours)
#     sal = float(money)
# except:
#     print("Error, please enter numeric input")
#     quit()
    
# # print(mult, sal)
# if mult > 40:
#     ok_working_hours = mult * sal
#     overtimed_working_hours = (mult - 40.0) * (sal * 0.5)
#     total = ok_working_hours + overtimed_working_hours
# else:
#     total = mult * sal
# print(f"Your salary would be: {total} per week")



# 3.3

# score = input("Enter score: ")
# try:
#     ok_score = float(score)
# except:
#     print("Error, please enter numeric input")
#     quit()
# if ok_score >= 0 and ok_score <= 1:
#     if ok_score >= 0.9:
#         print('A')
#     elif ok_score >= 0.8:
#         print(f'B')
#     elif ok_score >= 0.7:
#         print(f'C')
#     elif ok_score >= 0.6:
#         print(f'D')
#     elif ok_score < 0.6:
#         print(f'F')
# else:
#     print(f'Out of range')


# def addtwo(a, b):
#     added = a + b
#     return a

# x = addtwo(2, 7)
# print(x)


