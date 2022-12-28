import numpy
import math
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--iterations', \
                    default=1, type=int, \
                    help='Number of iterations (=1).')
args = parser.parse_args()

# Define length
l=4

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
p4=numpy.array([0,0])

P = numpy.stack((p1,p2,p3,p4))

for i in range(args.iterations):
  k=0
  for j in range(len(P)-1):
    lx=(P[k+1,0]-P[k,0])/3
    ly=(P[k+1,1]-P[k,1])/3
    P1=numpy.array([P[k,0]+lx,P[k,1]+ly])
    P3=numpy.array([P[k,0]+lx*2,P[k,1]+ly*2])
    P2=rotate(P3, P1, -60)

    P = numpy.vstack((P[:(k+1),:], P1, P2, P3, P[(k+1):,:]))
    k=k+4
  
  with open("KSP"+str(args.iterations)+".txt","w") as f:
    f.write("x,y\n")
    numpy.savetxt(f, P, fmt='%1.5f', delimiter=',')
