#Problem_04 : Swap two variables.
# Write a python program to take two numbers as input from user and swap their values.

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
print("You entered:", num_1, "and", num_2)
print("Before swapping: num_1 =", num_1, ", num_2 =", num_2)
# Swapping values using a pythonic way
num_1, num_2 = num_2, num_1
print("After swapping: num_1 =", num_1, ", num_2 =", num_2)
# Goal: Practice variable assignment, input handling, and value swapping in Python.