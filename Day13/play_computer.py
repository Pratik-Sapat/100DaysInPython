#read your code and understand it.

year = int(input("your year of birth? "))
# if year > 1980 and year < 1994:
#     print("you are a millenial")
# elif year > 1994:
#     print("you are a Gen Z.")


# if we enter 1994 then it will print nothing bcz of condition.

#just change one of condition to >=
#fixed code.

if year > 1980 and year < 1994:
    print("you are a millenial")
elif year >= 1994:
    print("you are a Gen Z.")