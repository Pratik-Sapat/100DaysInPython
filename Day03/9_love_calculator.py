print("Welcome to the love calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2 #to concatinate two string

lower_case_string = combined_string.lower() #change to lower case.

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love)) # we did here str bcz we just want to concatinate string. and also used int bcz we want it as integer so we can also check condition n if statement.
 

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score} , you go together like coke and mentos. ")
elif love_score >= 40 and love_score <= 50:
    print(f"your love score is {love_score} , you are alright together.")
else:
    print(f"your score is {love_score}")
