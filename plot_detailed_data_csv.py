#!/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1], sep=' ')

fig, ax = plt.subplots(figsize=(8, 5))

print(df)

#ax.plot(df.iloc[:,0], np.cumsum(df.iloc[:,9]), marker='o')
ax.plot(df.iloc[:,0], df.iloc[:,9], marker='o')

ax.legend()
#ax.set_title('Runtime for Fractured Cube Example (ref2)')
ax.set_xlabel(df.columns.values[0])
ax.set_ylabel(df.columns.values[9] + ' in s')
#ax.grid() #True, linestyle='-.')
#ax.set_yscale('log')
plt.show()

