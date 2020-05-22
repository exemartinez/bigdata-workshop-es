#!/bin/bash
apt-get update && \
apt-get --no-install-recommends --no-install-suggests install -y python3 python3-pip python3-setuptools python3-distutils
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10 
pip3 install --no-cache-dir --default-timeout=120 -r /tmp/requirements.txt 
apt-get autoremove -y 
rm -rvf /tmp/requirements.txt /var/lib/apt/lists/* 
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -P /tmp/ 
bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b 
eval "$(/root/miniconda3/bin/conda shell.bash hook)" 
conda init 
conda update -n base -c defaults conda 
conda config --add channels conda-forge 
conda env create --file /tmp/igwn-py37.yaml 
conda activate igwn-py37 
conda install gwosc=0.5.3 
conda install pyarrow -y
conda install findspark -y
conda install matplotlib -y 
conda install seaborn -y
conda install wheel -y
conda install gensim -y
ipython kernel install --user --name=igwn-py37 
apt-get autoremove -y 
rm -rvf /tmp/requirements.txt /tmp/igwn-py37.yaml /var/lib/apt/lists/* 