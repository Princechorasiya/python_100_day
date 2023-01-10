import random
#randrange(start,stop,step) reurns a randomly selected integer from randrange(start,stop,step) value error if start>stop.
a=random.randrange(2,10,2)
#step defines the incrementation
print(a)
b=random.randrange(2,10,3)
print(b)


#code challenge
#virtual coin toss "heads" and "tails"
import random as rd
random_number=rd.randint(1,2)
print("welcome to the coin toss.Please toss the coin")
if random_number==1:
    print("Heads")
else:
    print("tails")