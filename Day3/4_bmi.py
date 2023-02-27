height = float(input("Enter your Height in m: "))
weight = int(input("Enter your weight in kg: "))

b = weight / height **2
bmi = int(b)

if bmi < 18.5:
    print(f"your bmi is {bmi} , you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi} , you are a normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi} , you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi} , you are obese.")
else:
    print(f"your bmi is {bmi} , you are clinically obese.")