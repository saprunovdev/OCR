# OCR API

## Description
After executing this script you will get json file with numbers and their coordinates.
The file will appear in the OCR directory.

## Getting Started

HOW TO INSTALL

### Installing

* Clone this repository to your machine
* Download and install conda on your machine
* Go to the OCR directory in terminal and run this
```
conda create -n venv
source activate venv
conda install pip
pip install -r requirements.txt
```

### Executing program

* Move to OCR directory
* Write this to execute the script
* replace "path-to-the-image" with actuall path: (ex. iamges/img.png) 
```
python api.py -i path-to-the-image
```
