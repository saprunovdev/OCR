import cv2
from matplotlib import pyplot as plt
import numpy as np

def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)   
    height, width, depth = im_data.shape

    figsize = width / float(dpi), height / float(dpi)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    ax.axis('off')
    ax.imshow(im_data, cmap='gray')
    plt.show()

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#this is the most important step  
def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, 220, 250, cv2.THRESH_BINARY)
    return th1

# Noise removal
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    kernel = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


# def thin_font(image):
#     image = cv2.bitwise_not(image)
#     kernel = np.ones((2,2), np.uint8)
#     image = cv2.erode(image, kernel, iterations = 1)
#     image = cv2.bitwise_not(image)
#     return(image)


# def thick_font(image):
#     image = cv2.bitwise_not(image)
#     kernel = np.ones((2,2), np.uint8)
#     image = cv2.dilate(image, kernel, iterations = 1)
#     image = cv2.bitwise_not(image)
#     return(image)


# def remove_boreders(image):
#     contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
#     cnt = cntsSorted[-1]
#     x, y, w, h = cv2.boundingRect(cnt)
#     crop = image[y:y+h, x:x+w]
#     return (crop)

