hours = input("How many hours can your work per week?: ")
try:
    mult = float(hours)
except:
    mult = -1

money = input("How much money do you want to earn per hour?: ")
try:
    sal = float(money)
except:
    sal = -1

if sal > 0:    
    if mult > 0 and mult <= 40:
    
        print(f"{mult * sal}")
    elif mult > 40:
        print(f"{(( 40) * sal + (mult - 40) * sal * 1.5)}")    
    else:
        print(f'ffs man, "{hours}" is not working hours')
else:
    print(f'ffs man, "{money}" is not money') 