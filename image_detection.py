from imageai.Detection import ObjectDetection
import os
from skimage.io import imread


def object_detection(url):
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    img = imread(fname=url)
    detections = detector.detectObjectsFromImage(input_image= img, input_type="array", output_type= 'array')
    objects = detections[1]
    object_number = len(objects)
    # print(type(objects))
    return objects, object_number
