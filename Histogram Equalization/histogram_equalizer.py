#!/usr/bin/python3
import cv2
import numpy as np
import click
from histogram_normalizer import Histogram_normalizer


class Histogram_equalizer:
  def __init__(self, image, plot=False):
    if type(image) == str: image = cv2.imread(image, 0)

    self.normalizedHist = Histogram_normalizer(image).get()
    # Could also use this:
    # image_histogram, bins = np.histogram(image.flatten(), 255, [0,255], density=True)

    cdf = self.normalizedHist.cumsum() # cumulative distribution function
    print(self.normalizedHist)
    print(cdf)
  
  def get(self):
    pass





Histogram_equalizer('gama_0.5.jpg')

