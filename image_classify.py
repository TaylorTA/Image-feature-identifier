from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
import numpy as np
from PIL import Image
import os
from io import BytesIO
import requests

def image_classify(url):
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

    model = VGG16(weights='imagenet', include_top = True)

    # img_path = 'car.jpg'
    # img = image.load_img(img_path, target_size=(224, 224))
    # print(type(img))
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    # x = np.resize(x,(224,224,3))
    # print(model.fit())
    # print(model.summary())
    features = model.predict(x)
    label = decode_predictions(features)
    return label
