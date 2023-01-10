# conditional
# if/else
# if condition:
# do this
# else:
# do this


#!
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("continue")
print("Welcome to the rollercoaster")


# 2 #buying tickets ata roller coaster conditon height>=120
height = int(input("What is your  height:"))
if height >= 120:  # this doesn't include120 if u want 120 to be included in the if statement then type >=
    # this line of code lives in if statement all the statements after if
    print(" You can ride the rollercoaster!")
    # indatation are counted in if.
else:
    print("sorry,you have to grow taller to ride the rollarcoaster.!")
    # > greater than
    # <lesser than
    # >=greater than equal to.
    # <=lessser than equal to.
    # == equal to
    #!= not equal to.
    # =means assignment of value to variable == is used in if/else for equal to.


# 3
number = int(input("Which number you want to check?"))
number_1 = number % 2
if number_1 == 1:
    print(f"The given number {number} is a odd number")
else:
    print(f"The given number {number} is even number")


# 4 Rollar coaster ticket ticket costs
# age<+18 $7
# >+18$12
# Nested if else
# if condition:
    # if another_condition:   #this is already indented.
    # do this
    # else:
    # do this
height_1 = int(input("What is your height?"))
if height_1 >= 120:
    print("YOu can ride the rollarcoaster!")
    age = int(input("what is your age?"))
    if age <= 18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")


# 5 Boss comes situation goes complex
# age,12 "5$",12-18 "7$",>18"12"
# in case of more variables we use elif statement
# if condition1:
    # doA
# elif conditon3:{else if}
    # do B
# else:
#    do this
height_1 = int(input("What is your height?"))
if height_1 >= 120:
    print("YOu can ride the rollarcoaster!")
    age = int(input("what is your age?"))
    if age <= 12:
        print("Please pay 5$.")

    elif age < 18:  # we can use as many elif as we want.
        print("Please pay 7$")
    else:
        print("Please pay 12$.")


# 6 coding challenge.
height_6 = float(input("Enter the height in m:"))
weight_6 = float(input("Enter the weight in Kgs: "))
bmi = round(weight_6/(height_6**2))
print(f"Your BMI is {bmi}")
if bmi < 18.5:  # if,elif,else are group statement first check this if wrong thengoes to next one.
    print("You are underweight")
elif bmi <= 25:  # in case of values with lower limit and upper limit split them in two.here the lower limit is checked by the previous statement.
    print("You are Normal weight")
elif bmi <= 30:
    print("YOu are overweight")
elif bmi <= 35:
    print("You are obese")
else:
    print("YOu are clinically obese.")


# 7 coding challenge. #find the flow from the flowchats
year = int(input("Which year do you want to check?"))
# write  a program to find out if a given year is a leap year
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by  100
# unless the year is also evenly divisible by 400.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a leap year")
        else:
            print("This year is not a leap year.")
    else:
        print("The year is a  leap year")

else:
    print("Not a leap year.")


# rollar coster ticketing $3 extra for taking picutres.
# we are going to use multiple ifs.all conditons in multiple if are calculated while in elif one of them is calcualted.
print("welcome to the rollercoster Ride!")
height = int(input("What is your height in cm? "))

age = int(input("What is your age in years?"))
bill = 0
if height >= 120:
    print("You can ride the rollarcoaster.")
    if age <= 12:
        bill = 5
        print("Child ticket are available for 5$.")
    elif age < 18:
        bill = 7
        print("Youth thickets are available for 7$")
    else:
        bill = 12
        print("Adult tickets are available for 12$")

    wants_photo = input("Do you want a photo taken?Y or N.")
    if wants_photo == "Y":  # add 3$ to the bill
        bill += 3
    print(f"Your bill is {bill}")

else:
    print("Sorry you cant ride the rollercosternow.\nPlease come back after you grow up.")


# interactive excercise pizza deliver system.
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S , M or L")
add_pepperoni = input("Do you want pepperoni?Y or N")
extra_cheese = input("Do you want exta cheese?Y or N")
bill = 0

if size == "S":
    bill += 15
    print("Small size pizza:$15")
elif size == "M":
    bill += 20
    print("Medium size pizza:$20")
else:
    bill += 25
    print("Large size pizza:25")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is {bill}.")
        else:
            bill += 0
            print(f"Your bill is {bill}.")
    if size == "M":
        bill += 3

        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is {bill}.")
        else:
            bill += 0
            print(f"Your bill is {bill}.")
    if size == "L":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your bill is {bill}.")
        else:
            bill += 0
            print(f"Your bill is {bill}.")
else:
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is {bill}.")
    else:
        bill += 0
        print(f"Your bill is {bill}.")

 # method 2


bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
print(f"The final bill is {bill}")


# logical operators
# muliple conditions.
# and  both have to true.
a = 12
if a > 15:
    print("true")
else:
    print("false")
if a > 10 and a < 13:  # both have to true if oenis wrong it will print false
    print("true")
else:
    print("false")
