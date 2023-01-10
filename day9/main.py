# dictionaries
# key and associated value
# dictionary = {key:Value}
dictionary = {
    "Bug": "error in a program",
    "function": "functions performs tasks",
}
# list[index] to access the item
print(dictionary["Bug"])
# instead of index we use key write key properly along with the correct data type

# adding new items to the dictionary
dictionary["Loop"] = "the action of doing something again and again"
print(dictionary)


empty_dictionary = {}

# # wipe out a dictionary
# dictionary = {}

# print(dictionary)

# edit an item in a dictionary
dictionary["Bug"] = "A moth in your computer"
print(dictionary)


# looping through dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])


# grading challenge
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# convert scores into grades
# 91-100 outstanding
# 81-90 excced expectations
# 71-80 Acceptable
# <70 fail
student_grades = {}
for key in student_scores:
    marks = student_scores[key]
    grades = ""
    if 91 <= marks < 100:
        grade = "Outstanding"
    elif 81 <= marks < 90:
        grade = "Excced Expectations"
    elif 71 <= marks < 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)

# nesting lists and dictionaries
# nesting placing one inside the other
# dict1={
#     key:value,
#     key:value
# }
# nested list and dictionary format
# # {
# #     key:[list],
# #     key:{dictionary}
# }

capitals = {
    "France": "paris",
    "Germany": "berlin",
}

travel_log = {
    # "France":"Paris","Lille" this is wrong one key one value.
    "Country_visited": {"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}},
    "India": ["Delhi", "Mumbai", ["Agra", "Bilaspur"]],

}
# list inside a dictionary which is nested inside a dictionary
# nesting dictionaries inside a list
# [{key:[list],key2:{dict}},{key:value,key2:value,}]
# inside a list item is accessed by index while in dictionaries key is used.

list_travel_log = [
    {"country:": "France",
     "cities_visited": ["paris", "Lille", "Dijon"],
     "noofvisits":12,
     }
]

# coding challenge
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": ["paris", "Lille", "Dijon"]

    },
    {
        "country": "germany",
        "visits": 2,
        "cities_visited": ["berlin", "hamburg", "stuttgart"]
    }

]


def add_new_country(country, visits, cities_visited):
    global travel_log
    # mydict = {
    #     "country": country,
    #     "visits": visits,
    #     "cities_visited": cities_visited
    # }
    # travel_log.append(mydict)
    # print(travel_log)
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)
    print(travel_log)


add_new_country("russia", 2, ["Saint Petersburg", "moscow"])


# Blind auction program
