#!/usr/bin/python
# --------------------------------------------------------------------------------------------------------------------------------------------
# paraview_timeseries, building from the orginal paraview code, 
# fix: KeysViewHDF5
#
# author. gnsa1e21, 2023, extension from satya p jammy, 2017
# university of southampton
# --------------------------------------------------------------------------------------------------------------------------------------------
# from paraview import read_dataset, strip_halos, 
# Convert the output from OpenSBLI to the domain only by removing the halo points
# Author Satya P Jammy, 2017
# Requires numpy and h5py

from __future__ import division
import numpy as np
import h5py
import argparse
import os
import sys

def read_dataset(openname, dataset):
    d_m = openname["%s"%(dataset)].attrs['d_m']
    d_p = openname["%s"%(dataset)].attrs['d_p']
    size = openname["%s"%(dataset)].shape
    read_start = [abs(d) for d in d_m]
    read_end = [s-abs(d) for d,s in zip(d_m,size)]
    if len(read_end) == 2:
        read_data = openname["%s"%(dataset)][read_start[0]:read_end[0], read_start[1]:read_end[1]]
    elif len(read_end) == 3:
        read_data = openname["%s"%(dataset)][read_start[0]:read_end[0], read_start[1]:read_end[1], read_start[2]:read_end[2]]
    else:
        raise NotImplementedError("")
    return read_data

def strip_halos(fname, output_name):

    opensbli_file = h5py.File(fname, 'r')
    block_name1 = list(opensbli_file.keys())[0]
    group_block =  opensbli_file[block_name1]
    output_opensbli = h5py.File(output_name, 'w')
    for key in group_block.keys():
        data_without_halos = read_dataset(group_block, key)
        output_opensbli.create_dataset("%s"%(key), data=data_without_halos)
    output_opensbli.close()
    return

class Smesh(object):
    coord_names = ["X", "Y", "Z"]
    def __init__(self, dims, size, fname, coordinates=True):
        self.ndim = dims
        self.size = size
        self.node_size_str = " ".join([str(s) for s in self.size])
        self.cell_size = [s-1 for s in size]
        self.fname = fname
        if coordinates:
            self.coordinate = ["x%d_B0"%d for d in range(self.ndim)]
        else:
            self.coordinate = coordinates
        return
    def topology(self):
        return "<Topology TopologyType=\"%dDSMesh\" NumberOfElements=\"%s\"/>" %(self.ndim, self.node_size_str)
    @property
    def dataitem_node(self):
        return """<DataItem Dimensions=\"%s\" NumberType=\"Float\" Precision=\"4\" Format=\"HDF\">\n %s:/%s\n</DataItem>\n""" 
    def attribute_node(self, attribute):
        attr = """<Attribute Name=\"%s\" AttributeType=\"Scalar\" Center=\"Node\">\n"""%(attribute)
        attr += self.dataitem_node%(self.node_size_str, self.fname, attribute) + "</Attribute>\n"
        return attr 
    def coordinate_read(self):
        geom = "<Geometry GeometryType=\"%s\">\n"%("_".join(self.coord_names[0:self.ndim]))
        reading = geom
        for d in range(self.ndim):
            reading += self.dataitem_node%(self.node_size_str, self.fname, self.coordinate[d])
        reading += "</Geometry>\n"
        return reading

def write_xdmf(output_name, timed):
    opensbli_file = h5py.File(output_name, 'r')
    block_name1 = list(opensbli_file.keys())[0]
    size =  opensbli_file[block_name1].shape # size of the first data set
    mesh = Smesh(len(size), size, output_name)
    file_write = """<?xml version=\"1.0\" ?>
<!DOCTYPE Xdmf SYSTEM \"Xdmf.dtd\" []>
<Xdmf Version=\"2.0\">
<Domain>
<Grid Name=\"CellTime\" GridType=\"Collection\" CollectionType=\"Temporal"\>
    <Grid Name=\"mesh1\" GridType=\"Uniform\" CollectionType=\"Temporal"\>
    <Time Value = \"timed\" />
     """+ mesh.topology()+ mesh.coordinate_read() + ''.join([mesh.attribute_node(k) for k in list(opensbli_file.keys())])+"""   </Grid>\n</Domain>\n</Xdmf>\n"""
    with open('read.xdmf', 'w') as f:
        f.write(file_write) 
    return

