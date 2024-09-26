# list is mutable in nature
# Mutable = Change

squares = [1,4,16,25,36]
squares[3] = 64
print(squares)

# Touple = it is immutable in nature

my_tuple = (1,4,16,25,36)
#my_tuple[3] = 64
print(my_tuple)

shopping_list = ["bread", "butter", "milk"]
shopping_list[2] = "khari"
print(shopping_list)

# real world project
 # thetestingacademy.com , sdet.live

my_tuple = ("tta.com", "sdet.live")
my_api_list = list(my_tuple)  #conversion
my_api_list = tuple(my_tuple)  #conversion
print(my_api_list)