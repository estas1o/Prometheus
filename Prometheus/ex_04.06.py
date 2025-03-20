def computepay(hours, money):
    if hours > 40:
        reg = money * hours
        otp = (hours - 40.0) * (money * 0.5)
        xp = reg + otp
    else:
        xp = hours * money
    return xp
hours = input("How many hours can your work per week?: ")
money = input("How much money do you want to earn per hour?: ")
try:
    mult = float(hours)
    sal = float(money)
except:
    print("Error, please enter a numeric input")
    quit()
print("Your weekly pay is: ", computepay(mult, sal))
