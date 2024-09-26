# Dictionary
# Key value Pair

student_info = {"name" : "nilesh", "age" : 65, "address" : "Pune"}
print(student_info)

print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 100
print(student_info)

student_info1 = {
    "name" : "nilesh",
    "age" : 65,
    "address" : {
        "Home address" : "pune",
        "office address" : "Chinchwad"
    }
}

student_info2 = {
    "name" : "yogesh",
    "age" : 55,
    "address" : {
        "Home address" : "Chinchwad",
        "office address" : "pune"
    }
}

student_list = [student_info1,student_info2]
print(student_list)