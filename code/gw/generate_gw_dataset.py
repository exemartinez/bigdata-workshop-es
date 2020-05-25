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

findspark.init()
spark = SparkSession.builder.appName("pyspark-gw").getOrCreate()
sqlCtx = SQLContext(spark)

#forming a new dataset - for everyblock block
block_number = 1
block = 1138
begin = 0
end = block * block_number
all_records = 7966

for block_init in range(begin, all_records, block): # will process 7 different blocks

    gwdf = df[block_init:block_init+block] #we reduce the set of data to test the algorithm at a fast rate.

    print("Processing block {0} to {1}...as parquet.".format(block_init, block_init + block))

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

    print("Main procedures finished. Saving block...")

    sdf = sqlCtx.createDataFrame(gwdf) #getting a spark dataframe out of a Pandas dataframe.   

    # We use the spark dataset to write its contents (all the gravity spy's dataset) to a partquet file for easy classification. 
    sdf.write.format("parquet") \
    .partitionBy("gravityspy_id","sample_type") \
    .option("path", "/dataset/gw_gravity_spy_dataframe_" + block_init) \
    .mode("overwrite") \
    .saveAsTable("gw_gravity_spy" + block_init)    
    
    print("File saved block {0} to {1}...as parquet.".format(block_init, block_init + block))