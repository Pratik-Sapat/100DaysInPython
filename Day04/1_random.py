import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() #0.0000 to 0.99999..
print(random_float)

random_float = random.random() * 5  #0.0000 to 4.99999.. *5 will give till 4.99 *6 will give till 5.999
print(random_float)


love_score = random.randint(1,100)
print(f"your love score is {love_score}")
