from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions
import numpy as np
from PIL import Image
import os
from io import BytesIO
import requests

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'

model = VGG19(weights='imagenet', include_top = True)

response = requests.get("https://i.pinimg.com/236x/5b/ca/de/5bcade6dd8e19cfc91458ecc66f97fc5.jpg")
img = Image.open(BytesIO(response.content))
img = img.resize((224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)
label = decode_predictions(features)
print(label)