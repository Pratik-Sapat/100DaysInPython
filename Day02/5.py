height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))


bmi = weight/height ** 2  # ** is power sign

bmi_as_int = int(bmi)
print(bmi_as_int)