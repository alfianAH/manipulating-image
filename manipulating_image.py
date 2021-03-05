#!/usr/bin/env python3

from PIL import Image
import os

images_dir = os.path.join("images", "")
destination_dir = os.path.join("opt", "icons", "")


def convert_images(file_name):
    """
    Rotate, resize, and save image
    :param file_name: image file
    :return:
    """

    width = height = 128
    destination_file = os.path.join(images_dir, file_name)
    saved_file = os.path.join(destination_dir, file_name)

    im = Image.open(destination_file)
    # Rotate, resize, and save file as JPEG
    new_im = im.rotate(90).resize((width, height)).convert("RGB")
    new_im.save("{}.jpeg".format(saved_file), "JPEG")


def iterate_images():
    """
    Change images' name in destination directory
    :return:
    """

    # Make destination directory
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copy and change files' name in destination directory
    for index, image in enumerate(os.listdir(images_dir)):
        if index != 0:
            convert_images(image)


def main():
    if __name__ == "__main__":
        iterate_images()


main()
