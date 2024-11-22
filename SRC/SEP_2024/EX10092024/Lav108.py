import os

# print(os.name)

# if os.name == 'posix':
#      print("using mac")
# else:
#     print("windows")

# print(os.getcwd)
# os.chdir("Downloads")
# print(os.getcwd())


# os.mkdir('new_directory')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#    print(file)

# os.remove('example.txt')
# os.rmdir('new_directory')

full_path = os.path.join('/Users\Admin\PycharmProjects\pyatb4x\SRC\SEP_2024\EX10092024','file.txt')


print(full_path)

print(os.path.exists('file.txt'))
print(os.path.isfile('file.txt'))
print(os.path.isdir('directory_name'))

