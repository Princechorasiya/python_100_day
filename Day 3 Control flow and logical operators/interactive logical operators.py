lower_case="Hello World".lower()
print(lower_case)
count_of_o=lower_case.count("o")
print(count_of_o)
#
#Interactive question
print("Welcome to the love calculator!")
name1=input("What is your name?\n")
name2=input("Whats their name?\n")
name1_lower=name1.lower()
name2_lower=name2.lower()
count_of_t=(name1_lower+name2_lower).count("t")
count_of_r=(name1_lower+name2_lower).count("r")
count_of_u=(name1_lower+name2_lower).count("u")
count_of_e=(name1_lower+name2_lower).count("e")



count_of_l_2=(name2_lower+name1_lower).count("l")
count_of_o_2=(name2_lower+name1_lower).count("o")
count_of_v_2=(name2_lower+name1_lower).count("v")
count_of_e_2=(name2_lower+name1_lower).count("e")

true=count_of_t+count_of_r+count_of_u+count_of_e
love=count_of_l_2+count_of_v_2+count_of_o_2+count_of_e_2
#print(first_digit)
#print(second_digit)
score=str(true)+str(love)# for cintantion convert into strings and join with +signs
score_1=int(score)
if score_1<10 or score_1>90:
    print(f"Your love score is {score_1},you go together like coke and mentos")
elif score_1>40 and score_1<50:
    print(f"Your love score is {score_1},you are alright together")
else:
    print(f"Your love score is {score_1}")

