# debugging
# The process of removing the bugs from the code
# 1) describe the problem
# def my_function():
#     for i in range(1,20):
#         if i ==20:
#             # The above line has the bug
#             print("You got it")
# my_function()

# 2) Reproduce the bug find what value is making the problem
# from random import randint
# dic_imgs = ["a","b","c","d","e","f"]
# dic_num = randint(1,6)
# print(dic_imgs[dic_num])


# 3)Play computer run the code with values

# year = int(input("enter the age:"))
# if year>1980 and year<1994:
#     print("You are millenial")
# elif year>1994:
#     print("you are a GenZ")

# 4)Fixing the errors
# age = input("How old are:")
# if age>18:
# print("You can drive")
# two errors

# 5) print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Enter the pages:"))
# print(pages)
# words_per_page == int(input("Enter the words:"))
# print(word_per_page)
# total_words = pages*words_per_page

# debuggers
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item*2
#     b_list.append(new_item)
#     print(b_list)
# mutate[1,2,3]
# debuggers thonny or pythontutor
#  7)take a break
# ask a friend
# run your code often
# ask stackoverflow
