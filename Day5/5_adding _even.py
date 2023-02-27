total = 0
for number in range(0,101,2):
    total += number
print(total)

#OR

sum = 0
for number in range(1,101):
    if number % 2 == 0:
        sum += number
print(sum)