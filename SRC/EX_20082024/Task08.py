# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides,
#
# determine if the triangle is equilateral (all sides are equal),
#
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.

L1 = int(input("Enter the Length1\n"))
L2 = int(input("Enter the Length2\n"))
L3 = int(input("Enter the Length3\n"))

if L1 == L2 and L2 == L3 and L1 == L3:
    print("it is a equilateral triangle")
elif L1 == L2 or L1 == L3:
    print("it is isosceles triangle")
elif L1 != L2 and L2 != L3:
    print("it is scalene triangle")
