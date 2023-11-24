import numpy as np
import matplotlib.pyplot as plt

L = 0.1
H = 0.01
nx = 300
ny = 100
fx = 4 # stretching factor for the sinh graph in x direction
fy = 5 # stretching factor in the y direction

## for the x direction
plate_xs = np.linspace(0,L,nx) 
norm_xs = plate_xs / L * fx # divided by L to create a difference when passed through the function
funct_x = np.sinh(norm_xs)
xs =funct_x / max(funct_x) * L # spreading the points within the plate boundaries

x_zeros = np.zeros(nx)

## for the y direction
plate_ys = np.linspace(0,H,ny)
norm_ys = plate_ys / H * fy
funct_y = np.sinh(norm_ys)
ys = funct_y / max(funct_y) * H

y_zeros = np.zeros(ny)

## positive coordinates
pos_coords = []
for x in range(len(xs)):
    for y in range(len(ys)):
        pos_coords.append((xs[x],ys[y]))

neg_coords = []
# how long is the symmetry; 0=no symmetry 
neg_range = 0.01

for lines in pos_coords:
    if lines[0] <= neg_range:
        if lines[0] != 0:
            neg_coords.append((-lines[0],lines[1]))

neg_coords = neg_coords[::-1]
new_neg_coords = []

## The y values of the neg coords need to be flipped to be going from bottom to top of domain
for i in range(len(neg_coords)):
    new_neg_coords.append((neg_coords[i][0],neg_coords[len(neg_coords)-i-1][1]))
neg_coords = new_neg_coords # give the values back to neg_coords

coords = []

for i in range(len(neg_coords)+len(pos_coords)):
    if i< len(neg_coords):
        coords.append(neg_coords[i])
    else:
        coords.append(pos_coords[i-len(neg_coords)])

# print(len(neg_coords)+len(pos_coords))
# print(len(coords))

fig, ax = plt.subplots(1,1)
# print(np.shape(coords))
for i in range(len(coords)):
    ax.plot(coords[i][0],coords[i][1],marker='.',markersize=1)

ax.set_aspect(1)
plt.savefig("gridplot.pdf")


node_coords = []
x=0
for i in range(len(coords)):

    node_coords.append((coords[i][0],coords[i][1],x))
    x=x+1

## node_coords now holds an index for each point as well ##

nx = len(coords) / ny
print('----------------------------------------------')
print("This is a %.0f x %.0f grid" % (nx,ny))
print('----------------------------------------------')

nx = int(nx)
print(nx)
n_nodes = nx*ny
n_elem = (nx-1)*(ny-1)
print(n_elem)

elements = []

########################################################################
cell_connectivity = []
for row in range(nx-1):
    for cell in range(ny-1):
        cell_number = cell # was +1 which I think was the problem
        
        node_1 = row*ny + cell_number
        node_2 = node_1+1
        
        node_4 = (row+1)*(ny) + cell_number
        node_3 = node_4 + 1
        
        connect = [node_1, node_2, node_3, node_4]
        cell_connectivity.append(connect)
#################################################################


farfield = []

for i in range(nx-1):
    farfield.append((node_coords[ny*(i+1)-1][2],node_coords[ny*(i+1)+ny-1][2]))

lower = []
for i in range(nx-1):
    lower.append((node_coords[i*ny][2],node_coords[i*ny+ny][2],node_coords[i*ny+ny][0]))

symmetry = []; wall = []

for i in range(len(lower)):
    if lower[i][2] <= 0:
        symmetry.append((lower[i][0], lower[i][1]))
    else:
        wall.append((lower[i][0],lower[i][1]))

inlet = []
outlet = []

min_x = min(node_coords[0])

for i in range(ny-1):
    inlet.append((node_coords[i][2],node_coords[i+1][2]))
    outlet.append((node_coords[ny*(nx-1)+i][2], node_coords[ny*(nx-1)+i+1][2]))


########################################################################################
#################################   WRITING THE FILE  ##################################
########################################################################################

#First we define the necesarry variables:
N_DIME = 2
N_POIN = n_nodes
N_ELEMS = n_elem
N_MARK = 5

inner_type = 9
boundary_type = 3

#Then we open the file to write to, ensuring there is no carried over data points
f = open("mesh_%dx%d_grid.su2" % (nx,ny), 'w')

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
