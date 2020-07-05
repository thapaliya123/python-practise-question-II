"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

sample_list = [("anish", "thapaliya", 20), ("arjun", "devkota", 25), ("aakrit", "subedi", None)]
average_age = 0
count = 0
for item in sample_list:
    age = item[2]
    if(age != None):
        count+=1
        average_age = average_age+age
average_age = average_age//count

for person in sample_list:
    age = person[2]
    if age is None:
        print(person[0], "age is unknown")
    else:
        if age>average_age:
            print(person[0], "old")
        else:
            print(person[0], "young")