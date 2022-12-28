import numpy
import math
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--iterations', \
                    default=100, type=int, \
                    help='Number of iterations (=100).')
args = parser.parse_args()

# Define length
l=4

# A function to rotate a point around another point
def rotate(point, origin, degrees):
  radians = numpy.deg2rad(degrees)
  x,y = point
  offset_x, offset_y = origin
  adjusted_x = (x - offset_x)
  adjusted_y = (y - offset_y)
  cos_rad = numpy.cos(radians)
  sin_rad = numpy.sin(radians)
  qx = offset_x + cos_rad * adjusted_x - sin_rad * adjusted_y
  qy = offset_y + sin_rad * adjusted_x + cos_rad * adjusted_y
  return qx, qy

# Make the triangle
p1=numpy.array([0,0])
p2=numpy.array([l,0])
p3=rotate(p2, p1, 60)

# Put a random point
random_point=numpy.array([1.5,2])

# Make a tuple to select p1, p2 or p3 randomly
r=numpy.stack((p1,p2,p3))

# Add the first point
p=numpy.vstack((p1,p2,p3,(p1+random_point)/2))

# Add the other points
for i in range(args.iterations):
  pp=random.choice(r)
  pnew=(pp+p[-1])/2
  p=numpy.vstack((p, pnew))

# Save the points to a file
# Add header x,y for Tikz
with open("sierpinskiPoints"+str(args.iterations)+".txt","w") as f:
  f.write("x,y\n")
  numpy.savetxt(f, p, fmt='%1.5f', delimiter=',')
