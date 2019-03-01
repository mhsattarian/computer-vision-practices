#!/usr/bin/python3
import cv2
import numpy as np
import click
import os
import math

class Bit_plane_slicer:
  def __init__(self, imageColorBits = 8):
    # Assume Images have 8 bit to store colors
    self.imageColorBits = imageColorBits
  
  def get_remainder(self, image):
    return np.bitwise_and(image, 1)
  
  def slice(self, image):
    if type(image) == str: image = cv2.imread(image)

    imagePlanes = []
    for _ in range(self.imageColorBits):
      temp = self.get_remainder(image)
      imagePlanes.append(np.dot(temp, pow(2, self.imageColorBits)))
      image = np.right_shift(image,1)

    return imagePlanes

if __name__ == '__main__':

  s = Bit_plane_slicer()

  CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
  @click.group(context_settings=CONTEXT_SETTINGS)
  def cli():
      """Extract images plane slices"""

  @cli.command('slice', short_help='Encode an image within another')
  @click.argument('image', type=click.Path(exists=True))
  @click.option('-o', '--out', help="Specify output directory", default="slices")
  @click.option('--show', help="Display output image", is_flag=True)
  def slice(image, out, show):
    """Encode containee within container"""
    
    if not os.path.exists(out): os.makedirs(out)
    
    outputs = s.slice(image)

    for i, img in enumerate(outputs):
      if show: 
        cv2.imshow(f"slice_{i}", img)
        cv2.waitKey(0)
        print(img)
      cv2.imwrite(os.path.join(out, f"slice_{i}.png"), img)
    
    if show: cv2.destroyAllWindows()
    print("- slices are stored.")


  MainHeader = '''  '''
  print(MainHeader)

  cli()

  # cv2.imshow("container", container)
  # cv2.waitKey(0)
  # cv2.imshow("containee", containee)
  # cv2.waitKey(0)
  # cv2.imshow("output", output)
  # cv2.waitKey(0)
  
