#!/usr/bin/env python3

import numpy

x=numpy.arange(0,10*numpy.pi,0.01)
y=numpy.sin(x)

A=numpy.column_stack((x,y))

numpy.savetxt("dat.txt",A)
