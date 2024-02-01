import math
# Create a class named circle to store the data about this c1. This class should contain the following:
# Initialization (self, radius)
# Sets the radius property
class Circle:
    def __init__(self, radius):
        self.radius=radius

# Methods
# calculate_diameter()
# Returns the calculated diameter
    def calculate_diameter(self):
        diameter= self.radius*2
        return diameter


# calculate_circumference()
# Returns the calculated circumference
    def calculate_circumference(self):
        circumference=2*math.pi*self.radius
        return circumference
# calculate_area()
# Returns the calculated area
    def calculate_area(self):
        area=math.pi*math.pow(self.radius,2)
        return area

# grow()
# Doubles the radius property
    def grow(self):
        self.radius*=2
# get_radius()
# Returns the radius value
    def get_radius(self):
        return self.radius

validInput = False
while validInput == False:
    radius = float(input("Enter the radius of the circle: "))
    if (type(radius) != float):
        print("Invalid input, please enter a positive number")
    elif (radius <= 0):
        print("Invalid input, please enter a positive number")
    else:
        validInput = True
c1= Circle(radius)
print(f"Diameter: {c1.calculate_diameter()}")
print(f"Circumference: {c1.calculate_circumference()}")
print(f"Area: {c1.calculate_area()}")
growChoice=input("Would you like your circle to grow?(y/n) ")
while growChoice=='y':
    c1.grow()
    print(f"Diameter: {c1.calculate_diameter()}")
    print(f"Circumference: {c1.calculate_circumference()}")
    print(f"Area: {c1.calculate_area()}")
    growChoice = input("Would you like your circle to grow?(y/n) ")
    if growChoice=='n':
        print("Goodbye")
    elif(growChoice=='y'):
        pass
    else:
        print("Invalid input, please")
        growChoice=input("Would you like your c1 to grow?(y/n) ")
# For the value of pi, use the pi constant of the math module (import math).
# Get the user input, create a circle object, and display the diameter, circumference and area.
Circle(5)