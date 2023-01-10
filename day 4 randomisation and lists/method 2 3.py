row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
map_1 = (f"{row1}\n{row2}\n{row3}")
position = input(
    "Where do  want to put the treasure?Enter a two digit number for coulmn and row. ")
position_int = int(position)

h = int(position[0])
v = int(position[1])
selected_row = map[v-1]
selected_row[h-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
