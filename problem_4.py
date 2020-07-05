"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""
sample_list = []
number_of_items_list = 5
for  i in range(number_of_items_list):
    sample_list.append(f"anish{i}")
sample_list.sort()

for i in range(2):
    print(f"{i} item is {sample_list[i]}")