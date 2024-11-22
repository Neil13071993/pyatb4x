# How to write to a file

with open("Testdata.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")  # or    end="\n"