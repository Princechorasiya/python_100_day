import random
word_list = ["ardvark", "baboon", "camel"]
# todo randomly choose a word from word_list
# Ask the  user for to guess a letter make it lower case and assign it to variable guess.var
# check if guess is in chosen_word.
chosen_word = word_list[random.randint(0, 2)]
print(chosen_word)
guess = input("Guess a letter: ")
guess_lower = guess.lower()
print(guess_lower in chosen_word)
for item in chosen_word:
    print(guess_lower == item)


# method 2
chosen_word_1 = random.choice(word_list)
guess_1 = input("guess a letter: ")
guess_lower_1 = guess_1.lower()
for letter in chosen_word_1:
    if letter == guess_lower_1:
        print("Right")
    else:
        print("wrong")


# replacing _ with the guessed letter
word_list = word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ")
guess_lower = guess.lower()


# todo 1: create an empty list display.
# for each letter in chosen_word add _to the display


# todo 2 loop through each position in the chosen_word; if the letter mathces guess then
# reveal that letter in the display at that position
# todo -3 printdisplay and see the guessed letter in the correct position and every other letter replace with "_"
display = []
for letter in chosen_word:
    display += ["_"]
print(display)
# for i in range(len(chosen_word)):
#     if chosen_word[i] == guess_lower:
#         if chosen_word[i] == guess_lower:
#             display[i] = guess_lower
#     else:
#         pass
# print(display)
# for i in display:
#     print(i, sep=" ", end=" ")


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

chosen_word = random.choice(word_list)
# guess = input("Guess a letter: ")
# guess_lower = guess.lower()


# todo 1: create an empty list display.
# for each letter in chosen_word add _to the display


# todo 2 loop through each position in the chosen_word; if the letter mathces guess then
# reveal that letter in the display at that position
# todo -3 printdisplay and see the guessed letter in the correct position and every other letter replace with "_"

display = []
for letter in chosen_word:
    display += ["_"]
print(display)
# for i in range(len(chosen_word)):
#     if chosen_word[i] == guess_lower:
#         display[i] = guess_lower
#     else:
#         pass
# print(display)
# for i in display:
#     print(i, sep=" ", end=" ")

lives = 6
end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ")
    guess_lower = guess.lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess_lower:
                display[i] = guess_lower
    else:
        lives -= 1

    print(HANGMANPICS[6-lives])
    print(display)
    if "_" not in display and lives != 0:
        print("You win")
    elif "_" in display and lives == 0:
        print("You lost all lives.You lose.")

    if "_" not in display:
        end_of_game = True
    elif lives == 0:
        end_of_game = True


# create a vriable lives to keep track of lives set  lives to 6
# if guess is not in chosen_word thenreduce live by one.


# join all the elements in the list and print them as string

print("the word was:", chosen_word)

# check if user has got all the letters
# print the ascart from the stages of the game
