"""
After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
"""

import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    """driver code"""
    is_valid_args(sys.argv)
    read_file = sys.argv[1]
    write_file = sys.argv[2]
    shirt = "shirt.png"
    try:
        with Image.open(shirt) as shirt_file:
            with Image.open(read_file) as muppet:
                muppet = ImageOps.fit(muppet, shirt_file.size)
                muppet.paste(shirt_file, shirt_file)
                muppet.save(write_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def is_valid_args(args):
    """Checking if cmd-line args are valid or not"""
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    read_file_ext = splitext(args[1].lower())[1]
    write_file_ext = splitext(args[2].lower())[1]
    if read_file_ext != write_file_ext:
        sys.exit("Input and output have different extensions")
    if not (read_file_ext == ".jpg") and not (
            read_file_ext == ".jpeg") and not (read_file_ext == ".png"):
        sys.exit("Invalid input")
    if not (write_file_ext == ".jpg") and not (
            write_file_ext == ".jpeg") and not (write_file_ext == ".png"):
        sys.exit("Invalid output")


if __name__ == "__main__":
    main()
