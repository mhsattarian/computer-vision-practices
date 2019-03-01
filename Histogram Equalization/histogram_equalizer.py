#!/usr/bin/python3
import cv2
import numpy as np
import click

class Histogram_equalizer:
  



if __name__ == '__main__':

  s = Steganography()

  CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
  @click.group(context_settings=CONTEXT_SETTINGS)
  def cli():
      """Hide an image within another"""

  @cli.command('encode', short_help='Encode an image within another')
  @click.argument('container', type=click.Path(exists=True))
  @click.argument('containee', type=click.Path(exists=True))
  @click.option('-o', '--out', help="Specify output file", default="output.png")
  @click.option('--show', help="Display output image", is_flag=True)
  def encode(container, containee, out, show):
    """Encode containee within container"""
    output = s.encode_images(container, containee)
    if show: 
      cv2.imshow("output", output)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    cv2.imwrite(out, output)
    print("- output stored.")

  @cli.command('decode', short_help='Extracts encoded image')
  @click.argument('image', type=click.Path(exists=True))
  @click.option('-o', '--out', help="Specify output file", default="extracted.png")
  @click.option('--show', help="Display output image", is_flag=True)
  def decode(image, out, show):
    """Decode an image and store the extracted image"""
    codedImage = s.decode_image(image)
    if show: 
      cv2.imshow("extracted", codedImage)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    cv2.imwrite(out, codedImage)
    print("- extracted image stored.")


  MainHeader = '''  '''
  print(MainHeader)

  cli()

  # cv2.imshow("container", container)
  # cv2.waitKey(0)
  # cv2.imshow("containee", containee)
  # cv2.waitKey(0)
  # cv2.imshow("output", output)
  # cv2.waitKey(0)
  
