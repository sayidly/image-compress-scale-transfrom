#encoding:utf-8

from PIL import Image, ImageDraw
import os, sys
import imageio

# get home path
from pathlib import Path
home = str(Path.home())
path = home + "/Desktop/tinypng/pngs"

images = []

for dirpath, dirs, files in os.walk(path):
    files.sort()
    for file in files:
        try:
            if file.endswith('.png'):
                imgpath = os.path.join(dirpath, file)
                print(imgpath)
                images.append(imageio.imread(imgpath))
        except:
            pass
print("\n制作 gif 成功\n")

#print(list(images))

imageio.mimsave(('%s/movie.gif' % path), images, fps=16)

#images[0].save(('%s/imagedraw.gif' % path),
#               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
