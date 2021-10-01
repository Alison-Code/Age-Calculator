yearage = int(input("What is your age/Year of birth: "))
year = 0
age = 0

if yearage < 100 and yearage > 0:
    year = 2021 - yearage
    age = yearage
    print(f"You will turn 100 in the year {year+100}(after {100-age} years)")

elif yearage > 1900 and yearage < 2021:
    year = yearage
    age = 2021 - yearage
    print(f"You will turn 100 in the year {year+100}(after {100-age} years)")

elif yearage > 100 and yearage < 150:
    print(f"You have already turn 100")

elif yearage > 2021:
    print("You are not yet born")

else:
    print("Wrong input")
