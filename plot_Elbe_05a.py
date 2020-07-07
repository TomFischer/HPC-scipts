#!/bin/python

# #Modelname Nodes Elements Cores Runtime_in_s
# Elbe_05a_3layer 28411320 42571932 960 2022
# Elbe_05a_4layer 35516150 56762576 960 2706
# Elbe_05a_5layer 42616980 70953220 960 3236
# Elbe_05a_6layer 49719810 85145864 960 3833

import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1], sep=' ')

fig, ax = plt.subplots(figsize=(8, 5))

print(df)

ax.plot(df.iloc[:,1]/1000000, df.iloc[:,4]/60, marker='o')

#ax.legend()
ax.set_title('Runtime for Elbe Catchment Model (Elbe_05a) with Different Number of Layers')
ax.set_xlabel('$\\times 10^6$ mesh nodes')
ax.set_ylabel('runtime in minutes')
ax.grid() #True, linestyle='-.')

for i in range(0, len(df)):
    text_label=df['#Modelname'][i]
    x=df['Nodes'][i]/1000000
    y=df['Runtime_in_s'][i]/60
    yshift=3
    if i == 3:
        yshift = -3
    ax.annotate(text_label, xy=(x, y),  xycoords='data',
                    xytext=(x, y+yshift), textcoords='data',
                    arrowprops=dict(arrowstyle='-', edgecolor='white', facecolor='white'),
                    horizontalalignment='center',
                    verticalalignment='top', color='blue' #, rotation=90,
                    #ha="right", rotation_mode="anchor"
                    )

#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")

plt.show()

fig.savefig('Elbe_05a_runtimes.pdf')
