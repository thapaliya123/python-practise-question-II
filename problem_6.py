"""
6. Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""

collegue_list = ["anish", "manish", "pramish", "arjun", "aakrit", "samir"]
target_string = "John"

if target_string in collegue_list:
    print("found")

else:
    print("not found")