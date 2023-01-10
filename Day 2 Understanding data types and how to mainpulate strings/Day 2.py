# len used to count no of letters in a string.
# print(len(2)) counts as error
# Data types
# 1)strings
print("Hello"[0])
# start count from zero
print("Hello"[2])
"123"
# it is treated as a string not a number
print("123" + "345")
# 2)Integer
print(123 + 345)
# to define integer just write the number
print(123_456_789)  # large numbers like 123,456,789 replace , by _.
# 3) FLoat 9floating point number)
print(3.14)
# 4) Boolean
True
False
two_digit_number = input("Enter the value: ")
print(type(two_digit_number))
# data type is string conver it into integer data type.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)
# Data conversion.
# len(2345)#gives a type error
# below two codes gives error {type error} len gives int data type output.
num_char = len(input("whats your name?"))
# print("your name has"+num_char+"characters")
print(type(num_char))
# Adding string to a number doesnt makes sense
# type conversion/type casting
new_num_char = str(num_char)
print("Your name has" + " " + new_num_char + " " + "characters.")
a = 123
print(type(a))
b = str(123)
print(type(b))
c = float(123)
print(type(c))
print(20 + float("100.5"))
# str is converted to float and then added to 20
print(str(70) + str(100))
# contanation of two strings
two_digit_number_1 = input("Enter the value:")
print(type(two_digit_number_1))
first_digit_1 = int(two_digit_number_1[0])
second_digit_1 = int(two_digit_number_1[1])
print(first_digit_1)
print(second_digit_1)
result = first_digit_1 + second_digit_1
print(result)
# Mathametical operaators
print(7 - 3)  # subtraction
print(4 * 5)  # multiplication
print(type(6 / 3))  # divison gives output in float
print(3 ** 4)  # exponents
print(6 % 4)  # gives the modulus
# multiple operations in a single line
# Priority oder PEMDAS [parentheses>exponents>multiplication>division>Addition>subtraction]
# ()
# **
# */
# +-
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(3 + 3 - 3 * 3 / 3)
# Bmi calculator
height = input("enter your heightin m: ")
weight = input("enter your weight in kg: ")
B_M_I = int(weight) / (float(height) ** 2)
new_B_M_I = int(B_M_I)
new_B_M_I_1 = str(new_B_M_I)
print("YOur BMI is" + " " + new_B_M_I_1)
# number manipulation and f-stirngs
print(int(8 / 3))
# for round off
print(round(8 / 3))
print(round(8 / 3, 2))  # for rounding off two digits
print(8 // 3)  # chooping of the numbers after the decimal palce
print(type(8 // 3))
# repeated operations
result = 4 / 2
result /= 4
print(result)
score = 0
# user scores a point
score += 1
sub = 45
print(score)
sub -= 1
print(sub)
sub *= 3
print(sub)
sub **= 2
print(sub)
score_1 = 23
print("Your score is" + str(score))
score_2 = 45
height_1 = 1.4
isWinning = True
# f-string
print(f"your score is{score_2}")
# print(f"your score is{score_2},your height is{height_1},you are winning {is winning}")
print(f"your height is {height_1}")
print(f"you are winning {isWinning}")
print(
    f"Your score is {score_2},Your height is {height_1},you are winning {isWinning}")
print(
    f"Your score is {score_2},your height is {height_1},you are winning {isWinning}")
# while writing f-string write the content then write print afterwards.
f_string = f"your score is {score_2}"
print(f_string)
print(
    f"YOuir score is {score_2},YOur height is {height_1},you are winning {isWinning}")
# excercise part
age = input("What is your age?")
print(type(age))
no_of_days_left = 90*365-int(age)*365
no_of_years_left = 90-int(age)
no_of_weeks_left = 90*52-int(age)*52
print(
    f"You have {no_of_days_left} days,{no_of_weeks_left} weeks,{no_of_years_left}years left")
# use f-string in following way to prevent errors.f-string is used to combine two differnet types of data types.
message = f"You have {no_of_years_left}years,{no_of_weeks_left} weeks,{no_of_years_left}days left"
print(message)


# project
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?$")
split_btw = input("How many people to split the bill?")
percentage_of_tip = input(
    "What percentage tip would you like to give? 10,12, or 15?")
percentage_of_tip_1 = int(percentage_of_tip)/100
tip = float(total_bill)*percentage_of_tip_1
tip_1 = f"Tip tp pay is:${tip}"
print(tip_1)
total = eval(total_bill)+tip
total_per_person = round(float(total)/int(split_btw), 2)
bill = f"Each person should pay:${total_per_person}"
print(bill)
