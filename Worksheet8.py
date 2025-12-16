import math
import numpy as np

#Question1
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:", distance)

#Question2
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
print("Midpoint:", (mid_x, mid_y))

#Question3
if x2 - x1 != 0:
    slope = (y2 - y1) / (x2 - x1)
    print("Slope of line:", slope)
else:
    print("Slope is undefined")

#Question4
if x2 - x1 != 0:
    c = y1 - slope * x1
    print("Equation of line: y =", slope, "x +", c)

#Question5
a = np.array([1, 2])
b = np.array([3, 4])
print("Vector addition:", a + b)
print("Vector subtraction:", a - b)

#Question6
dot = a[0]*b[0] + a[1]*b[1]
print("Dot product:", dot)

#Question7
mag_a = math.sqrt(a[0]**2 + a[1]**2)
mag_b = math.sqrt(b[0]**2 + b[1]**2)
print("Magnitude of a:", mag_a)
print("Magnitude of b:", mag_b)

#Question8
angle = math.acos(dot / (mag_a * mag_b))
print("Angle between vectors (radians):", angle)

#Question9
p1 = np.array([0, 0])
p2 = np.array([4, 5])
p3 = np.array([3, 2])

num = abs((p2[1]-p1[1])*p3[0] - (p2[0]-p1[0])*p3[1] + p2[0]*p1[1] - p2[1]*p1[0])
den = math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)
print("Distance of point from line:", num / den)

#Question10
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("Matrix addition:")
print(A + B)

print("Matrix multiplication:")
print(np.dot(A, B))