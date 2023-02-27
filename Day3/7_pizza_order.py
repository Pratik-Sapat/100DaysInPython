print("Welcome to python pizza Deliveries!")
size = input("What size pizza do youw want? s,m or l ")
add_pepperoni = input("Dp you Want pepperoni? y or n ")
extra_cheese = input("do  you want extra cheese? y or n ")
bill=0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill +=1

print(f"your final bill is ${bill}")

