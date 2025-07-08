#problem_03 : Area  of a Circle.
#Write a python program to calculate the area of a circle.

radius = input ("Enter the radius of the circle: ")
print("You entered:", radius)
radius = float(radius)  # Convert input to float for calculation
area = 3.14 * radius * radius  # Calculate area using the formula πr²
print("The area of the circle with radius", radius, "is:", area)

# Goal: Practice float input, mathematical operations, and output formatting in Python.