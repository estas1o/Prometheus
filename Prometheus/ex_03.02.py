hours = input("How many hours can your work per week?: ")
money = input("How much money do you want to earn per hour?: ")
try:
    mult = float(hours)
    sal = float(money)
except:
    print("Error, please enter a numeric input")
    quit()
    
print(mult, sal)
if mult > 40:
    reg = sal * mult
    otp = (mult - 40.0) * (sal * 0.5)
    xp = reg + otp
else:
    xp = mult * sal
print("Your weekly pay is: ", xp)
