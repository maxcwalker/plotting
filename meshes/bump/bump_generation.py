import numpy as np
import matplotlib.pyplot as plt
import math

L =  400
x0 = L/3
H = 100
h0 = H/20
nx = 256
ny = 128
a = 20 # smaller values compress the bump in the x direction
b = 5 # stretching factor in y direction
h = []

eta = np.linspace(0,1,ny)
xs = np.linspace(0,L,nx)
for i in range(len(xs)): h.append(h0*math.exp(-((xs[i]-x0)/a)**2))

y = []
for ypos in eta:
    for bumph in h: y.append(bumph+((H-bumph)*np.sinh(b*ypos))/np.sinh(b))

x = []
for i in range(ny): 
    for xp in xs: x.append(xp)

plt.scatter(x,y,marker='.',s=0.2)

node_coords = []
for i in range(len(x)): node_coords.append((x[i],y[i],i))
    

n_nodes = nx*ny
n_elem = (nx-1)*(ny-1)

cell_connectivity = []

for col in range(nx-1):
    for row in range(ny-1):
        
        node_1 = row*nx + col
        node_2 = (row+1)*nx + col
        node_3 = node_2 +1
        node_4 = node_1+1
        connect = [node_1, node_2, node_3, node_4]
        cell_connectivity.append(connect)

farfield=[]; wall=[]; inlet=[]; outlet=[]
for i in range(nx -1): farfield.append((node_coords[nx*(ny-1)+i][2], node_coords[nx*(ny-1)+i+1][2]))
for i in range(nx-1): wall.append((node_coords[i][2],node_coords[i+1][2]))
for i in range(ny-1): inlet.append((node_coords[i*nx][2],node_coords[i*nx+nx][2]))
for i in range(ny-1): outlet.append((node_coords[nx*(i+1)-1][2],node_coords[nx*(i+1)+nx-1][2]))


#First we define the necesarry variables:
N_DIME = 2
N_POIN = n_nodes
N_ELEMS = n_elem
N_MARK = 4

inner_type = 9
boundary_type = 3

#Then we open the file to write to, ensuring there is no carried over data points

bump_type = input('Is the bump centred (0) or offset (1)?')
if bump_type == 0:
    f = open("centred_bumps/bump_%dx%d_grid_centredbump.su2" % (nx,ny), 'w')
elif bump_type == 1:
    f = open("offset_bumps/bump_%dx%d_grid_offsetbump.su2" % (nx,ny), 'w')
else:
    print('BUmp type does not exist')
#First elements of the file are the dimension number and points array:
f.write("NDIME= " + str(N_DIME) +"\n")
f.write("NELEM= " + str(N_ELEMS) + "\n")

for element in cell_connectivity:
    f.write(str(inner_type) + " " + str(element[0]) + " " + str(element[1]) + " " + str(element[2]) + " " + str(element[3]) + "\n")

#Now we need to write in the element connectivity

f.write("NPOIN= " + str(N_POIN) +"\n")

#point in node_coordinates:
for i in range(len(node_coords)):
    point = node_coords[i]
    f.write(str(point[0]) + " " + str(point[1]) + " " + str(i) + "\n")

# Boundary definitions:
f.write("NMARK= " + str(N_MARK) + "\n")

# farfield
f.write("MARKER_TAG= upper_wall" +"\n")
f.write("MARKER_ELEMS= " + str(len(farfield)) + "\n")
for element in farfield: f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")

# inlet
f.write("MARKER_TAG= inlet" +"\n")
f.write("MARKER_ELEMS= " + str(len(inlet)) + "\n")
for element in inlet: f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")
 
 # outlet
f.write("MARKER_TAG= outlet" +"\n")
f.write("MARKER_ELEMS= " + str(len(outlet)) + "\n")
for element in outlet: f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")

# wall
f.write("MARKER_TAG= lower_wall" +"\n")
f.write("MARKER_ELEMS= " + str(len(wall)) + "\n")

for element in wall: f.write(str(boundary_type) + " " + str(element[0]) + " " + str(element[1]) + "\n")

f.close()

plt.show()
