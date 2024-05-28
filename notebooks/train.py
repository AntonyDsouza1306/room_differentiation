import os
import urllib.request
# Clone and set up keras-retinanet

import tensorflow as tf
tf.test.gpu_device_name()

# Download pretrained model
PRETRAINED_MODEL = 'keras-retinanet/snapshots/_pretrained_model.h5'
URL_MODEL = 'https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5'
urllib.request.urlretrieve(URL_MODEL, PRETRAINED_MODEL)

# Set pretrained model path
PRETRAINED_MODEL = '/content/snapshots/resnet50_csv_11.h5'

# Train the model
os.system(f'keras-retinanet/keras_retinanet/bin/train.py --freeze-backbone --weights {PRETRAINED_MODEL} --initial-epoch 8 --weighted-average --batch-size 16 --steps 247 --snapshot-path /content/snapshots --image-min-side 250 csv /content/data/annotation/train.csv /content/data/classes/classes.csv')