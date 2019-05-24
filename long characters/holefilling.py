import cv2
import numpy as np

img = cv2.imread('passage.jpg', 0)
binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
binary_img_inv = cv2.bitwise_not(binary_img)
binary_img_cpy = (binary_img/255).astype('uint8')

# cv2.imshow('binary', binary_img)
# cv2.imshow('binary-inv', binary_img_inv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

height, width = img.shape
blank_img = np.zeros((height, width), np.uint8)
blank_img = blank_img[1:-1, 1:-1]


# Add one pixel white border
marker = cv2.copyMakeBorder(blank_img, top=1, bottom=1, left=1, right=1, borderType= cv2.BORDER_CONSTANT, value=[255])

SE = np.ones((5, 5), np.uint8)

old_marker = marker
marker = cv2.dilate(marker, SE, iterations=1)
marker = cv2.bitwise_and(binary_img_inv, marker)
print (np.count_nonzero(np.bitwise_xor(old_marker, marker)))
while np.count_nonzero(np.bitwise_xor(old_marker, marker)) is not 0:
  old_marker = marker
  marker = cv2.dilate(marker, SE, iterations=1)
  marker = cv2.bitwise_and(binary_img_inv, marker)
  print(np.count_nonzero(marker))

out = cv2.bitwise_not(marker)
cv2.imshow('output', out)
cv2.imwrite('holdefilling-output.png', out)
cv2.waitKey(0)
cv2.destroyAllWindows()