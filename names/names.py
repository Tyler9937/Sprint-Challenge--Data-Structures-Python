import time

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)




start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements

# names_2_tree = BSTNode(names_2[0])
# for i in names_2:
#   names_2_tree.insert(i)


# for name_1 in names_1:
#     if names_2_tree.contains(name_1):
#          duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")


# Inital runtime complexity is O(n^n)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

dup_strecth = []
names_1_stretch = names_1
names_2_stretch = names_2

for name_1_stretch in names_1_stretch:
    if name_1_stretch in names_2_stretch:
        names_2_stretch.remove(name_1_stretch) # Doesnt imporve performace much but thought it was a good idea
        dup_strecth.append(name_1_stretch)

end_time = time.time()
print(' ')
print('Stretch Data Structure')
print (f"{len(dup_strecth)} duplicates:\n\n{', '.join(dup_strecth)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
