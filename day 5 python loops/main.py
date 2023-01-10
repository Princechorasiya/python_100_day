# LOOPS THINGS HAPPENING OVER AND AGAIN.
# 1 FOR LOOP CAN BE USED EASILY WITH LIST.bY USING FOR LOOP WE CAN PERFORM SOME ACTIONS WITH EVERY INDIVIDUAL ELEMENT
# OF THE LOOP.
# for item in list_of_items:
#  #Do something to each item

import random
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    # we can do many things inside for loop
    print(fruit+"pie")
    # if indented the instructins are carried as amany times as the for loop need to repeat.
    print(fruits)
print(fruits)  # not included in the loop as it is not intended.


punishment = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
punishment_1 = punishment+punishment
for element in punishment_1:
    print("This is your punishment")


#
# coding challenge1
student_heights = input(
    "Enter the list of the heights of the students").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# len(student_heights) for total no of inputs
# sum(student_heights) or sum of all inputs


total_height = 0
for height in student_heights:  # we can call height as anything as long as we are consistent
    total_height += height
print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height/number_of_students)
print(average_height)


# coding challenge
student_scores = input("Input a list of students scores:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# max(student_scores) for max in alist
# min(student_scores) for min in a list.
# no_of_students=0
# for mark in student_scores:
#  no_of_students+=1
# print(no_of_students)
# marks_total=0
# for mark in student_scores:
#   marks_total+=mark
# print(marks_total)
# for mark in student_scores:
#    if mark*no_of_students>marks_total
#                  if mark


# solution:
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class:{highest_score}")

lowest_score = highest_score
for score in student_scores:
    if lowest_score > score:
        lowest_score = score
print(lowest_score)


# we have been using for loops for lists other uses.
# using for loops with range function
# for number in range(a,b) and b is not included while a is included in the range.
# print(number)

for number in range(1, 10):
    print(number)

for number in range(0, 11):
    print(number)


# 3 is step can be any number for what increament in values we want.
for number in range(0, 11, 3):
    print(number)

# calculate 1+2+3+4+...+100
total = 0
for number in range(1, 101):
    total += number
print(total)


# coding challenge
total = 1
for number in range(2, 101, 2):
    total += number
print(total)

total_1 = 1
for number in range(1, 101):
    if number % 2 == 0:
        total_1 += number

print(total_1)


# fizz buzz challenge
# fizz buzz challenge
outspoken = 0
for number in range(1, 101):
    outspoken = number
    if outspoken % 3 == 0:
        if outspoken % 5 == 0:
            number = "fizz buzz"
        else:
            number = "fizz"
    if outspoken % 5 == 0 and outspoken % 3 != 0:
        number = "buzz"
    print(number)

# method 2
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = "fizzbuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "buzz"
    else:
        number = number
    print(number)


# project 5
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = ""
for n in range(1, nr_letters+1):

    letter_1 = letters[random.randint(0, 51)]
    letter += letter_1
# print(letter)
number = str()
for n in range(1, nr_numbers+1):
    number_1 = numbers[random.randint(0, 9)]
    number += str(number_1)
# print(number)
symbol = str()
for n in range(1, nr_symbols+1):
    symbol_1 = symbols[random.randint(0, 8)]
    symbol += symbol_1
# print(symbol)

print(f"Your password is {letter}{number}{symbol}")

# adding integers to a string is not possible.


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list2 = [[letter], [symbol], [number]]
# print(list2)
# print(list2[1][0][1])
# print(list2[2])
letter_individual_list = []
for n in range(1, nr_letters+1):
    letter_individual = list2[0][0][n-1]
    letter_individual_list += [letter_individual]
# print(letter_individual_list)
number_individual_list = []
symbol_individual_list = []
for q in range(1, nr_numbers+1):
    number_individual = list2[2][0][q-1]
    number_individual_list += number_individual

for r in range(1, nr_symbols+1):
    symbol_individual = list2[1][0][r-1]
    symbol_individual_list += symbol_individual
# print(number_individual_list)
# print(symbol_individual_list)
list3 = letter_individual_list+number_individual_list+symbol_individual_list
# print(list3)
password = str()
for n in range(1, len(list3)+1):
    random_index = random.randrange(len(list3))
    password_1 = list3.pop(random_index)
    password += password_1

print(f"Your password is {password}")


# easy level
password = ""
for char in range(1, nr_letters+1):
    password += random.choice(letters)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)
print(password)

# hard level
password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is:{password}")
