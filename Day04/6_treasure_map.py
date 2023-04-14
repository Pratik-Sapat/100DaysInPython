row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position =  input("Where do you want to put the treasure?")

#23
horizontal = int(position[0])#2 so postion is 2-1=1
vertical = int(position[1])#3  position is 3-1 = 2


#it will get row 1
# selected_row = map[vertical-1] 
#and this will replace x in 2 place of row two
# selected_row[horizontal - 1] = "X" 


#or

map[vertical-1][horizontal - 1] = "X" 

print(f"{row1}\n{row2}\n{row3}")