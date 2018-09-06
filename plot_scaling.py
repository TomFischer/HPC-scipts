#!/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1])

fig, ax = plt.subplots(figsize=(8, 5))

last_index=len(df.iloc[:,0])
idealy = np.arange(1, df.iloc[last_index-1,0]/df.iloc[0,0]+1)
idealx = [x * df.iloc[0,0] for x in idealy]
ax.plot(idealx, idealy, 'k--', label='ideal')

s = df.iloc[0,1]
ax.plot(df.iloc[:,0], [s / x for x in df.iloc[:,1]], marker='o', label='gmres + jacobi')

ax.set_title('Scaling for Fractured Cube Example (ref2)')
ax.legend()
ax.set_xlabel(df.columns.values[0])
ax.set_ylabel('scaling $\\frac{t(920)}{t(N)}$')
ax.grid() #True, linestyle='-.')

fig.savefig('scaling_juwels.png', transparent=True)

plt.show()

