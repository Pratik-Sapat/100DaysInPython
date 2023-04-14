# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() #to free up open file.

#we might forget to close the file so many developer use with.

# Read File
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#write file. #delete dataand write newly.
with open("my_file.txt", mode="w") as file:
    file.write("New text : me")

#write data. by append without delete existing data.
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text : mee2 ")
    
#create new file
with open("new_text.txt", mode="w")as file:
    file.write("Hello new file.")
