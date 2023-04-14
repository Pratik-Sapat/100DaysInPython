students_height = input("Input a list of students heights ").split() #it will create list directly.
# print(students_height)

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])

print(students_height)

#don't use sum and len function bcz its easier to calculate using sum.
# print(len(students_height))
# print(sum(students_height))

total_height = 0
for height in students_height:
    total_height += height
# print(total_height)

number_of_students = 0
for students in students_height:
    number_of_students += 1
# print(number_of_students)

average = round(total_height/number_of_students)
print(f"Average hright of students is {average}")