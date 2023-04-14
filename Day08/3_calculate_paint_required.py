import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover) #to round up the result math.ceil().
    print(f"you will need {num_of_cans} cans of paint.")


test_h = int(input("Height of Wall : "))
test_w = int(input("width of Wall : "))
coverage = 5

paint_calc(height = test_h, width=test_w, cover = coverage)