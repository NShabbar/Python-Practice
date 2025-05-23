# A program designed to calculate the volume of a cube and a cone 
# based on a user's inputs

import math
# Since the cube with be equal on all sides, only one measurement is needed.
# The formula for the volume of a cube is length(width)(height)
while True:
    try:
        cube_length = float(input("Please enter a desired length for a cube: "))
    except ValueError:
        print("You have entered an unvalid value.")
        continue
    if cube_length == (int | float):
        continue
    else:
        break

#To find the volume of a cone, the formula is: (radius^2(height/3)(pi))
while True:
    try:
        cone_height = float(input("Please enter a desired height for the cone: "))
    except ValueError:
        print("You have entered an unvalid value.")
        continue
    if cone_height == (int | float):
        continue
    else:
        break

while True:
    try:
        cone_radius = float(input("Please enter a desired radius for the cone: "))
    except ValueError:
        print("You have entered an unvalid value.")
        continue
    if cone_radius == (int | float):
        continue
    else:
        break   

# The ** syntax allows for exponent math. Similarly math.pow(x, y) 
# where x is the number being raised to y power.

# cube_volume = cube_length ** 3
cube_volume = math.pow(cube_length, 3)
cone_volume = math.pow(cone_radius, 2) * (cone_height/3) * math.pi 

print(f"The volume of the cube is: {cube_volume}.")
print(f"The volume of the cone is: {cone_volume}.")