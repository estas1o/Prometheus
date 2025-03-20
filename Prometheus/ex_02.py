country = input("Are you from EU or US? ")
floor = input("Which floor are you on? ")
if country == "US":
    us_floor = int(floor) + 1
    print("You are on floor", us_floor)
elif country == "EU":
    eu_floor = int(floor)
    print("You are on floor", eu_floor)
else:
    print("Invalid input")