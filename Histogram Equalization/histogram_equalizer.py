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
    # self.normalizedHist, bins = np.histogram(image.flatten(), 255, [0,255], density=True)

    cdf = self.normalizedHist.cumsum() # cumulative distribution function
    cdf = 255 * cdf

    self.equalizedHist = cdf
    bins = [i for i in range(0, 256)]
    # use linear interpolation of cdf to find new pixel values
    self.equalizedImage = np.interp(image.flatten(), bins[:-1], cdf).reshape(image.shape)
    
  def get(self):
    return self.equalizedImage, self.equalizedHist


# a, b = Histogram_equalizer('gama_0.5.jpg').get()
# print(a)
# print('\n')
# print(b)
# cv2.imwrite("test.png", a)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

