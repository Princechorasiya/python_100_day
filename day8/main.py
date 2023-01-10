# Create a function called greet().
# write 3 print statement inisde the function
# call the greet() and run your code.

import math as m


"""def greet():
    print("Good morning")
    print("Good afternoon")
    print("Good night")


greet()"""

# allow little variation in functions.


# def my_function(something):
# Do this
# then do this
# finally do this. something works as a variable for  the function.

# functions that allow for input
#
"""def greet_with_name(name):
    print("hello", name)
    print(f"How do you do {name}")"""


# greet_with_name("Prince")

# def my_function(something):
# something is parameter
#  $the value of the parameter entered when the fucntion is called is called argument

# positional vs keyword arguments

# positional arguments depends upon on the order of the arguments
"""def greet_with(name, location):
    print(f"hello {name}")
    print(f"weather is nice at {location}")


greet_with("prince", "delhi")

greet_with("nowhere", "prince")"""


# keyword arguments
"""def my_function(a, b, c):
    # do this with a
    # do this with b
    # do this with c
    return (a, b, c)


print(my_function(a=1, b=2, c=4))"""


# interactive code challenge
# calculate how many can of paints we need to paint a wall of given surface area


"""test_h = int(input("height of the wall: "))
test_width = int(input("width of the wall:"))
coverage = 5


def can_calculator(a, b, c):
    num_of_cans = (a*b)/c
    print("number of cans needed", m.ceil(num_of_cans))


can_calculator(a=test_h, b=test_width, c=coverage)"""


# prime number checker
"""a = int(input("Enter the number: "))"""


"""def prime_number_checker(a):
    for i in range(2, a):
        if a % i == 0:
            value = "Not a Prime number"
            break
        else:
            value = "prime number"
    print(f"the given number {a} is {value}")


prime_number_checker(a)"""


"""def prime_checker(number):
    is_prime = True
    for i in range(2,number)
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("not a prime number")"""


# project ceaser cipher
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alpha = alphabet.split()
alphabets = []
for i in range(0, 52):
    alphabets += alpha[0][i]
print(alphabets)
direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# # encrypt the function second part.

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)

#         new_position = position + shift_amount
#         new_letter = alphabets[new_position]
#         # second method duplicate the list

#         # index function gives the first index of a needed part but we cannot enter shift higher than 26.
#         # if new_position < 26:
#         #     new_letter = alphabets[new_position]
#         # else:
#         #     index = new_position % 26
#         #     new_letter = alphabets[index]
#         cipher_text += new_letter
#         print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabets.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabets[new_position]
#     print(f"The decoded text is {plain_text}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)


# combine these two functions and def ceaser()
# def ceaser(text, shift, direction):
#     message = ""
#     for letter in text:
#         position = alphabets.index(letter)
#         if direction == "encode":
#             new_position = position + shift

#         elif direction == "decode":
#             new_position = position - shift
#         message += alphabets[new_position]
#     output = f"The {direction}d message is {message}"
#     print(output)


# ceaser(text, shift, direction)
