# List
# List - Collection of Items( Duplicate is allowed)
# my_list = [1, 2, 3]  # Same type of data (int)
# my_list2 = [1, True, "Pramod", 12.34]

my_list = [1,2,3]
print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[2])
#print(my_list[10]) # list index out of range.

my_list[0] = "Nilesh"
my_list[1] = "Shailesh"
my_list[2] = "Yogesh"
#my_list[10] = "Akshay"  # list assignment index out of range

print(my_list[0])
print(my_list[2])
print(my_list[1])

print("element at the index o -", my_list[0])
print("element at the index o -", my_list[2])
print("element at the index o -", my_list[1])

print(my_list)

for element in my_list:
    print(element)

my_list = [1,2,3,]
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list)

my_list.extend([7,8,9])
my_list.extend([10])
my_list.extend(["Nilesh"])
print(my_list)

my_list.insert(1, "Gaikwad")
print(my_list)

my_list[1] = "Yogesh"
my_list[5] = "Shailesh"
print(my_list)

my_list.insert(-1, "Gaikwad")
print(my_list)

# Remove
my_list.remove("Shailesh")
print(my_list)

print("_______________________")
print("_______________________")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Nilesh")
my_copy_list.remove("Yogesh")
my_copy_list.remove("Gaikwad")
my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)