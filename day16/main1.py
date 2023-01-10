#  object oriented programming
# day 15 project goes haywire in the brain makes it difficult to find what is going on the program,
# This is procedral programming
# mainting simple realtions ehile writing a complex code.
# for example making an automated car make it into different modules. these modules can be made by different people
# and can be accesed afterwards

# Running a resturant
# REceponist
# waiter
# cook
# cleaning
# doing all this alone or hiring few people specialised in their tasks makes the work easier

# How to use oop
# three staff
# chef
# waiter
# cleaner
# manager
# model a waiter what it has and what it does:
# has these: atrributes(variables)
# is_holding_plate = True
# table_responsibele - [1, 2, 3]

# can do: methods(functions)


# def take(table, order):
#     # takes order to chef


# def take_payment(amount):
#     # add money to restuarant

# we can generate as many we want .
# waiter -class (blueprints of the waiter)0

# made from blueprints objects
# henry waiter1
# liza waiter2

# class
# Blueprint for the car functionality + data which models the car is known as class
# from these we can generate many objects

# car = CarBlueprint()
# car = objects

# CarBlueprint() = class

# object from blueprint already created turtle
# import turtle
# timmy = turtle.Turtle()
# # timmy = object
# # turtle = Module
# # Turtle() = class
# or
# import PrettyTable
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# # moving the turtle
# timmy.forward(100)
#
# my_screen = Screen()
# # my_screen = object and canvheihgt = artibute
# print(my_screen.canvheight)
# my_screen.exitonclick()

# carobject  atrributes =  speed and fuel

# accessing these atributes car.speed
# object.attributes represents speed of this car object

# using methods of the class associated with the Car
# object.function
# Learn turtle module from documentation
# python packages

# each file we create is module in itself
# package collection of many modules by different or same programmers
# Pypi find software developed by others using it in our code
from prettytable import PrettyTable
table = PrettyTable()
# object created here now using teh methods available in the class

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "water", "Fire"])

print(table)
print(table.align)
# printing thr attribute
# we can also change the attributes of the table.
table.align = "l"
# Changing the attribute
print(table)

# you go to anew country and make your clothes dirty finding dry cleaners is hell
# hotel object with dry cleaning method makes it easier. hotel.dryclean()
