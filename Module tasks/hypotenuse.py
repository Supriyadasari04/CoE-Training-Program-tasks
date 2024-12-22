import math
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
hyp = hypotenuse(a, b)
print(f"The hypotenuse of the triangle is: {hyp:.2f}")
