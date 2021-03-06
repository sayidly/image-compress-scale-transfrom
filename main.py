#encoding:utf-8
#!/usr/bin/env python

from compress import compress
from tojpg import tojpg
from topng import topng
from scale import scale
from heictojpg import heictojpg

# get home path
from pathlib import Path
home = str(Path.home())
path = home + "/Desktop/tinypng"       # 图片路径
# cwd = os.getcwd()


# options
import sys

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg=="-c":
                compress(path)
            if arg=="-tjpg":
                tojpg(path)
            if arg=="-tpng":
                topng(path)
            if arg=="-heic":
                heictojpg(path)
            if arg=="-s":
                scale(path)
            if arg=="-h":
                print("-h \t help;\n-c \t compress the image;\n-t \t transform image from png to jpg;\n-s \t scale image;")
            else:
                pass
    else:
        print("-h \t help;\n-c \t compress the image;\n-t \t transform image from png to jpg;\n-s \t scale image;")

if __name__ == "__main__":
    main()
