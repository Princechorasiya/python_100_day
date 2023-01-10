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
    else:
        bill=12
        print("Adult tickets are available for 12$")

    wants_photo=input("Do you want a photo taken?Y or N.")
    if wants_photo=="Y":#add 3$ to the bill
        bill+=3
    print(f"Your bill is {bill}")

else:
    print("Sorry you cant ride the rollercosternow.\nPlease come back after you grow up.")