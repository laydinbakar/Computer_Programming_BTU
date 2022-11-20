#!/usr/bin/env python3
# 1/A 1234567890 Levent Aydinbakar

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", type=str, help="Output file name")
parser.add_argument("-f", "--folders", nargs=2, type=str, help="Enter two folder names")
args=parser.parse_args()

o=args.output
f1=args.folders[0]
f2=args.folders[1]

import os

if not os.path.exists("python_output"):
  os.mkdir("python_output")
if not os.path.exists("python_output/"+str(f1)):
  os.mkdir("python_output/"+str(f1))
if not os.path.exists("python_output/"+str(f2)):
  os.mkdir("python_output/"+str(f2))


import numpy
A=numpy.ones((2,50))

numpy.array(A, dtype="f8").tofile(open("python_output/"+str(f1)+"/"+str(o),"wb"))

for i in range(50):
  if i%3==0:
    A[:,i]=A[:,i]*5

numpy.array(A, dtype="f8").tofile(open("python_output/"+str(f2)+"/"+str(o),"wb"))

