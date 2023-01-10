# scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside are{enemies}")


increase_enemies()
print(f"enemies inside are{enemies}")

# local scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# print(potion_strength) gives name error

#global scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# namespace anything u name has a namespace no such thing as block scope any thing indetned in
# loops or if are counted in global scope
# vairable created isnide a function is available only inside the function.

# modifying global scope
a = 10


def modify():
    global a
    a += 2


modify()
print(a)
# global constants
# never change
# make them uppercase
# PI = 3.14159
