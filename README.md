# Image-feature-identifier
ReadMe

-  main program in image_feature.py, the program runs normally in terminal. Internet and libraries (imageai, PIL, keras, numpy, io, request, json, openCV, tensorflow, etc.) required to run.

-  Standard input:
{
    "success": true,
    "data": {
        "images": [
           {
                            "_id": "5cf544dc2700ba024131348c",
                            "trailId": "5cf544a22700ba02413132c6",
                            "queryId": "5cf544dc2700ba024131348b",
                            "thumbSrc": "https://s-media-cache-ak0.pinimg.com/564x/4c/78/59/4c785917de453a83adcb3e71daecb380.jpg",
                            "src": "https://s-media-cache-ak0.pinimg.com/564x/4c/78/59/4c785917de453a83adcb3e71daecb380.jpg",
                            "height": null,
                            "width": null,
                            "timestamp": "2019-06-03T16:03:40.694Z",
                            "__v": 0
                        }
        ]
    }
}

Modify line 83 in image_feature.py to modify input file name.

-  Standard output:
		{
                            "_id": "5cf544dc2700ba024131348c",
                            "trailId": "5cf544a22700ba02413132c6",
                            "queryId": "5cf544dc2700ba024131348b",
                            "thumbSrc": "https://s-media-cache-ak0.pinimg.com/564x/4c/78/59/4c785917de453a83adcb3e71daecb380.jpg",
                            "src": "https://s-media-cache-ak0.pinimg.com/564x/4c/78/59/4c785917de453a83adcb3e71daecb380.jpg",
                            "height": null,
                            "width": null,
                            "timestamp": "2019-06-03T16:03:40.694Z",
                            "__v": 0,
			    'features': {
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
-  Error: some libraries used in the program does not run on some specific url, reason unknown. Need to download the images and run it separately.


