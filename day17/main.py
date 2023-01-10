# today goal
# quiz

# class is blueprint creating our own classes
class User:
    def __init__(self, user_id="003", user_name="prince_365"):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# self refers to the object referring to itself


class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_model(self):
        self.seats = 2


# camelCase
# snake_case
# PascalCase
car1 = Car("4")
print(car1.seats)
car1.enter_race_model()
print(car1.seats)

user1 = User("001", "prince")
print(user1.user_id)
print(user1.followers)

user2 = User("002", "liza")
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)


# method 1 lengthy not useful
# method 2 using constructor when using constructor we have to pass the required parameters or
# else it gives error
# we can use default value here to prevent this

# Adding method to the class


# user1.id = "001"
# user1.username = "prince"
# print(user1.username)

# //constructor specify what should happen when object is created
# __init__(self) is used  special method