# or when both are false then it becomes false else its always true.
# not reverses the condition.so if the condition is false it reverses it to true.
if not a > 15:
    print("true")
else:
    print("false")

# roller coster problem for everyone having mid life crisis give them free tickets.
# mid life crisis:aged 45-55
print("welcome to the rollercoster Ride!")
height = int(input("What is your height in cm? "))

age = int(input("What is your age in years?"))
bill = 0
if height >= 120:
    print("You can ride the rollarcoaster.")
    if age <= 12:
        bill = 5
        print("Child ticket are available for 5$.")
    elif age < 18:
        bill = 7
        print("Youth thickets are available for 7$")
    elif age > 45 and age < 55:
        print("Everything is going to be okay.Have a free ride with us.")
    else:
        bill = 12
        print("Adult tickets are available for 12$")

    wants_photo = input("Do you want a photo taken?Y or N.")
    if wants_photo == "Y":  # add 3$ to the bill
        bill += 3
    if age > 45 and age < 55:
        bill = 3
    print(f"Your bill is {bill}")

else:
    print("Sorry you cant ride the rollercosternow.\nPlease come back after you grow up.")


# interactive probelm love calculator count the no oftimes t r u e occurs in both names
# count the no of time l o v e occurs in both names concantate them adn its the score.
# print it along with conditional statemnet
lower_case = "Hello World".lower()
print(lower_case)
count_of_o = lower_case.count("o")
print(count_of_o)
#
# Interactive question
print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("Whats their name?\n")
name1_lower = name1.lower()
name2_lower = name2.lower()
# combine name1 and name 2 stirngs in the begining to shorten the code.
count_of_t = (name1_lower+name2_lower).count("t")
count_of_r = (name1_lower+name2_lower).count("r")
count_of_u = (name1_lower+name2_lower).count("u")
count_of_e = (name1_lower+name2_lower).count("e")


count_of_l_2 = (name2_lower+name1_lower).count("l")
count_of_o_2 = (name2_lower+name1_lower).count("o")
count_of_v_2 = (name2_lower+name1_lower).count("v")
count_of_e_2 = (name2_lower+name1_lower).count("e")

true = count_of_t+count_of_r+count_of_u+count_of_e
love = count_of_l_2+count_of_v_2+count_of_o_2+count_of_e_2
# print(first_digit)
# print(second_digit)
# for cintantion convert into strings and join with +signs
score = str(true)+str(love)
score_1 = int(score)
if (score_1 < 10) or (score_1 > 90):
    print(f"Your love score is {score_1},you go together like coke and mentos")
elif score_1 > 40 and score_1 < 50:
    print(f"Your love score is {score_1},you are alright together")
else:
    print(f"Your love score is {score_1}")


# project day3
print('''
************************************************************************
          |                   |                  |                     |
 ___|_____.="";=._____|_______|__
|                   |  ,-"_,=""     `"=.|                  |
|______|"=._o`"-.        `"=._____|______
          |                `"=.o`"=.      `"=.                     |
 ___|_______:=.o "=..".-="'"=.______|__
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|______|."  ,. .` ` `` ,  `"-."-._   ". '_|______
          |           |o`"=.` , "` `; .". ,  "-."-._; ;              |
 ___|____| ;`-.o`"=.; ." ` '`."\` . "-._ /_____|___
|                   | |o;    `"-.o`"=.``  '` " ,_.--o;   |
|______|| ;     (#) `-.o `"=.`.--"_o.-; ;_|______
_/__/__/_|o;.    "      `".o|o_.--"    ;o;_/__/__/_
/__/__/__/"=._o--.        ; | ;        ; ;/__/__/__/_
_/__/__/__/"=._o--.   ;o|o;     .;o;_/__/__/_
/__/__/__/__/_"=._o.; | ;.--"o.--"/__/__/__/_
_/__/__/__/__/_"=.o|o.--""_/__/__/__/__
/__/__/__/__/__/__/__/__/__/__/___ /
**************************************************************************
''')
print("Welcome to the Treasure island")
print("Your mission is to find the treasure")
choice1 = input(
    "You are at a cross road.\nWhere do you want to go?Type \"left\" or \"right\"\n")
if choice1 == "left":
    choice2 = input(
        "You came at a lake.\nThere is an island in the middle of the lake.\nType \"wait\" to wait for the boat.Type\"swim\" to swim across\n ")
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the island safely.\nThere is a house on the island with 3 doors.\none red,one yellow and one blue.Which one do you choose?\n")
        if choice3 == "blue":
            print("Congratulation, you have found the treasure")
        elif choice3 == "yellow":
            print("You have arrived at the room filled with snake.You died.\"Game over\"")
        else:
            print(
                "You arrived at a room filled with fire. You have been burned to death. \"Game over\"")
    else:
        print("You choose to swim in the lake.\nThe lake was filled with crocodiles.You have been eatan alive.\"Game over\"")

else:
    print("You walked about a mile,but didn't find anything.\n You choose to return but suddenly someone attacked you.\n You died of an heart attack due to fear \"Game over\"")
