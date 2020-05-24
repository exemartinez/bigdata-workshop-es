'''
Author: Ezequiel H. Martinez
This script just generates a csv file with the dataframe that we will need as a parquet fortmat later.
'''

import numpy as np
import findspark

findspark.init() #this allows us to find the libs for the usage of spark.

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import h5py
import os
import pandas as pd
from gwpy.timeseries import TimeSeries

#load up the hd5f dataset provided by Gravity Spy.
hd5f_file='/dataset/trainingsetv1d1.h5'

hf = h5py.File(hd5f_file, 'r')

#first, we get the dataframe in pandas with all the headers for the data.
csv = '/dataset/trainingset_v1d1_metadata.csv'
parquet='/dataset/gw_gravity_spy_dataframe.parquet'
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
    
    png = np.reshape(png,23800).tolist()  #we place the whole image in just one dimension array. 140x170 (remember this)
    
    gwdf.at[index, 'png'] = png

    print("Record #%s processed" % str(index))

print("Main procedures finished. Saving...")

findspark.init()
spark = SparkSession.builder.appName("pyspark-gw").getOrCreate()

sqlCtx = SQLContext(spark)
sdf = sqlCtx.createDataFrame(gwdf) #getting a spark dataframe out of a Pandas dataframe.   

# We use the spark dataset to write its contents (all the gravity spy's dataset) to a partquet file for easy classification. 
sdf.write.parquet(parquet)

print("File saved as parquet." + parquet)