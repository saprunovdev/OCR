import cv2
from cv2 import dnn_superres

#This part of code enhances the image resolution 
def upscale_x2(img):
    # Create a super resolution object
    sr = dnn_superres.DnnSuperResImpl_create()
    # Read the desired model
    path = 'models/EDSR_x2.pb'
    sr.readModel(path)
    # Set the desired model and scale to get correct pre- and post-processing 
    sr.setModel('edsr', 2)
    return sr.upsample(img)

def upscale_x3(img):
    # Create a super resolution object
    sr = dnn_superres.DnnSuperResImpl_create()
    # Read the desired model
    path = 'models/EDSR_x3.pb'
    sr.readModel(path)
    # Set the desired model and scale to get correct pre- and post-processing 
    sr.setModel('edsr', 3)
    return sr.upsample(img)

def upscale_x4(img):
    # Create a super resolution object
    sr = dnn_superres.DnnSuperResImpl_create()
    # Read the desired model
    path = 'models/EDSR_x4.pb'
    sr.readModel(path)
    # Set the desired model and scale to get correct pre- and post-processing 
    sr.setModel('edsr', 4)
    return sr.upsample(img)