def write_xdmf_top(output_name, timed):
    opensbli_file = h5py.File(output_name, 'r')
    block_name1 = list(opensbli_file.keys())[0]
    size =  opensbli_file[block_name1].shape # size of the first data set
    mesh = Smesh(len(size), size, output_name)
    file_write = """<?xml version=\"1.0\" ?>
<!DOCTYPE Xdmf SYSTEM \"Xdmf.dtd\" []>
<Xdmf Version=\"2.0\">
<Domain>
<Grid Name=\"CellTime\" GridType=\"Collection\" CollectionType="Temporal">
    <Grid Name=\"mesh1\" GridType=\"Uniform\">
    <Time Value = "%s" />
     """%(str(timed))+ mesh.topology()+ mesh.coordinate_read() + ''.join([mesh.attribute_node(k) for k in list(opensbli_file.keys())])+"""   </Grid>"""
    with open('read.xdmf', 'w') as f:
        f.write(file_write) 
    return

def write_xdmf_middle(output_name, timed):
    opensbli_file = h5py.File(output_name, 'r')
    block_name1 = list(opensbli_file.keys())[0]
    size =  opensbli_file[block_name1].shape # size of the first data set
    mesh = Smesh(len(size), size, output_name)
    file_write = """
    <Grid Name=\"mesh1\" GridType=\"Uniform\">
    <Time Value = "%s" />
     """ %(str(timed))+ mesh.topology()+ mesh.coordinate_read() + ''.join([mesh.attribute_node(k) for k in opensbli_file.keys()])+"""   </Grid>"""
    with open('read.xdmf', 'a') as f:
        f.write(file_write) 

def write_xdmf_bottom(output_name, timed):
    opensbli_file = h5py.File(output_name, 'r')
    block_name1 = list(opensbli_file.keys())[0]
    size =  opensbli_file[block_name1].shape # size of the first data set
    mesh = Smesh(len(size), size, output_name)
    file_write = """
    <Grid Name=\"mesh1\" GridType=\"Uniform\">
    <Time Value = "%s" />
     """%(str(timed))+ mesh.topology()+ mesh.coordinate_read() + ''.join([mesh.attribute_node(k) for k in opensbli_file.keys()])+"""  </Grid>\n </Grid>\n</Domain>\n</Xdmf>\n"""
    with open('read.xdmf', 'a') as f:
        f.write(file_write) 
    
if(__name__ == "__main__"):
    # Parse the command line arguments provided by the user, Teo paths should be provided
    # parser = argparse.ArgumentParser(prog="pat")
    # parser.add_argument("input_path", help="Path of the HDF5 file written out from OpenSBLI inlcuding the file name", action="store", type=str)
    # args = parser.parse_args()
    # print "Processing HDF5 from the path %s"%args.input_path
    # a = args.input_path.split('/')
    # if '.h5' not in a[-1]:
    #     raise ValueError("Provide the HDF5 file with .h5 extension")
    

    dir_path = '/Users/maxwalker/git/opensbli/apps/gaussian_bump/gaussian_bump_200x200/output/'
    dir_path = sys.argv[1]
    new_path = dir_path

    # empty list to store files
    h5files = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            h5files.append(path)


    timeseries = [s.replace('opensbli_output_', '') for s in h5files]
    timeseries = [s.replace('.h5', '') for s in timeseries]


    timeseries = list(map(int, timeseries))
    mintim, maxtim = np.min(timeseries), np.max(timeseries)
    # os.remove(read)

    # print(timeseries)

    for i in range(0,len(timeseries)):

        it = timeseries[i]
        apath = dir_path  + h5files[i]
        a = h5files[i]

        if it == mintim:
            # h5name_output = a[-2:-1].split('.')[0]
            h5name_output = a.replace('.h5', '')
            # output_name = '/'.join(a[:-1]+['%s_pp.h5'%h5name_output])
            output_name = new_path + '%s_pp.h5'%h5name_output

            strip_halos(apath, output_name)
            write_xdmf_top(output_name, it) 

        elif it == maxtim:
            # h5name_output = a[-2:-1].split('.')[0]
            h5name_output = a.replace('.h5', '')
            # output_name = '/'.join(a[:-1]+['%s_pp.h5'%h5name_output])
            output_name =  new_path + '%s_pp.h5'%h5name_output
            strip_halos(apath, output_name)
            write_xdmf_bottom(output_name, it)

        else:
            # h5name_output = a[-2:-1].split('.')[0]
            h5name_output = a.replace('.h5', '')
            print(h5name_output)
            # output_name = '/'.join(a[:-1]+['%s_pp.h5'%h5name_output])
            output_name = new_path + '%s_pp.h5'%h5name_output
            strip_halos(apath, output_name)
            write_xdmf_middle(output_name, it)
