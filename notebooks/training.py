# -*- coding: utf-8 -*-
"""training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HYHWAmjq0DTI_SyxTAFQ1lLo4i2yiaMX
"""

import tensorflow as tf
tf.test.gpu_device_name()

#!pip install openimages

from downloadOI import DownloadOI

classes = ['Bookcase','Bathtub', 'Pillow' ,'Couch', 'Gas stove', 'Washing machine' ,'Bed',
 'Refrigerator', 'Bathroom accessory', 'Kitchen & dining room table',
 'Television' ,'Sink' ,'Sofa bed' ,'Kitchenware' ,'Toilet' ,'Ceiling fan',
 'Microwave oven', 'Furniture', 'Coffeemaker', 'Cupboard', 'Dishwasher',
 'Shower' ,'Clock' ,'Countertop' ,'Mug', 'Table']

data_path = 'content/data'
csv_path = 'content/data/files'
limit = 100

# Commented out IPython magic to ensure Python compatibility.
# %mkdir data
# %cd data
# %mkdir files
# %cd files
!wget https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv
!wget https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv
!wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-bbox.csv
!wget https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv
# %cd ..
# %cd ..

download_dataset = DownloadOI(classes, data_path, csv_path, limit)

download_dataset.form_dataset()

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/fizyr/keras-retinanet.git
# %cd keras-retinanet/
!pip install .
!python setup.py build_ext --inplace
# %cd ..

import urllib

PRETRAINED_MODEL = 'keras-retinanet/snapshots/_pretrained_model.h5'

URL_MODEL = 'https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5'
urllib.request.urlretrieve(URL_MODEL, PRETRAINED_MODEL)

PRETRAINED_MODEL = '/content/snapshots/resnet50_csv_11.h5'

!keras-retinanet/keras_retinanet/bin/train.py  --freeze-backbone --weights {PRETRAINED_MODEL} --initial-epoch 8 --weighted-average --batch-size 16 --steps 247 --snapshot-path /content/snapshots --image-min-side 250 csv /content/data/annotation/train.csv /content/data/classes/classes.csv

