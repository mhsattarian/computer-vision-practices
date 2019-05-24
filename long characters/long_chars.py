import cv2
import numpy as np

img = cv2.imread('passage.jpg', 0)

length = 15
SE = np.ones((length, 1), np.uint8)

ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
mask = cv2.erode(binary_img, SE, iterations=1)

cv2.imshow("mask", mask)

SE = np.ones((3, 3), np.uint8)

old_mask = mask
mask = cv2.dilate(mask, SE, iterations=1)
mask = cv2.bitwise_and(binary_img, mask)
print (np.count_nonzero(np.bitwise_xor(old_mask, mask)))
while np.count_nonzero(np.bitwise_xor(old_mask, mask)) is not 0:
  old_mask = mask
  mask = cv2.dilate(mask, SE, iterations=1)
  mask = cv2.bitwise_and(binary_img, mask)
  print(np.count_nonzero(mask))

cv2.imshow('long characters', mask)
cv2.imwrite('longchars-output.jpg', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
