my_shopping_list = ["bread", "butter", "milk"]
print(my_shopping_list[0])
print(len(my_shopping_list))

# to remove the duplicates we used function SET
def bring_more_food(my_list):
    more_item = input("Enter the name \n")
    my_list.append(more_item)
# my_list.remove(more_item)
#my_list.insert(0,more_item)
    return my_list

l = bring_more_food(my_shopping_list)
print(l)