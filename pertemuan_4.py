# -*- coding: utf-8 -*-
"""Pertemuan 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14zRKJEgyWO_ye8OmHDDzyhkugag1KI5v

## **Grayscaling**
![image.png](data:image/png;base64,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)
"""

from skimage import io
import matplotlib.pyplot as plt

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")

plt.figure()
plt.imshow(img)

print(img.shape)

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]
#menggunakan perhitungan manual
img_gray = (img_red+img_green+img_blue)/3

#untuk menampilkan gambar dengan warna gray
plt.figure()
plt.imshow(img_gray,cmap=plt.cm.gray)

#menggunakan library 

plt.figure()
plt.imshow(img_gray,cmap=plt.cm.Greys)

plt.figure()
plt.imshow(img_red,cmap=plt.cm.Reds)
#melihat histogram 
plt.figure()
plt.hist(img_red.flatten(),bins=256)


plt.figure()
plt.imshow(img_blue,cmap=plt.cm.Blues)
#melihat histogram 
plt.figure()
plt.hist(img_blue.flatten(),bins=256)

plt.figure()
plt.imshow(img_green,cmap=plt.cm.Greens)
#melihat histogram 
plt.figure()
plt.hist(img_green.flatten(),bins=256)



from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")

plt.figure()
plt.imshow(img)

print(img.shape)

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]
#menggunakan perhitungan manual
img_gray = (img_red+img_green+img_blue)/3

#untuk menampilkan gambar dengan warna gray
plt.figure()
plt.imshow(img_gray,cmap=plt.cm.gray)

#menggunakan library 
img_library= rgb2gray(img)
plt.figure()
plt.imshow(img_library,cmap=plt.cm.gray)

#menggunakan perhitungan manual dengan rumus berbeda
img_newg = 0.2125 * img_red + 0.7154 * img_green + 0.0721 * img_blue
plt.figure()
plt.imshow(img_newg,cmap=plt.cm.gray)

"""**Latihan**"""

import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np

def quan(img):
  img_q = np.zeros((img.shape[0],img.shape[1]))
  for r in range (0,img.shape[0]):
    for c in range (0,img.shape[1]):
      if img[r,c] > 100:
        img_q[r,c] = 255
      else:
        img_q[r,c] = 0
  return img_q

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")
img_gray = rgb2gray(img)*255
img_quant = quan(img_gray)

plt.imshow(img_quant,cmap=plt.cm.gray,vmin=0, vmax=255)

"""**Binerisasi**"""

from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")

plt.figure()
plt.imshow(img)

print(img.shape)

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]

#menggunakan perhitungan manual dengan rumus berbeda
img_newg = 0.2125 * img_red + 0.7154 * img_green + 0.0721 * img_blue
plt.figure()
plt.imshow(img_newg,cmap=plt.cm.gray)

#binerisasi

def binerisasi(img) :
  img_q = np.zeros((img.shape[0],img.shape[1]))
  for r in range(0,img.shape[0]):
    for c in range (0,img.shape[1]):
      if img[r,c] < 128:
        img_q[r,c]= 0
      else:
        img_q[r,c] = 255

  return img_q

img_biner = binerisasi(img_newg)
plt.figure()
plt.imshow(img_biner,cmap=plt.cm.gray)

"""**Histogram image**"""

from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")

plt.figure()
plt.imshow(img)

print(img.shape)

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]

#menggunakan perhitungan manual dengan rumus berbeda
img_newg = 0.2125 * img_red + 0.7154 * img_green + 0.0721 * img_blue
plt.figure()
plt.imshow(img_newg,cmap=plt.cm.gray)

#melihat histogram 
plt.figure()
plt.hist(img_newg.flatten(),bins=256)

from skimage import io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from skimage.filters import threshold_mean
import numpy as np

img = io.imread("https://cdn06.pramborsfm.com/storage/app/media/Prambors/Editorial/mario%20bros%20-20210924085947.jpg?tr=w-800")

plt.figure()
plt.imshow(img)

print(img.shape) 

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]

#menggunakan perhitungan manual dengan rumus berbeda
img_newg = 0.2125 * img_red + 0.7154 * img_green + 0.0721 * img_blue
plt.figure()
plt.imshow(img_newg,cmap=plt.cm.gray)

#binerisasi

def binerisasi(img,threshold) :
  img_q = np.zeros((img.shape[0],img.shape[1]))
  for r in range(0,img.shape[0]):
    for c in range (0,img.shape[1]):
      if img[r,c] < threshold:
        img_q[r,c]= 0
      else:
        img_q[r,c] = 255

  return img_q

img_biner = binerisasi(img_newg,128)
plt.figure()
plt.imshow(img_biner,cmap=plt.cm.gray)

#thresohld pakai library

plt.figure( )
threshold = threshold_mean(img_newg)
print(threshold)
img_libbiner =binerisasi(img_newg,threshold)
plt.figure()
plt.imshow(img_libbiner,cmap=plt.cm.gray)