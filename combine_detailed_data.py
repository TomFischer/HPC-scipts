#!/usr/bin/env python

import sys
import pandas as pd

first_core=int(sys.argv[1])
last_core=int(sys.argv[2])

df = pd.read_csv(str(first_core) + '.txt')
df['core'] = first_core

for core in range(first_core+1, last_core+1):
    df_t = pd.read_csv(str(core) + '.txt')
    df_t['core'] = core
    df = df.append(df_t)

df.to_csv('complete_data.csv', ',')
print(df)
