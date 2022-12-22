# -*- coding: utf-8 -*-
"""Pertemuan 9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fVq4nxQtqCNGk4YHB0VhPn3KPj6JIXfR
"""

import numpy as np
import math

class filtering:
  def __init__(self,img,tipe_filter,kernel=None):
    self.img = img
    self.tipe = tipe_filter
    self.kernel = kernel

  def filter(self):
    self._kernel_selection()
    return self._konvolusi()

  def _kernel_selection(self):
    if self.tipe == 'highpass':
      if self.kernel.any() != None:
        self.kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    elif self.tipe == 'lowpass':
      if self.kernel.any() != None:
        self.kernel = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

  def _konvolusi(self):
    # jumlah padding
    pad_size = math.floor(self.kernel.shape[0]/2)
    # buat gambar baru
    img_padd = np.zeros((self.img.shape[0]+2*pad_size,self.img.shape[1]+2*pad_size))
    # gambar lama masuk ke gambar berpadding
    for r in range(self.img.shape[0]):
      for c in range(self.img.shape[1]):
        img_padd[r+pad_size,c+pad_size] = self.img[r,c]
    # apply konvolusi
    img_akhir = np.zeros((self.img.shape[0],self.img.shape[1]))
    for r in range(img_akhir.shape[0]):
      for c in range(img_akhir.shape[1]):
        for i in range(self.kernel.shape[0]):
          for j in range(self.kernel.shape[1]):
            img_akhir[r,c] += self.kernel[i,j]*img_padd[r+i,c+j]
    return self._clipping(img_akhir)
  
  def _clipping(self,img,max=1,min=0):
    img_c = np.zeros((img.shape[0],img.shape[1]))
    for r in range(img.shape[0]):
      for c in range(img.shape[1]):
        if img[r,c] > max:
          img_c[r,c] = max
        elif img[r,c] < min:
          img_c[r,c] = min
        else:
          img_c[r,c] = img[r,c]
    return img_c

from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


url ="https://tinyjpg.com/images/social/website.jpg"
img = io.imread(url)
img_libgray = rgb2gray(img)

kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
img_filter = filtering(img_libgray,'highpass',kernel).filter()

plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(img_libgray,cmap=plt.cm.gray)
plt.figure()
plt.imshow(img_filter,cmap=plt.cm.gray)

import numpy as np
import math

class filtering:
  def __init__(self,img,tipe_filter,kernel=None):
    self.img = img
    self.tipe = tipe_filter
    self.kernel = kernel

  def filter(self):
    self._kernel_selection()
    return self._konvolusi()

  def _kernel_selection(self):
    if self.tipe == 'highpass':
      if self.kernel.any() != None:
        self.kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    elif self.tipe == 'lowpass':
      if self.kernel.any() != None:
        self.kernel = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

  def _konvolusi(self):
    # jumlah padding
    pad_size = math.floor(self.kernel.shape[0]/2)
    # buat gambar baru
    img_padd = np.zeros((self.img.shape[0]+2*pad_size,self.img.shape[1]+2*pad_size))
    # gambar lama masuk ke gambar berpadding
    for r in range(self.img.shape[0]):
      for c in range(self.img.shape[1]):
        img_padd[r+pad_size,c+pad_size] = self.img[r,c]
    # apply konvolusi
    img_akhir = np.zeros((self.img.shape[0],self.img.shape[1]))
    for r in range(img_akhir.shape[0]):
      for c in range(img_akhir.shape[1]):
        for i in range(self.kernel.shape[0]):
          for j in range(self.kernel.shape[1]):
            img_akhir[r,c] += self.kernel[i,j]*img_padd[r+i,c+j]
    return self._clipping(img_akhir)
  
  def _clipping(self,img,max=1,min=0):
    img_c = np.zeros((img.shape[0],img.shape[1]))
    for r in range(img.shape[0]):
      for c in range(img.shape[1]):
        if img[r,c] > max:
          img_c[r,c] = max
        elif img[r,c] < min:
          img_c[r,c] = min
        else:
          img_c[r,c] = img[r,c]
    return img_c

from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


url ="https://tinyjpg.com/images/social/website.jpg"
img = io.imread(url)
img_libgray = rgb2gray(img)

kernel = np.array([[-2,-2,-2],[-2,15,-2],[-2,-2,-2]])
img_filter = filtering(img_libgray,'lowpass',kernel).filter()

plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(img_libgray,cmap=plt.cm.gray)
plt.figure()
plt.imshow(img_filter,cmap=plt.cm.gray)