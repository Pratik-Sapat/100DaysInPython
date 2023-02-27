print("Welcome to the rollercoaster!")

height = int(input("Height in CM? "))

if height > 120:
    print("YOu can ride rollercoaster!")
    age = int(input("What is your age? "))

    if  age<12:
        print("Please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry ,you have to grow taller before!")

    