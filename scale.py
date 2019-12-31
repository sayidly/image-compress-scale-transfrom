from PIL import Image
import os, sys

#path = "/Users/sayidhe/Desktop/tinypng/scale"

def to_pixel(val, path):
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            try:
                imgpath = os.path.join(dirpath, file)
                im = Image.open(imgpath)
                basewidth = val
                print("原始图片尺寸%spx" %im.size[0])
                wpercent = (basewidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                im = im.resize((basewidth,hsize), Image.ANTIALIAS)
                im.save(imgpath)
                print("缩放至%dpx" %basewidth)
            except:
                pass

def to_percent(val, path):
    for dirpath, dirs, files in os.walk(path):
        for file in files:
            try:
                imgpath = os.path.join(dirpath, file)
                im = Image.open(imgpath)
                wpercent = val
                print("原始图片尺寸%spx" %im.size[0])
                wsize = int((float(im.size[0])*wpercent))
                hsize = int((float(im.size[1])*wpercent))
                im = im.resize((wsize,hsize), Image.ANTIALIAS)
                im.save(imgpath)
                print("缩放至%s倍%spx" %(val, wsize))
            except:
                pass


def scale(path):
    try:
        rawwidth = input("Enter the size you want to resize(Percent with @x): \n")
        val = int(rawwidth)
        print("Scale to pixel %dpx" %val)
        to_pixel(val, path)
    except ValueError:
        try:
            if rawwidth[0] == "@":
                try:
                    val = float(rawwidth[1:])
                    print("Scale to percent %s" %val)
                    to_percent(val, path)
                except ValueError:
                    print("No.. input is not a wrong format. ")
            else:
                print("No.. input is not a wrong format. ")
        except ValueError:
            print("No.. input is not a wrong format. ")
    print("\n完成缩放")
