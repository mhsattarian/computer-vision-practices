import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys, os

# Importing histogram equalizer 
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Histogram Equalization'))
from histogram_equalizer import Histogram_equalizer


def high_freq_emp_filter(image):
    if type(image) == str: image = cv2.imread(image, 0)

    # Compute the 2-dimensional discrete Fourier Transform
    f = np.fft.fft2(image)
    # Shift the zero-frequency component to the center of the spectrum
    fshift = np.fft.fftshift(f)
    
    magnitudeSpectrum = 20 * np.log(np.abs(fshift))

    HG = np.zeros((fshift.shape))
    D0 = 40.0
    m1 = 0.5
    m2 = 0.75

    for u in range(fshift.shape[0]):
        for v in range(fshift.shape[1]):
            D = -1 * (((u - fshift.shape[0] / 2) ** 2) + ((v - fshift.shape[1] / 2) ** 2)) / (2 * (D0 ** 2))
            HG[u, v] = 1 - math.exp(D)
    
    highFreqEmpFilter = (m1 + m2 * HG) * fshift
    f_ishift = np.fft.ifftshift(highFreqEmpFilter)
    imgBackToTime = np.fft.ifft2(f_ishift)
    imgBackToTime = np.abs(imgBackToTime)
    imgBackToTime = np.around(imgBackToTime)
    imgBackToTime = imgBackToTime.astype(int)
    
    # Calculate the equalized histogram of input image
    result, _ = Histogram_equalizer(imgBackToTime).get()
    
    # Saving Result
    cv2.imwrite('magnitude_spectrum.jpg', magnitudeSpectrum)
    cv2.imwrite('img_returned_to_time.jpg', imgBackToTime)
    cv2.imwrite('img_returned_to_time_eq.jpg', result)

    # Saving a plot of comparision 
    plt.subplot(121)
    plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122)
    plt.imshow(result, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.savefig('plot.png')


# Running
img = cv2.imread('./chest_m.png', 0)
high_freq_emp_filter(img)