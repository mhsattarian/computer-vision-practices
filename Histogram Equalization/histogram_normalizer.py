#!/usr/bin/python3
import cv2
import numpy as np
import click
import matplotlib.pyplot as plt

class Histogram_normalizer:
  def __init__(self, image, plot=False):
    if type(image) == str: image = cv2.imread(image, 0)

    hist, _ = np.histogram(image.flatten(), 255, [0,255])
    h, w = image.shape
    normalizedHist = np.divide(hist, h * w)

    if plot:
      plt.figure(1)
      plt.subplot(211)
      plt.plot(hist, color = 'b')
      plt.subplot(212)
      plt.plot(normalizedHist, color = 'r')
      plt.show()
    
    self.normalizedHist = normalizedHist
  
  def get(self):
    return self.normalizedHist


# a = Histogram_normalizer('gama_0.5.jpg').get()