#!/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1], sep=',')

print(df)

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(np.cumsum(df['AssemblyTime']), marker='.', label='cumulative assembly')
ax.plot(np.cumsum(df['LinearSolverTime']), marker='x', label='cumulative linear solver')

ax.legend()
ax.set_title('Runtime on core ' + str(sys.argv[2]) + ' of ' + str(sys.argv[3]) + ' for Fractured Cube Example (' + str(sys.argv[4]) + ')')
ax.set_xlabel('linear iterations number')
ax.set_ylabel('time in s')
ax.grid(True, linestyle='-.')
#ax.set_yscale('log')
plt.show()

