set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

set1 = {1, 2, 3,4,5}
set2 = {4, 5, 6,7,8}
my_test = set1.intersection(set2)
print(my_test)

my_test = set1.difference(set2)
print(my_test)

my_test = set2.difference(set1)
print(my_test)

set1 = {1, 2, 3,4,5}
set2 = {4, 5, 6,7,8}
subset = set2.issubset(set1)
print(subset)