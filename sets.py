#Sets 
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)  # Adds an element to the set
print(my_set)

my_set.remove(3)  # Removes an element from the set
print(my_set)

'''
# Set operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)  # Prints the union of set1 and set2

# Intersection of two sets
inter_set = set1.intersection(set2)
print(inter_set) # Prints the intersection of set1 and set2

# Difference of two sets
diff_set = set1.difference(set2)
print(diff_set)  # Prints the difference of set1 and set2