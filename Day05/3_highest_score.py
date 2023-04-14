#to create list via input.
student_score = input("Input a list of students scores :").split()
print(type(student_score))

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

#Don't use max/min function it's easy.
# print(max(student_score))

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is {highest_score}")

