"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""
sample_tuple = ("anish", "thapaliya", 24)
people = []
people.append(sample_tuple)
sample_tuple_one = ("arjun", "devkota", 25)
sample_tuple_two = ("sushim", "joshi", 24)
people.append(sample_tuple_one)
people.append(sample_tuple_two)
people.sort(key=lambda tupel: tupel[1])
print(people)