import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me Everybody's names,seperated with comma without space. ")
names = namesAsCSV.split(",")

#----------------Way1----------------------#
#get total number of items in list
num_items = len(names)
#generate random numbers between 0 and the last item
random_choice = random.randint(0 , num_items-1 )
person_pay = names[random_choice]
print(f"{person_pay},will pay today")

#-------------------OR-Way2-----------------#
#below two lines will also work same.

# person_pay = random.choice(names)
# print(f"{person_pay},will pay today")


