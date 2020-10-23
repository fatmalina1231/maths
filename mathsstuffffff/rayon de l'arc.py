

from math import pi, radians
print("Calculates the length of radius based on arc length")

while True:
    arc = float(input("Arc? "))
    deg = float(input("Degrees? "))
    f = radians(deg)
    print(" ")

    print("Radius:")
    print(arc/f)
    print(" ")

    print("Circumference")
    print((arc/f)*2*pi)  
    print(" ")
