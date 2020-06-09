#encoding:utf-8

from PIL import Image, ImageDraw
import os, sys
import numpy

# get home path
from pathlib import Path
home = str(Path.home())
path = home + "/Desktop/tinypng/pngs"

images = []

for dirpath, dirs, files in os.walk(path):
    files.sort()
    for file in files:
        try:
            newname = file
            newname = newname.split(".")
            if newname[-1]=="png":
                newname = str.join(".",newname)
                imgpath = os.path.join(dirpath, newname)
                print(imgpath)
                im = Image.open(imgpath)
                draw = ImageDraw.Draw(im)
                images.append(im)
        except:
            pass
print("\n制作 gif 成功\n")

#print(list(images))

images[0].save(('%s/imagedraw.gif' % path),
               save_all=True, append_images=images[1:], optimize=False, duration=0, loop=0)
