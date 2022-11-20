#!/usr/bin/env python3
# 1/A 1234567890 Levent Aydinbakar
import os

os.mkdir("python_output")

import numpy
A=numpy.ones((3,1000))

import math
for i in range(3):
  for j in range(1000):
    A[i,j]=A[i,j]*i*j*math.pi

numpy.savetxt("python_output/text.txt", A)
numpy.array(A, dtype="f8").tofile(open("python_output/binary","wb"))

print("Size of text.txt is ",os.path.getsize("python_output/text.txt"), "bytes and binary is ", os.path.getsize("python_output/binary"), "bytes.")

