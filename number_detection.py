import matplotlib.pyplot as plt
import keras_ocr
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# img = [keras_ocr.tools.read('upscaled/bw_image.jpg'), keras_ocr.tools.read('upscaled/bw_image.jpg')]

def ocr(img):
    pipeline = keras_ocr.pipeline.Pipeline()
    prediction_groups = pipeline.recognize(img)

    # Plot the predictions
    # fig, axs = plt.subplots(nrows=len(image), figsize=(20, 20))
    # for ax, image, predictions in zip(axs, image, prediction_groups):
    #     keras_ocr.tools.drawAnnotations(image=image, predictions=prediction_groups[0], ax=ax)

    # plt.show()
    return prediction_groups[0] 
    

# data = ocr(img)

# for text, coordinates in data:
#     print(text)
#     print(coordinates)



