import image_classify as i_c
import image_detection as i_d
import brightness as br
import color
from object_size import get_biggest_object_size
from saturation import get_image_saturation
from text_detection import contain_text_or_not
import json
import numpy as np
import codecs


def get_features(url):
    label = i_c.image_classify(url)
    label = label[0][0][1]
    print(label)

    # get objects and the number of  objects
    objects, objects_number = i_d.object_detection(url)
    for eachObject in objects:
        print(eachObject["name"], " : ", eachObject["percentage_probability"])
    print(objects_number)
    # objects = objects['name']
    newOb = []
    for each in objects:
        each = {key: each[key] for key in ['name']}
        newOb.append(each)
    print(objects)
    print(newOb)

    # get brightness
    # For return values > 120.0 I consider the image to be bright, otherwise - not.
    # And ~ 200.0 would be super-bright, ~ 20.0 - super dark.
    brightness = br.get_brightness(url)
    print(brightness)

    # get main color (ASCII value of the color) and decide the image is cool/warm
    colour_peak, colour = color.get_main_color(url)
    temp = ""
    if colour_peak[1] > colour_peak[0]:
        temp = "cool"
    else:
        temp = "warm"
    print(colour)
    print(temp)

    # get biggest object size
    biggest_object_size = get_biggest_object_size(url)
    print(biggest_object_size)

    # get image saturation
    # higher than 50 - colourful otherwise pale
    saturation = get_image_saturation(url)
    print(saturation)

    # whether the image contain text or not
    # 1 - yes
    # 0 - no
    text = contain_text_or_not(url)
    if text == 1:
        text = 'yes'
    else:
        text = 'no'

    print(text)

    data = {'features': {
            'label': label,
            'objects': newOb,
            'number of objects': objects_number,
            'brightness': brightness,
            'colour': colour,
            'temp': temp,
            'object size': biggest_object_size,
            'saturation': saturation,
            'text': text
            }
            }
    return data


# reading json input
with open("json/p5.json") as json_file: #load existing data
    json_data = json.load(json_file)

test = 'TestCase2'
result = json_data
images = result["data"]['images']
for each in images:
    url = each['thumbSrc']
    print(url)
    each.update(get_features(url))
    with open('instory-p16-imageData', 'a') as outfile:
        json.dump(each, outfile)




