import numpy as np
import matplotlib.pyplot as plt
import math

nx = 10
L = 0.3*1.05 # 105% of length so that the the outlet is slightly over the line
H = 0.03

plate_xs = np.linspace(0,L,nx)
plate_ys = np.zeros(nx)

n = 10 # not sure what this controls yet
a = 3 # a factor of stretching I think


xs = np.linspace(-1,1,n)
ys = np.tanh(np.pi*xs/a) + 1

## scaling the dx values for the length of the domain
dxs = ys/n*L
actuals = []
dx = 0

for value in dxs:
    actuals.append(dx)
    dx+=value
zers=np.zeros(len(actuals))
# plt.figure(figsize = (15, 2))
# plt.plot(actuals,zers, ".")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("x spacing for a=3")


## converting the points to node coordinates

mult_y = L/H # Factor of difference between length and H to calc the y coords
## I have a feeling this is for a nxn grid, amy need adjusting for n x m grid ##
dys = dxs /mult_y

ys = []

for x in actuals:
    dy = 0
    holder = []
    for d in dys:
        holder.append(dy)
        dy+=d
    ys.append([x,holder])

## stretching the grid upstream of the leading edge

F = 3 # meaning 1/F of a domain upstream of the leading edge
## The grid has to be mirrored about x = 0

coords_array =[]; right_hard = []; left_hand = []

for v_line in ys:
    if v_line[0] <= (L/F): # taking values that are up to L/F which is how far the grid needs to be extended
        left_hand.append([-v_line[0], v_line[1]]) # appending with the neg x coord
    else:
        break

for ys_val in ys:
    right_hard.append(ys_val)

for coord in reversed(left_hand):
    coords_array.append(coord)

for coord in right_hard[1:]:
    coords_array.append(coord)

# plotting these coordinates

plt.figure(figsize=(10,1), dpi = 180)
for line in coords_array:
    x = line[0]
    for y in line[1]:
        plt.plot(x,y,'.')

plt.xlabel('x')
plt.ylabel('y')

# ordering the cooridnates in a structured way to ouput them to a .txt file
y_range = len(coords_array[0][1])
x_range = len(coords_array)
node_coordinates = []

current_index = 0
for y in range(y_range):
    for x in range(x_range):
        x_coord = coords_array[x][0]
        y_coord = coords_array[x][1][y]

        node_coordinates.append((x_coord,y_coord))

n_x = len(coords_array)
n_y = len(coords_array[0][1])

n_nodes = n_x*n_y
n_cells = (n_x-1)*(n_y-1)

print("There are", n_nodes, "nodes in the grid.")
print("There are", n_cells, "cells in the grid.")
print("There are", n_x, "nodes per row.")
print("There are", n_y, "rows of nodes.")


cell_connectivity = []
for row in range(n_y-1):
    for cell in range(n_x-1):
        cell_number = cell+1 # was +1 which I think was the problem
        
        node_1 = row*n_x + cell_number
        node_2 = node_1+1
        
        node_4 = (row+1)*(n_x) + cell_number
        node_3 = node_4 + 1
        
        connect = [node_1, node_2, node_3, node_4]
        cell_connectivity.append(connect)


symmetry = []
wall = []
farfield = []
for cell in cell_connectivity[:n_x-1]:
    if node_coordinates[cell[1]-1][0] <= 0.0:
        symmetry.append([cell[0], cell[1]])
    else:
        wall.append([cell[0], cell[1]])
        
for cell in cell_connectivity[len(cell_connectivity)-n_x+1:]:
    farfield.append([cell[3], cell[2]])

inlet = []
outlet = []
for i in range(1, n_y):
    inlet.append([(i-1)*n_x+1, i*n_x+1])
    outlet.append([(i-1)*n_x+n_x, i*n_x+n_x])

#First we define the necesarry variables:
N_DIME = 2
N_POIN = n_nodes
N_ELEMS = n_cells
N_MARK = 5

inner_type = 9
boundary_type = 3

#Then we open the file to write to, ensuring there is no carried over data points
f = open("mesh_test5.su2", 'w')

#First elements of the file are the dimension number and points array:
f.write("NDIME= " + str(N_DIME) +"\n")
f.write("NELEM= " + str(N_ELEMS) + "\n")

for element in cell_connectivity:
    f.write(str(inner_type) + " " + str(element[0]) + " " + str(element[1]) + " " + str(element[2]) + " " + str(element[3]) + "\n")

#Now we need to write in the element connectivity

f.write("NPOIN= " + str(N_POIN) +"\n")

#point in node_coordinates:
for i in range(len(node_coordinates)):
    point = node_coordinates[i]
    f.write(str(point[0]) + " " + str(point[1]) + " " + str(i) + "\n")

#Finally we need to define the boundaries:
f.write("NMARK= " + str(N_MARK) + "\n")


#Finally the UPPER
f.write("MARKER_TAG= farfield" +"\n")
f.write("MARKER_ELEMS= " + str(len(farfield)) + "\n")

for element in farfield:
    f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")


#First the INLET
f.write("MARKER_TAG= inlet" +"\n")
f.write("MARKER_ELEMS= " + str(len(inlet)) + "\n")

for element in inlet:
    f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")
 

 #Then the OUTLET
f.write("MARKER_TAG= outlet" +"\n")
f.write("MARKER_ELEMS= " + str(len(outlet)) + "\n")

for element in outlet:
    f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")


#Then the FIRST LOWER
f.write("MARKER_TAG= symmetry" +"\n")
f.write("MARKER_ELEMS= " + str(len(symmetry)) + "\n")

for element in symmetry:
    f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")


#Then the FLAT PLATE
f.write("MARKER_TAG= wall" +"\n")
f.write("MARKER_ELEMS= " + str(len(wall)) + "\n")

for element in wall:
    f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")

f.close()



plt.show()



