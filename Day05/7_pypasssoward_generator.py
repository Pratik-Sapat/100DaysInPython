#passoword Generator Project.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welocme to PyPassword Generator")
user_choice = int(input((f"Type 1 for Custom Password Length.\nType 2 for Automatic Password Generation.\n")))

if user_choice == 1:
    nr_letters = int(input(f"How many letters would you like?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
elif user_choice == 2:
    nr_letters = random.randint(1,5)
    nr_symbols = random.randint(1,5)
    nr_numbers = random.randint(1,5)
else:
    print("You Selected Wrong Choice , Please select right choice.")

#Eazy level.

# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols) 
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# print(password)


#hard Level

password_list = []
#we can use .append and += both will work same.
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)
    
for char in range(0, nr_numbers):
    password_list += random.choice(numbers)
    
# print(password_list)
random.shuffle(password_list) #to get password in shuffle mode not in a row.
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")

#to change list to string add every char to empty string and 
# to change sring to list do split function to string.