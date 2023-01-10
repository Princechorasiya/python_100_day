# python lists
# a list id is what you would call a data structure,assigning a variable stroing of single data.
# when storing  a grouped piece of data ,data that has some sort of connection with each other.
# example all states of usa single variable and for wanting order in your data.
# Lists   fruits=[orange,apple] # data stored in a list can have any data type,it can even have mixed data type.
# format  [1,2,3,4]
import random
# order in the list is the order of the list of elements in which want
states_of_america = ["delaware", "Pensnsylvania", "New Jersy"]
print(states_of_america[0])
# programmers start counting from 0.
# starts from back last element -0 doesn't make sense.
print(states_of_america[-1])
# changing elements in alist.
states_of_america[1] = "Pencilvania"
print(states_of_america)

# adding elements list'
states_of_america.append("Prince land")  # adds single element.
print(states_of_america)

states_of_america.extend(["Prince1 land", "Prince2 land"])
print(states_of_america)


# other functions
# list.insert(i,x)  i=position,x=input which u want to add to the list.
# list.pop([i]) i=position removes the item from list and returns it no index(i) specififed then last element.
# list.count(x) count no of times x appears in the list.
# list.reverse() reverses the elements of a list.
# list.copy Returns the shallow copy of the list.
# list.index(x) to find the index of element based on zero system.
# len(list) provides the number of elemts in a list.


# who will pay the bill.
# string.split
# converts string to list.
a = "Prince,Chorasiya,Python"  # seperated by ,
b = (a.split(","))  # seperated by ,
print(b)


# challenge
names_string = input("Give me everybody's name, seperated by a comma.")
names = names_string.split(",")
no_of_people = len(names)
no_of_people_1 = int(no_of_people-1)
b = random.randint(0, no_of_people_1)
whos_paying = names[b]
print(f"{whos_paying} is paying the bill.")

# method 2
print(random.choice(names))
# random.choice(list) for random value generation in a list.


# nested lists:
# common error Index error:list index out of range.
# print(states_of_america[6])    gives error.
num_of_states = len(states_of_america)
# print(states_of_america[nim_of_states])   gives error
print((states_of_america)[num_of_states-1])

# dirty_dozens=["Strawberries","spinach","Kale","nectarines","Apples","grapes","Peaches","Cherries","Pears","tomatoes","Celery",
#             "potatoes"]

# keep the list and create a list of vegetables and fruits.
# nested list list in a list.
fruits = ["strawberries", "nectarines", "Apples",
          "grapes", "peaches", "cherries", "pears"]
vegetables = ["Spinach", "Kale", "tomatoes", "celery", "Potatoes"]
dirty_dozens = [fruits, vegetables]
print(dirty_dozens)


# coding challenge3
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
map_1 = (f"{row1}\n{row2}\n{row3}")
position = input(
    "Where do  want to put the treasure?Enter a two digit number for coulmn and row.")
position_int = int(position)
column = (int(position[0]))
row = int(position[1])
# print(column)
# print(row)
# row1[1]="X"
# print(row1)
if row == 1:
    if column == 1:
        row1[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif column == 2:
        row1[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        row1[2] = "X"
        print(f"{row1}\n{row2}\n{row3}")
elif row == 2:
    if column == 1:
        row2[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif column == 2:
        row2[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        row2[2] = "X"
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

 # method 2
h = int(position[0])
v = int(position[1])
selected_row = map[v - 1]
selected_row[h - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")


# project build rock paper scisor.
