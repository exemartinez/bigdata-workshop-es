import numpy as np
import h5py
import os

hf = h5py.File('./dataset/trainingsetv1d1.h5', 'r')
print(list(hf.keys()))

# &&
print(hf.values)
lines = hf.get('1080Lines')

lines.