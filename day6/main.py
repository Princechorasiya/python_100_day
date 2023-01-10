# functions we can get our code to perform many pieces if functionality.
# built in functions of python.(check the link in document.
# print is a function   name of a function  followed by parenthesis.
print("Hello")
len("Hello")  # because of the parenthesis we can get tha tlen is a function
# all this have been achieved by built in functions

# for starting a new function function is differnet form variable because it is followed by


def my_function():
    print("Hello")
    print("Bye")
# run the function nothing printed because we havent executed the function.


# execute the function type the name of the functon fillowed by parnthesis and the input
my_function()
# first step  def the function by def function give the name to the function followed by parenthesis
# write the set of instructions for the function.
# def my_function():
# do this
# then so this
# finally do this
# calling functions
# my_function()
# once computer sees this code it will go and carry out all the instructuions wriiten in the code
# the robot is going to perform teh task we wanted no more no less
# eg go to store and buy milk we need it give it every single instructions we have to program it each and every step
# we have to give those instructions every day
# function allow to give all these instructions in a single step.
# for n in range(0,6):
# move()
# turn_left()
# move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# turn_right()
# move()
# turn_right()
# move()
# turn_left()  code making robot reach the desired coordiante,in https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def jump():
# move()
# turn_left()
# move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# turn_right()
# move()
# turn_right()
# move()
# turn_left()
# then use for loop


# test the code step wise to avoid the errors in the program
# indentation in python:
# indented means shifted to the right by four spaces
def my_function():
    # indented by four spaces to the right we add the code to function with the same indentation.
    print("Hello")


print("World")  # not included in function
# indentation gets complicated if we have other blocks of code which are needed to be indented in the loop.
# spaces vs tabs two ways of creating indentation
# spaces are preferredd indentation format
# in python 3 you cant mix file with indentation of tab and space


# while loop the loop that will contine going till a particular condition is true.
# eg robot using while electricity while plugged in move forward.
# comparison
# for items in list:
# do something
# for number in range(a,b):
# do something


# while something_is_true
# do something repeatedly
# when something becomes false then it stops.
# in robo question
# no_of_hurdles=6
# while number_of_hurdles>0:
#  jump()
#  number_of_hurdles-=1
#  print(number_of_hurdles)

# while something_is_true:
#   #Do this
#   #then do this
#   #then do this


# Hurdle2 challenge
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
# def jump():
#  move()
#    turn_left()
# move()
#   turn_right()
#   move()
#    turn_right()
#    move()
#    turn_left()
#import random
# no_of_hurdles=random.randint(1,6)
# while no_of_hurdles>0:
#    no_of_hurdles-=1
#    jump()

# while at_goal !=True:
#    jump()
# while at_goal==False:
#   jump()
# while not at_goal():
#   jump()
#   #if i can use both loops when to use each them
"""for loop when we have to work with each elements of the content.
while loop is used when we dont care about particular elements.
while loops are dangerous we can create an infinite loop if a given condtition is always true."""

# Walls not fixed and goal also not fixed


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():

#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while at_goal() != True:  or we can write while not at_goal()

#     if wall_in_front():
#        jump()
#     else:
#         move()


# when everything is random
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():

#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while at_goal() != True:

#     if wall_in_front() and wall_on_right():
#         turn_left()
#     if wall_on_right() and front_is_clear():
#         move()
#     elif front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     if wall_in_front() and right_is_clear():
#         turn_right()
#         move()


# other method:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():

#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# # follow along the right hand side road and move along it.
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# # few cases in which robot gets into infinite loop
# # check this after day 15 debugging the problem
