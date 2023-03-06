from random import randint

dice_images = ['1', '2', '3', '4', '5', '6']
# dice_num = randint[1,6]
# print(dice_images[dice_num])

#it containse both 1 and 6 in randint and list index start from 0 so it should start from 0 to 5.
#fixed bug
dice_num = randint[0,5]
print(dice_images[dice_num])