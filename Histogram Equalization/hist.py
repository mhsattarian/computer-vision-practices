import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gama_0.5.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum() # cumulative distribution function
cdf_normalized = 255 * cdf / cdf[-1] 

# print(cdf_normalized)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
