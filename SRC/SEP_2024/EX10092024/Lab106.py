import os

file = open('example.txt', 'r')
print(file.read())   # FileNotFoundError: [Errno 2] No such file or directory: 'testdata.txt'