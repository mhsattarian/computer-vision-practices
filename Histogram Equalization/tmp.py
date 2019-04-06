import numpy as np
import cv2

def normalize_histogram(img):
    width, height = img.shape[:2]

    res = np.zeros(256)

    for i in range(width):
        for j in range(height):
            pix_res = img[i, j]
            res[pix_res] = res[pix_res] + 1

    num_pix = img.shape[0] * img.shape[1]
    res = res / num_pix
    
    return res

def equalize(img):
    norm_hist = normalize_histogram(img)
    equalized = np.zeros(256)

    for i in range(256):
        equalized[i] = np.sum(norm_hist[:i + 1])

    equalized = 255 * equalized
    equalized = np.around(equalized)

    return equalized
    
def match(eq_hist_inp, eq_hist_desired, img):
    new_img = np.zeros(shape=img.shape, dtype=int)

    width, height = img.shape[:2]
    for i in range(width):
        for j in range(height):
            pixel_val = np.where(eq_hist_desired == eq_hist_inp[img[i, j]][0])
            
            if np.array_equal(pixel_val[0], np.array([])) is False:
                new_img[i, j] = pixel_val[0][0]
            else:
                nearest = min(eq_hist_desired, key=lambda x:abs(x - eq_hist_inp[img[i, j]][0]))

                print(eq_hist_inp[img[i, j]][0], ' ' , nearest)
                new_img[i, j ] = nearest

    cv2.imwrite('eafa.jpg', new_img)

def main():
    img1 = cv2.imread('gama_0.2.jpg')
    img2 = cv2.imread('gama_0.5.jpg')

    eq_hist_inp = equalize(img1)
    eq_hist_desired = equalize(img2)
    
    match(eq_hist_inp, eq_hist_desired, img1)

main()