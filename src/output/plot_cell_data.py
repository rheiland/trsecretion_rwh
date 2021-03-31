#
# plot_cell_data.py:  plot a cell's custom data value over time
#
# Usage:
#  python plot_cell_data.py <...>
#    i.e., the arguments <...> are optional and have defaults.
# 
# Dependencies include matplotlib and numpy. We recommend installing the Anaconda Python3 distribution.
#
# Examples (run from directory containing the .xml and .mat files):
#  python 
#
# Author: Randy Heiland 
#
__author__ = "Randy Heiland"

import sys
import glob
import os
import xml.etree.ElementTree as ET
import math
from pyMCDS import pyMCDS
#join_our_list = "(Join/ask questions at https://groups.google.com/forum/#!forum/physicell-users)\n"
join_our_list = "( Submit a ticket at https://sourceforge.net/p/physicell/tickets/)\n"
try:
  import matplotlib
  import matplotlib.colors as mplc
  from matplotlib.patches import Circle, Ellipse, Rectangle
  from matplotlib.collections import PatchCollection
except:
  print("\n---Error: cannot import matplotlib")
  print("---Try: python -m pip install matplotlib")
  print(join_our_list)
#  print("---Consider installing Anaconda's Python 3 distribution.\n")
  raise
try:
  import numpy as np  # if mpl was installed, numpy should have been too.
except:
  print("\n---Error: cannot import numpy")
  print("---Try: python -m pip install numpy\n")
  print(join_our_list)
  raise
from collections import deque
try:
  # apparently we need mpl's Qt backend to do keypresses 
#  matplotlib.use("Qt5Agg")
  matplotlib.use("TkAgg")
  import matplotlib.pyplot as plt
except:
  print("\n---Error: cannot use matplotlib's TkAgg backend")
  print(join_our_list)
#  print("Consider installing Anaconda's Python 3 distribution.")
  raise


current_idx = 0
print("# args=",len(sys.argv)-1)

xml_files = glob.glob('output*.xml')
xml_files.sort()
#print(xml_files)
#for current_idx in range(len(svg_files)):

#mcds = pyMCDS(xml_files[0], '.')  # first file
mcds = pyMCDS(xml_files[-1], '.')  # last file
print(mcds.data.keys())
# Now our data lives in:
#mcds.data

#tval = mcds.get_time()

ds_count = len(xml_files)
# print("----- ds_count = ",ds_count)
mcds = [pyMCDS(xml_files[i], '.') for i in range(ds_count)]
tval = np.linspace(0, mcds[-1].get_time(), len(xml_files))

#cell_ids = mcds.data['discrete_cells']['ID'].astype(int)
print('cell_ids = ',cell_ids)
print()
cell_vars = mcds.get_cell_variables()
print('cell_vars = ',cell_vars)

#val = mcds.data['discrete_cells']['assembled_virion']
val = mcds.data['discrete_cells']['internal_chemical_A']
print(val)
#sum = val.sum()
#print("sum = ",sum)

x=[]
y=[]
for fname in xml_files:
  mcds = pyMCDS(fname, '.')  # last file
  tval = mcds.get_time()
  x.append(tval)
#  val = mcds.data['discrete_cells']['assembled_virion']
  val = mcds.data['discrete_cells']['internal_chemical_A']
#  y.append(val.sum())

# fig, ax = plt.subplot(1, figsize=(6,4))
# ax.plot(x,y)
plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("internal_chemical_A")
#ax.set_xlabel('time')
#ax.set_ylabel('')
# keep last plot displayed
#plt.ioff()
plt.show()
