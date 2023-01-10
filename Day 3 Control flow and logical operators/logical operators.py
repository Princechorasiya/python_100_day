# logical operators
#muliple conditions.
#and  both have to true.
a=12
if a>15:
     print("true")
else:
    print("false")
if a>10and a<13:#both have to true if oenis wrong it will print false
    print("true")
else:
    print("false")
#or when both are false then it becomes false else its always true.
#not reverses the condition.so if the condition is false it reverses it to true.
if not a>15:
    print("true")
else:
    print("false")

# roller coster problem for everyone having mid life crisis give them free tickets.
#mid life crisis:aged 45-55
print("welcome to the rollercoster Ride!")
height=int(input("What is your height in cm? "))

age=int(input("What is your age in years?"))
bill=0
if height>=120:
    print("You can ride the rollarcoaster.")
    if age<=12:
        bill=5
        print("Child ticket are available for 5$.")
    elif age<18:
        bill=7
        print("Youth thickets are available for 7$")
    elif age>45 and age<55:
        print("Everything is going to be okay.Have a free ride with us.")
    else:
        bill=12
        print("Adult tickets are available for 12$")

    wants_photo=input("Do you want a photo taken?Y or N.")
    if wants_photo=="Y":#add 3$ to the bill
        bill+=3
    if age>45 and age<55:
         bill=3
    print(f"Your bill is {bill}")

else:
    print("Sorry you cant ride the rollercosternow.\nPlease come back after you grow up.")
