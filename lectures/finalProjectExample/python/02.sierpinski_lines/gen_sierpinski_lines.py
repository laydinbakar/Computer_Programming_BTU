import numpy
import math
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--iterations', \
                    default=10, type=int, \
                    help='Number of iterations (=10).')
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
#p3=numpy.array([l/2,l/2])
p3=rotate(p2, p1, -60)

T = numpy.stack((p1,p2,p3,p1))

for i in range(args.iterations):
  # Make half of the triangle
  T1 = T/2
  
  ## Triplicate the half triangle and place them to obtain the orignal figure
  l1x = numpy.ones(len(T1))*l/2
  l1y = numpy.zeros(len(T1))
  l1 = numpy.column_stack((l1x,l1y))
  T3 = T1+l1
  
  l2x = numpy.ones(len(T1))*l/4
  l2y = numpy.ones(len(T1))*p3[1]/2
  l2 = numpy.column_stack((l2x, l2y))
  T2 = T1+l2
  T = numpy.vstack((T1,T2,T3,p1))

with open("lines"+str(args.iterations)+".txt","w") as f:
  f.write("x,y\n")
  numpy.savetxt(f, T, fmt='%1.5f', delimiter=',')
