dictionary = {
    "Bug" : "An Error",
    "Function" : "A piece of code",
    "Loop" : "action of doing something again and again."
}

# print(dictionary["Bug"])
# print(dictionary["Function"])

#adding new entry:
dictionary["Code"] = "An instruction to computer"
# print(dictionary)

#create empty dictionary
empty_dictionary = {}

#if you want to clear already exist dictionary:
# dictionary = {}


#edit item in dictionary.
dictionary["Bug"] = "a Programming Error"
# print(dictionary["Bug"])


#loop through a dictionary.

for key in dictionary:
    print(key)
    print(dictionary[key])
