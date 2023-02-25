num_char = len(input("your name? "))

# print("your name has "+num_char+" charactrs") we cannot concatinate string and integer.
print(type(num_char))

new_num_char = str(num_char) #converting int to char
print("your name has "+new_num_char+" charactrs")

