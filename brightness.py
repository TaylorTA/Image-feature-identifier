from PIL import Image, ImageStat
import requests
from io import BytesIO
import math


def get_brightness(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    stat = ImageStat.Stat(img)
    print(img)
    r,g,b = stat.rms
    brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    #For return values > 120.0 I consider the image to be bright, otherwise - not. And ~ 200.0 would be super-bright, ~ 20.0 - super dark.
    return brightness
