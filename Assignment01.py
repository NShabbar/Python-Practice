# A program designed to calculate the volume of a cube and a cone 
# based on a user's inputs

import math

# A function to check if user inputs are valid
def number_valid(number):
    if number == "":
        print("You did not enter a value.")
        output = float(input("Please enter a desired length for a cube: "))
        number_valid(output)
    elif type(number) != (int | float):
        print("You did not enter a valid number. Please try again.")
        output = float(input("Please enter a desired length for a cube: "))
        number_valid(output)
    else:
        return output

# Since the cube with be equal on all sides, only one measurement is needed.
# The formula for the volume of a cube is length(width)(height)
cube_length = number_valid(number = (input("Please enter a desired length for a cube: ")))



#To find the volume of a cone, the formula is: (radius^2(height/3)(pi))
cone_height = float(input("Please enter a desired height for the cone: "))
cone_radius = float(input("Please enter a desired radius for the cone: "))

# The ** syntax allows for exponent math. Similarly math.pow(x, y) 
# where x is the number being raised to y power.

# cube_volume = cube_length ** 3
cube_volume = math.pow(cube_length, 3)
cone_volume = math.pow(cone_radius, 2) * (cone_height/3) * math.pi 

print(f"The volume of the cube is: {cube_volume}.")
print(f"The volume of the cone is: {cone_volume}.")