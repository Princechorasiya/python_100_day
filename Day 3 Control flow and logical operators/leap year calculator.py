#7 coding challenge. #find the flow from the flowchats
year=int(input("Which year do oyu want to check?"))
#write  a program to find out if a given year is a leap year
#on every year that is evenly divisible by 4
#except every year that is evenly sivisible by  100
#unless the year is also evenly divisible by 400.
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This year is a leap year")
        else:
            print("This year is not a leap year.")
    else:
         print("The year is a  leap year")

else:
    print("Not a leap year.")
