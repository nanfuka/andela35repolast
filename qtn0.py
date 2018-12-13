
list1 = []
list2 =[]
grades = [23,4,5,6,64,90,67,98,45,23,67,78,89]
for grade in grades:
    if grade > 50:
        list1.append(grade)
return list1 


for grade in grades:
    if grade < 50:
        list2.append(grade)
return list2 

# 100 - 90 for Excellent
for grade in grades:
    if grade < 101 and grade > 89:
        return "Ecxcellent"

    if grade < 70 and grade > 59:
        return "very good"

    if grade < 68 and grade > 59:
        return "good"

    if grade < 58 and grade > 39:
        return "poor"

    if grade < 38 and grade > 19:
        return "very poor"

    if grade < 18 and grade > -1:
        return "repest"

# 59 - 40 for poor
# 39 - 20 for very poor
# 19 - 0 for repeat

   





