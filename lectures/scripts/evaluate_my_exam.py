#!/usr/bin/env python3
# Author: Levent Aydinbakar
# Date: 27 November 2022 07:21:02
# Last update: 27 November 2022 11:17:50

import os
import numpy
import sys
import shutil
import subprocess
import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--group_name", type=str, help="Enter your group letter. (Like 1A, 2B, 3C, 1D, 2E,...)")
args=parser.parse_args()

g=args.group_name
i = str(g)
p=0

if i=="1A" or i=="2B" or i=="3E":
  fname="answer"
  fname2="0001"
  fname3="0013"
  fname4="01.txt"
  fname5="93.txt"

  fname6="15.txt"
  fname7="75.txt"
  fname8="30.txt"
  fname9="35.txt"

  var0="column"
  var1=800

  var2=75
  var3=2
elif i=="1B" or i=="2E" or i=="3C":
  fname="A"
  fname2="0001"
  fname3="0015"
  fname4="01.txt"
  fname5="91.txt"

  fname6="0010.txt"
  fname7="0060.txt"
  fname8="0030.txt"
  fname9="0035.txt"

  var0="column"
  var1=1100

  var2=80
  var3=4

elif i=="1C" or i=="2A" or i=="3D":
  fname="ANSWER"
  fname2="00001"
  fname3="00015"
  fname4="01.txt"
  fname5="97.txt"

  fname6="010.txt"
  fname7="065.txt"
  fname8="030.txt"
  fname9="035.txt"

  var0="column"
  var1=1900

  var2=80
  var3=5
elif i=="1D" or i=="2C" or i=="3B":
  fname="Answer"
  fname2="001"
  fname3="017"
  fname4="0001.txt"
  fname5="0091.txt"

  fname6="00.txt"
  fname7="70.txt"
  fname8="30.txt"
  fname9="35.txt"

  var0="row"
  var1=1100

  var2=90
  var3=3
elif i=="1E" or i=="2D" or i=="3A":
  fname="script"
  fname2="00001"
  fname3="00012"
  fname4="000001.txt"
  fname5="000099.txt"

  fname6="025.txt"
  fname7="075.txt"
  fname8="030.txt"
  fname9="035.txt"

  var0="row"
  var1=1000

  var2=75
  var3=2
  
print("IF THE FILES run_all.sh, remove.sh and README.md EXIST:")
if os.path.exists("run_all.sh"):
  print("You have run_all.sh +5p")
  p=p+5
if os.path.exists("remove.sh"):
  print("You have remove.sh +5p")
  p=p+5
if os.path.exists("README.md"):
  print("You have README.md +10p")
  p=p+10

for j in range(1,2):
  if os.path.exists(fname+str(j)+"_"+i+".sh"):
    print("Q1 is being checked.")
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("************************")
      print("IF YOU GET AN ERROR HERE, REMOVE YOUR ./{0}{1}_{2} FILE (NOT FOLDER) AND RESTART THIS SCRIPT.".format(fname,str(j),i))
      print("************************")
      shutil.rmtree("./{0}{1}_{2}".format(fname,str(j),i))
    os.system("set -e ; bash {0}{1}_{2}.sh 1> /dev/null 2>&1 || true".format(fname,str(j),i))
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("You have ./{0}{1}_{2} +5p".format(fname,str(j),i))
      p=p+5
      if os.path.exists("./{0}{1}_{2}/{3}".format(fname,str(j),i,fname2)) and os.path.exists("./{0}{1}_{2}/{3}".format(fname,str(j),i,fname3)):
        print("You have ./{0}{1}_{2}/{3} and ./{0}{1}_{2}/{4} +5p".format(fname,str(j),i,fname2,fname3))
        p=p+5
        if os.path.exists("./{0}{1}_{2}/{3}/{4}".format(fname,str(j),i,fname2,fname4)) and os.path.exists("./{0}{1}_{2}/{3}/{4}".format(fname,str(j),i,fname3,fname5)):
          print("You have ./{0}{1}_{2}/{3}/{4} and ./{0}{1}_{2}/{5}/{6} +7.5p".format(fname,str(j),i,fname2,fname4,fname3,fname5))
          p=p+7.5
          if os.path.exists("./{0}{1}_{2}/{3}/{4}".format(fname,str(j),i,fname2,fname4)) and os.popen("cat ./{0}{1}_{2}/{3}/{4} | wc -l".format(fname,str(j),i,fname3,fname5)).read() == "5\n":
            print("You have five lines in ./{0}{1}_{2}/{3}/{4} and ./{0}{1}_{2}/{5}/{6} +7.5p".format(fname,str(j),i,fname2,fname4,fname3,fname5))
            p=p+7.5
          else:
            print("Either you do not have ./{0}{1}_{2}/{3}/{4} or it does not have 5 lines of text in it.".format(fname,str(j),i,fname2,fname4))
        else:
          print("./{0}{1}_{2}/{3}/{4} or ./{0}{1}_{2}/{5}/{6} does not exist.".format(fname,str(j),i,fname2,fname4,fname3,fname5))
      else:
        print("You do not have either ./{0}{1}_{2}/{3} or ./{0}{1}_{2}/{4} or both which you were asked to make.".format(fname,str(j),i,fname2,fname3))
    else:
      print("You do not have ./{0}{1}_{2} directory which you were asked to make.".format(fname,str(j),i))
  else:
    print(fname+str(j)+"_"+i+".sh does not exist. Q1 is not checked...")
