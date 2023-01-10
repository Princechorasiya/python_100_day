#who will pay the bill.
#string.split
#converts string to list.
a="Prince,Chorasiya,Python"
b=(a.split(","))
print(b)


#challenge
import random
names_string=input("Give me everybody's name, seperated by a comma.")
names=names_string.split(",")
no_of_people=len(names)
no_of_people_1=int(no_of_people-1)
b=random.randint(0,no_of_people_1)
whos_paying=names[b]
print(f"{whos_paying} is paying the bill.")

#method2
print(random.choice(names))



#coding challenge3
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
map_1=(f"{row1}\n{row2}\n{row3}")
position=input("Where do  want to put the treasure?Enter a two digit number for coulmn and row.")
position_int=int(position)
column=(int(position[0]))
row=int(position[1])
print(column)
print(row)
#row1[1]="X"
#print(row1)
if row==1:
    if column==1:
        row1[0]="X"
        print(f"{row1}\n{row2}\n{row3}")
    elif column==2:
        row1[1]="X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        row1[2]="X"
        print(f"{row1}\n{row2}\n{row3}")
elif row==2:
    if column==1:
        row2[0]="X"
        print(f"{row1}\n{row2}\n{row3}")
    elif column==2:
        row2[1]="X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        row2[2]="X"
        print(f"{row1}\n{row2}\n{row3}")
else:
    if column == 1:
        row3[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif column == 2:
        row3[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        row3[2] = "X"
        print(f"{row1}\n{row2}\n{row3}")






