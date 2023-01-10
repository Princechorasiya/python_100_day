#fizz buzz challenge
outspoken=0
for number in range(1,101):
    outspoken=number
    if outspoken%3==0:
        if outspoken%5==0:
            number="fizz buzz"
        else:
            number="fizz"
    if outspoken%5==0 and outspoken%3!=0:
        number="buzz"
    print(number)