for j in range(2,3):
  if os.path.exists(fname+str(j)+"_"+i+".sh"):
    print("Q2 is being checked.")
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("************************")
      print("IF YOU GET AN ERROR HERE, REMOVE YOUR ./{0}{1}_{2} FILE (NOT FOLDER) AND RESTART THIS SCRIPT.".format(fname,str(j),i))
      print("************************")
      shutil.rmtree("./{0}{1}_{2}".format(fname,str(j),i))
    os.system("set -e ; bash {0}{1}_{2}.sh F1 F2 F3 1> /dev/null 2>&1 || true".format(fname,str(j),i))
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("You have ./{0}{1}_{2} +5p".format(fname,str(j),i))
      p=p+5
      if os.path.exists("./{0}{1}_{2}/F1".format(fname,str(j),i)) and os.path.exists("./{0}{1}_{2}/F3".format(fname,str(j),i)):
        print("You have 3 subdirectories which are read from the commandline in ./{0}{1}_{2} +5p".format(fname,str(j),i))
        p=p+5
        if os.path.exists("./{0}{1}_{2}/F1/{3}".format(fname,str(j),i,fname6)) and os.path.exists("./{0}{1}_{2}/F3/{3}".format(fname,str(j),i,fname7)):
          print("You have ./{0}{1}_{2}/F1/{3} and ./{0}{1}_{2}/F3/{4} files +5p".format(fname,str(j),i,fname6,fname7))
          p=p+5
          if os.popen("cat ./{0}{1}_{2}/F1/{3} | grep even | wc -l".format(fname,str(j),i,fname8)).read()  == "1\n":
            print("Correct, ./{0}{1}_{2}/F1/{3} is an even file +5p".format(fname,str(j),i,fname8))
            p=p+5
          else:
            print("This is an even file is not written in ./{0}{1}_{2}/F1/{3}.".format(fname,str(j),i,fname8))
          if os.popen("cat ./{0}{1}_{2}/F3/{3} | grep odd | wc -l".format(fname,str(j),i,fname9)).read() == "1\n":
            print("Correct, ./{0}{1}_{2}/F1/{3} is an odd file +5p".format(fname,str(j),i,fname9))
            p=p+5
          else:
            print("This is an odd file is not written in ./{0}{1}_{2}/F3/{3}.".format(fname,str(j),i,fname9))
        else:
          print("./{0}{1}_{2}/F1/{3} or ./{0}{1}_{2}/F3/{4} does not exist.".format(fname,str(j),i,fname6,fname7))
      else:
        print("You do not have three subdirectories you read from de commandline in ./{0}{1}_{2} which you were asked to make.".format(fname,str(j),i))
    else:
      print("You do not have ./{0}{1}_{2} directory which you were asked to make.".format(fname,str(j),i))
  else:
    print(fname+str(j)+"_"+i+".sh does not exist. Q2 is not checked...")

