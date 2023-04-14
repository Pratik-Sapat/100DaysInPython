#check if prettytable installed or not..

from prettytable import PrettyTable
table = PrettyTable()

#make=ing table.
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Charizard"])
table.add_column("Type", ["Electric", "Fire", "Super Fire"])

#to change table style.
#print(table.align) -> c = center , l=left, r = right
table.align = "l"

print(table)
