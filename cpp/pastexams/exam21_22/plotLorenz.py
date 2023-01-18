import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv

data = []
with open('./data.txt') as f:                                                                                          
    lines = csv.reader(f, delimiter='\t')
    for i in lines:
   	    data.append(i)
        
print(np.shape(data))

fig, ax = plt.subplots(1,1)
ax.plot(int(data[:][0]), int(data[:][1]))

plt.show()