import os

full_path_file = os.path.join("/Users\Admin\PycharmProjects\pyatb4x\SRC\SEP_2024\EX10092024\pra", "nilesh.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)