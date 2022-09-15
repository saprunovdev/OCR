import preprocessing as prep
import upscale as up
import number_detection as nd
import cv2
import argparse
import keras_ocr
import os
import json

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])

# PREPROCESSING
# For better results change upscale to x3 or x4
img = up.upscale_x2(img) #upscale_x3, upscale_x4
img = prep.grayscale(img)
img = prep.noise_removal(img)
bw = prep.image_smoothening(img) 

# we save the preprocessed image here, so we can open in with keras library. Otherwise it just won't work.
cv2.imwrite('temp/pre.jpg', bw)
img = [keras_ocr.tools.read('temp/pre.jpg'), keras_ocr.tools.read('temp/pre.jpg')]

# Detecting numbers and coordinates
pipeline = keras_ocr.pipeline.Pipeline()
prediction_groups = pipeline.recognize(img)
data = nd.ocr(img)

# Clearing out the data and forming json file
text_array = []
coordinates_array = []
for text, coordinates in data:
    text_array.append(text)
    coordinates_array.append(coordinates.tolist())

dict_data = dict(zip(text_array, coordinates_array))
    
with open(str(args.values()).split("/")[-1].split(".")[0], 'w') as fp:
    json.dump(dict_data, fp)