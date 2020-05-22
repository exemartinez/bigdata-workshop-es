'''
Author: Ezequiel H. Martinez
This script just generates a csv file with the dataframe that we will need as a parquet fortmat later.
'''

import numpy as np
import h5py
import os
import pandas as pd
from gwpy.timeseries import TimeSeries

#load up the hd5f dataset provided by Gravity Spy.
hd5f_file='/dataset/trainingsetv1d1.h5'

hf = h5py.File(hd5f_file, 'r')

#first, we get the dataframe in pandas with all the headers for the data.
csv = '/dataset/trainingset_v1d1_metadata.csv'
df=pd.read_csv(csv, sep=',',header=0)

#forming a new dataset
gwdf = df

gvtyid = 21
labelid = 22
sampleid=23

gwdf.shape[0]
gwdf['png'] = ''

print("The shape of the matrix to be processed is %s" % str(gwdf.shape))

for index, record in gwdf.iterrows():
    gravityspy_id= record[gvtyid]
    label= record[labelid]
    sample_type= record[sampleid]
    
    png = np.array(hf[label][sample_type][gravityspy_id]['0.5.png'][0])
    
    png = np.reshape(png,23800) #we place the whole image in just one dimension array.
    
    gwdf.at[index, 'png'] = png

    print("Record #%s processed" % str(index))

print("Main procedures finished. Saving...")

gwdf.to_pickle('/dataset/gw_gravity_spy_dataframe.pickle')   

print("File saved.")