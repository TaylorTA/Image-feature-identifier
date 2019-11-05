from __future__ import print_function
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import requests
from io import BytesIO

NUM_CLUSTERS = 5

# print('reading image')
response = requests.get("https://www.popsci.com/sites/popsci.com/files/styles/1000_1x_/public/images/2018/01/snow.jpg?itok=XvQRJE7b&fc=50,50")
im = Image.open(BytesIO(response.content))
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

# print('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
# print('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
temp = "natural"

if peak[1] > peak[0]:
    temp = "cool"
else:
    temp = "warm"

print(temp)