for j in range(3,4):
  if os.path.exists(fname+str(j)+"_"+i+".py"):
    print("Q3 is being checked.")
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("************************")
      print("IF YOU GET AN ERROR HERE, REMOVE YOUR ./{0}{1}_{2} FILE (NOT FOLDER) AND RESTART THIS SCRIPT.".format(fname,str(j),i))
      print("************************")
      shutil.rmtree("./{0}{1}_{2}".format(fname,str(j),i))
    os.system("set -e ; python3 {0}{1}_{2}.py 1> /dev/null 2>&1 || true".format(fname,str(j),i))
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("You have ./{0}{1}_{2} +5p".format(fname,str(j),i))
      p=p+5
      if os.popen("ls ./{0}{1}_{2}/ | wc -l".format(fname,str(j),i)).read() == "2\n":
        print("You have two files in ./{0}{1}_{2} +5p".format(fname,str(j),i))
        p=p+5
        AA1=numpy.ones((3,var1))
        if var0=="column":
          for aa in range(3):
            AA1[aa,:]=AA1[aa,:]*aa*math.pi
        elif var0=="row":
          for aa in range(var1):
            AA1[:,aa]=AA1[:,aa]*aa*math.pi
        if numpy.sum(AA1[:,:]) == numpy.sum(numpy.loadtxt("./{0}{1}_{2}/text.txt".format(fname,str(j),i))[:]):
          p=p+7.5
          print("You text.txt is correct +7.5p")
        else:
          print("You could not multiply your array (text.txt) with a correct value.")
        if numpy.sum(AA1[:,:]) == numpy.sum(numpy.fromfile("./{0}{1}_{2}/binary".format(fname,str(j),i),dtype="f8")[:]):
          p=p+7.5
          print("You binary is correct +7.5p")
        else:
          print("You could not multiply your array (binary) with a correct value.")
      else:
        print("You do not have two files (text.txt and binary) in ./{0}{1}_{2} which you were asked to make.".format(fname,str(j),i))
    else:
      print("You do not have ./{0}{1}_{2} directory which you were asked to make.".format(fname,str(j),i))
  else:
    print(fname+str(j)+"_"+i+".py does not exist. Q3 is not checked...")
  
for j in range(4,5):
  if os.path.exists(fname+str(j)+"_"+i+".py"):
    print("Q4 is being checked.")
    if os.path.exists("./{0}{1}_{2}".format(fname,str(j),i)):
      print("************************")
      print("IF YOU GET AN ERROR HERE, REMOVE YOUR ./{0}{1}_{2} FILE (NOT FOLDER) AND RESTART THIS SCRIPT.".format(fname,str(j),i))
      print("************************")
      shutil.rmtree("./{0}{1}_{2}".format(fname,str(j),i))
    os.system("set -e ; python3 {0}{1}_{2}.py -o fname -f f1 f2 1> /dev/null 2>&1 || true".format(fname,str(j),i))
    if os.path.exists("./f1/fname"):
      print("You have ./f1/fname which are read from argparse +5p")
      p=p+5
      A1=numpy.ones((2,var2))
      if numpy.sum(A1[:,:]) == numpy.sum(numpy.fromfile("./f1/fname",dtype="f8")[:]):
        p=p+7.5
        print("Your array in ./f1/fname is correct +7.5p")
      else:
        print("You do not have correct array in fname file")
    else:
      print("You do not have ./f1/fname which f1 and fname must be read by argparse.")
    if os.path.exists("./f2/fname"):
      p=p+5
      print("You have ./f2/fname which are read by argparse +5p")
      A5=numpy.ones((2,var2))
      for i in range(var2):
        if i%var3==0:
          A5[:,i]=A5[:,i]*5
      if numpy.sum(A5[:,:]) == numpy.sum(numpy.fromfile("./f2/fname",dtype="f8")[:]):
        p=p+7.5
        print("Your array in ./f2/fname is correct +7.5p")
      else:
        print("You do not have correctly multiplied array in fname file")
    else:
      print("You do not have ./f2/fname which f2 and fname must be read by argparse.")
  else: 
    print(fname+str(j)+"_"+i+".py does not exist. Q4 is not checked...")
print("Total point: ",p)
