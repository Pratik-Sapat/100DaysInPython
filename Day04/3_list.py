#list indexing start from 0 and size is always len-1.
states_of_america = ["Delaware", "Pennsylvania", "new Jersey", "Texas", "Utah","New Mexico"]

print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "pencilvania"

states_of_america.append("Patriotic")

states_of_america.extend(["Maha", "UP" , "Delhi"]) #to add another list or append all items

print(states_of_america)

