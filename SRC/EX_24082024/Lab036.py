def print_arguments(*args):
    # *args = multiple arguments with no limits
    print(*args[0])


print_arguments("amit" , "pramod" , "lucky")
print_arguments("amit"  , "lucky")
print_arguments("lucky")
#print_arguments()   - minimum 1 arguments is required
