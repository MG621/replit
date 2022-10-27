from math import cos
from math import sqrt
from math import radians

# Name: Mario A. Garza


# Write a function that takes in some integer greater than 0 as a parameter and checks
# whether the integer is prime. Print a statement, does not return anything.
# Hint: Loop through the integers previous
# Hint: 1 is not prime

### Write here ###

def checkPrime(a):

  if a > 1:
    for x in range(2,a):
      if (a % x == 0):
        print(f"{a} is not prime")
        break
    else:
      print(f"{a} is prime")
  else:
    print(f"{a} is not prime")
    
i = int(input("Please enter a number: "))
checkPrime(i)
#--------------------------------------------------------------------------------------------------------

# Write a function that calculates the volume of a sphere. Then let the user input enter the radius for
# two spheres. Use the function to find and print which sphere is bigger, along with its volume up to two decimals.

### Write here ###

def compVol(a,b):
  volA = (4/3) * 3.1415 * (a ** 3)
  volB = (4/3) * 3.1415 * (b ** 3)

  if volA >= volB:
    print("The first sphere is larger")
    print(f"Volume: {round(volA, 2)}")
  else:
    print("The second sphere is larger")
    print(f"Volume: {round(volB,2)}")

a = int(input("Please enter the radius: "))
b = int(input("Please enter another radius: "))

compVol(a,b)

#--------------------------------------------------------------------------------------------------------

# Write a function that finds the length of the third side of a triangle. Function should have three
# arguments: one side of triangle, another side, angle between the sides. Ask the user to input the 
# two sides and the angle between them in degrees. Return the answer as a float and print it outside of 
# the function, format to two decimal points.
# Hint: Use the law of cosines formula
# Hint: The cos() function only takes radians, so use radians() function for conversion

### Write here ###

def lengthTriangle(a,b,ang):
  return sqrt(a**2+b**2 - 2*a*b * cos(radians(ang)))

a = float(input("Please enter the side length: "))
b = float(input("Please enter another side length: "))
ang = float(input("Please enter the angle in degrees: "))

print(f"The length of the side is {lengthTriangle(a,b,ang)}")