#!/bin/bash
#Before processing any of the packages, run this script so the conda environment has all the remaining packages installed
# Run this "conda activate igwn-py37" in the bash shell before you run this script 
conda install pyarrow package -y
conda install findspark -y
conda install matplotlib -y 
conda install seaborn -y
conda install wheel -y
conda install gensim -y

