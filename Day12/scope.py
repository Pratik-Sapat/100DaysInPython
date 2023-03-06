# enemies = 1 #global scope
# def increase_enemies():
#     enemies = 2 #local scope
#     print(f"enemies inside function : {enemies}")

# increase_enemies()
# print(f"enemies outside function : {enemies}")



#there is no bock scope in python

# game_level = 3
# enemies = ["skeleton", "Zombie", "Alien"]
# if game_level<5:
#     new_enemies = enemies[0]
#     #even new_enemies is created whithin this if block still you can print it in global scope. so, new_enemies available in program.

# print(new_enemies)


#function block example.

game_level = 3
def create_enemy():
    enemies = ["skeleton", "Zombie", "Alien"]
    if game_level<5:
        new_enemies = enemies[0]
        # so now, new_enemies available in program.whithin this function.
    print("new_enemies")

# print(new_enemies) #will give error


#for loop ,while loop ,if block- not create seprate local scope for variables..