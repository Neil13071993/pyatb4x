import os
try:
    file = open('testdata.txt', 'r')
    print(file.read())   # FileNotFoundError: [Errno 2] No such file or directory: 'testdata.txt'
except FileNotFoundError as fnfe:
    print("fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)