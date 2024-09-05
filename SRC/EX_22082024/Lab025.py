# Continue Statememt = Continue Statememt skips the current iteration of a loop and
# moves to next iteration.

for number in range(10):
    if number % 2 ==0:
        continue
    print(number)

    # or
for number in range(10):
    if number % 2 ==0:
        continue
    else:
        print(number)

        # or

for number in range(10):
    if number % 2 ==0:
        pass
    else:
        print(number)

# pass = can be used in the statement, functions, class, objects.