# randomisation and pythons lists

# Randomisation:useful when we want to create programs with certain degree of unpredictiablity.
# eg games.
# computer are deterministic:perform repeatable tasks in a fully predictable manner.
# pyhton uses Mersenne twister pseudo number generator.
# python already has random module.
import random as rd
import random
#import module1

random_integer = random.randint(1, 10)
# generating random integers   randint
print(random_integer)

# module
# split the lagre  code into individual module responsible for particular a part/action
# like when builidng a car we produce different parts at different palces.
# large project we can collabrate with differnet people creating different modules.
# Random module for randomisation.
# to create a module create a new file other than main file
# print(module1.pi) #importing the module.
# print(module1.a)
# this is also how random module works.
# random floating point number
random_float = random.random()  # this generates random float btw 0 and 1.
print(random_float)
# for floating numbers btw 0 and 5
random_float_btw_0to5 = random.uniform(0, 5)
print(random_float_btw_0to5)
random_float_btw_0to5_1 = random_float*5  # 0.0000 to 4.999999....
print(random_float_btw_0to5_1)

# love_score lastday.
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


# randrange(start,stop,step) reurns a randomly selected integer from randrange(start,stop,step) value error if start>stop.
a = random.randrange(2, 10, 2)
# step defines the incremental
print(a)
b = random.randrange(2, 10, 3)
print(b)


# code challenge
# virtual coin toss "heads" and "tails"
random_number = rd.randint(1, 2)
print("welcome to the coin toss.Please toss the coin")
if random_number == 1:
    print("Heads")
else:
    print("tails")


# python lists
# a list id is what you would call a data structure,assigning a variable stroing of single data.
# when storing  a grouped piece of data ,data that has some sort of connection with each other.
# example all states of usa single variable and for wanting order in your data.
# Lists   fruits=[orange,apple] # data stored in a list can have any data type,it can even have mixed data type.
# format  [1,2,3,4]
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
# len(list) provides the number of elements in a list.
# list.remove() to remove the element from the list. may not work.


# who will pay the bill.
# string.split
# converts string to list.
a = "Prince,Chorasiya,Python"  # seperated by ,
b = (a.split(","))  # seperated by ,
print(b)


# challenge
names_string = input("Give me everybody's name, separated by a comma.")
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


# project build rock paper scissor.
print("Welcome to rock,paper,scissors game")
move_player = input(
    "What do you choose?Type 0 for Rock,1 for paper or 2 for scissors.")
move_1 = int(move_player)
rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

scissors = '''
    ___
---'   _________)
          ________)
          ___)
         ___)
---.____)
'''

paper = '''
    _____)
---'   _________)
          _______)
       _________)
      (______)
---.______)
'''
player_move = [rock, paper, scissors]
if move_1 <= 2 and move_1 >= 0:
    player_move_1 = player_move[move_1]
    print(f"You have chosen {player_move_1}")
    computer_move = [rock, paper, scissors]
    random_number = random.randint(0, 2)
    move = computer_move[random_number]
    print(f"Computer chose {move}")

    if move_1 == random_number:
        print("The game is a Draw")
    if move_1 == 0:
        if move == paper:
            print("You lose")
        elif move == scissors:
            print("You win")

    if move_1 == 1:
        if move == rock:
            print("You win")
        elif move == scissors:
            print("You lose")
    if move_1 == 2:
        if move == rock:
            print("You lose")
        elif move == paper:
            print("you win")

else:
    print("you have chosen wrong number")


# method2
game_images = [rock, paper, scissors]
user_choice = input(
    "What do you  want to choose?Type 0 for rock,1 for paper and 2 for scissors.\n")
user_choice_1 = int(user_choice)
if user_choice_1 <= 2 and user_choice_1 >= 0:
    print(f"You chose\n {game_images[user_choice_1]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer choose\n {game_images[computer_choice]}")
    if user_choice_1 == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice_1 == 2:
        print("You lose")
    elif user_choice_1 >= 3 or computer_choice < 0:
        print("you typed an invalid number,you lose")
    elif computer_choice > user_choice_1:
        print("You lose")
    elif user_choice_1 > computer_choice:
        print("You win")
    elif computer_choice == user_choice_1:
        print("This is a draw")
else:
    print("you chose an invalid number.You lose")
