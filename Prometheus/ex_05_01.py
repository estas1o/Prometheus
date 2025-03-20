num = 0
tot = 0.0
largest = None
smallest = None
inputed_array = []
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)        
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
    inputed_array.append(fval)
    for the_num in inputed_array:
        if smallest is None:
            smallest = the_num
        elif the_num < smallest:
            smallest = the_num
        if largest is None:
            largest = the_num
        elif the_num > largest:
            largest = the_num
        
        # if largest is None:
        #     largest = the_num
        # elif the_num > largest:
        #     largest = the_num
    
# print('All Done')
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
print('you entered:', inputed_array)