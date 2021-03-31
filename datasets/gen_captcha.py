import argparse
import json
import string
import os
import shutil
import uuid
from captcha.image import ImageCaptcha
import itertools
from string import ascii_uppercase, ascii_lowercase, digits
from random import random, choices


def main(img_dir, width, height, n):
    print("Generating images.")
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    image = ImageCaptcha(width=width, height=height)

    total_images = 0
    for _ in range(n):
        i = my_cap = ''.join(choices(ascii_uppercase, k=4))
        captcha = ''.join(i)
        fn = os.path.join(img_dir, '%s_%s.png' % (captcha, uuid.uuid4()))
        image.write(captcha, fn)
        total_images += 1


os.system("rm -rf images")
main("./images/train/", 120, 100, 1000)
main("./images/test/", 120, 100, 1000)
