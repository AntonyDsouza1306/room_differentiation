

## About Files

- app : This is the main directory which contains all the required files.
- scripts : Thie the directory which ontains python files used during training.
    - downloadOI : This is used to download images from Open Images Dataset and form proper annotation file as required by keras-retinanet.
- notebooks : Jupyter Notebooks that I used to to train the model.

## How to Use

To train the model first download the images from Open Images using scripts/downloadOI.py it will create a folder 'data' which contains three folders
1. images : this will contains all the images downloaded.
2. classes : this contains classes.csv file which is required by keras-retinanet.
3. annotation : this contains annotation files (train.csv, test.csv, validation.csv) which is required by keras-retinanet.

then used notebooks/training.ipynb file to train the model.
