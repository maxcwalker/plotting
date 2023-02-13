################################################################
# This script makes sure that mesh files are in the same order #
#          to ensure postprocessing scripts work               #
################################################################
from matplotlib import pyplot as plt
import numpy as np

with open("./grid.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    if lines[i][0:2] == "NP":
        print(lines[i])
        a = i # a is the NPOIN line

print(lines[a])
print("This is a = "+str(a))

print("a is " + str(a))
print(len(lines))

# grabbing all lines after NPOIN
b = []
for i in range(len(lines)):
    if i > a:
        b.append(lines[i])
    else:
        continue

# grabbing all lines after NPOINT to the end of the coordinates
points = []

for i in range(len(b)):
    if b[i][0] != "%":
        points.append(b[i])
    else:
        c=i+a+1 # The line after the last coordinate
        break

print("This is c = "+str(c))
print(lines[c])
lines2 = lines[c:len(lines)]

for i in lines2:
    if lines2[i] == 'MARKER_TAG= outlet':
        lines2[i].replace("outlet", "inlet")

for i in lines2:
    if lines2[i] == 'MARKER_TAG= inlet':
        lines2[i].replace("inlet", "outlet")

## need to do something smart here to split and join and remove
points = points[::-1]

#########################################################
## This is to grab the numbers of the points which isnt needed as the numbering is implied by the order of coordinates
coords =[]
numbers = []
for i in range(len(points)):
    coords.append(points[i][0:50])
    numbers.append(points[i][51:len(points[i])])

numbers = numbers[::-1]
print(str(coords[1])+str(numbers[1]))

#########################################################

f = open("grid1.txt", 'w')

for i in range(a+1):
    f.write(str(lines[i]))

for i in range(len(points)):
    #f.write(str(points[i]))
    f.write(str(coords[i])) # removed +str(numbers[i]) as the numbers of the elements is already implied by the ordering

for i in range(len(lines2)):
    f.write(lines2[i])


f.close()


with open("grid1.txt") as f:
    lines4 = f.readlines()

for i in range(len(lines4)):
    if lines4[i] == 'MARKER_TAG= outlet':
        lines4[i].replace("outlet", "inlet")

for i in range(len(lines4)):
    if lines4[i] == 'MARKER_TAG= inlet':
        lines4[i].replace("inlet", "outlet")

f.close()