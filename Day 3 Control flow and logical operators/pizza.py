print("Welcome to Python Pizza Deliveries!")
size=input("What size of pizza do you want? S , M or L")
add_pepperoni=input("Do you want pepperoni?Y or N")
extra_cheese=input("Do you want exta cheese?Y or N")
bill=0

if size=="S":
    bill=15
    print("Small size pizza:$15")
elif size=="M":
    bill=20
    print("Medium size pizza:$20")
else:
    bill=25
    print("Large size pizza:25")
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
        if extra_cheese=="Y":
            bill+=1
            print(f"Your bill is {bill}.")
        else:
            bill+=0
            print(f"Your bill is {bill}.")
    if size=="M":
        bill+=3

        if extra_cheese=="Y":
            bill+=1
            print(f"Your bill is {bill}.")
        else:
            bill+=0
            print(f"Your bill is {bill}.")
    if size=="L":
        bill+=3
        if extra_cheese=="Y":
            bill+=1
            print(f"Your bill is {bill}.")
        else:
            bill+=0
            print(f"Your bill is {bill}.")
else:
    if extra_cheese=="Y":
        bill+=1
        print(f"Your bill is {bill}.")
    else:
        bill+=0
        print(f"Your bill is {bill}.")


