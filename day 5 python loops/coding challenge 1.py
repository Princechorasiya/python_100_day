#
#coding challenge1
student_heights=input("Enter the list of the heights of the students").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
#len(student_heights) for total no of inputs
#sum(student_heights) or sum of all inputs


total_height=0
for height in student_heights:#we can call height as anything as long as we are consistent
    total_height+=height
print(total_height)
number_of_students=0
for student in student_heights:
    number_of_students+=1
print(number_of_students)

average_height=round(total_height/number_of_students)
print(average_height)



#coding challenge
student_scores=input("Input a list of students scores:").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
#max(student_scores) for max in alist
#min(student_scores) for min in a list.
#no_of_students=0
#for mark in student_scores:
 #  no_of_students+=1
#print(no_of_students)
#marks_total=0
#for mark in student_scores:
 #   marks_total+=mark
#print(marks_total)
#for mark in student_scores:
 #    if mark*no_of_students>marks_total
#                  if mark


#solution:
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"The highest score in the class:{highest_score}")

lowest_score=highest_score
for score in student_scores:
    if lowest_score>score:
        lowest_score=score
print(lowest_score)

