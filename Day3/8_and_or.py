print("Welcome to the rollercoaster!")

height = int(input("Height in CM? "))
bill = 0
if height > 120:
    print("YOu can ride rollercoaster!")
    age = int(input("What is your age? "))

    if  age<12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    elif age>=45 and age <=55:
        print("Every thing is going to be ok.Have a Free Ride")
    else:
        bill = 12
        print("please pay $12.")
    wants_phot = input("Do you want a photo taken ? y or n")
    if wants_phot == "y":
        bill +=  3

    print(f"your final bill is ${bill}")


else:
    print("Sorry ,you have to grow taller before!")

    