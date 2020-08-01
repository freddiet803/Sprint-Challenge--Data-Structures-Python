import time
from bst import BinarySearchTree

start_time = time.time()

with open('./names/names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
    f.close()

with open('./names/names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names
    f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''

# not sure we could apply anything but a bst
bst = BinarySearchTree('duplicates')

for the_names in names_1:
    bst.insert(the_names)

for the_names_2 in names_2:
    if bst.contains(the_names_2):
        duplicates.append(the_names_2)

#######################################################################

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
