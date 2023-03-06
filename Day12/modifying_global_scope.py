# enemies = 1 #global scope

# def increase_enemies():
#     global enemies #in order to modify global variable inside function.
#     enemies += 1 #local scope
#     print(f"enemies inside function : {enemies}")
# increase_enemies()
# print(f"enemies outside function : {enemies}")


#avoid modifying global variable inside function.

#return it
enemies = 1 #global scope
def increase_enemies():
    print(f"enemies inside function : {enemies}")
    return enemies + 1
enemies= increase_enemies()
print(f"enemies outside function : {enemies}")


