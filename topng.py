from PIL import Image
import os, sys

def topng(path):
    for dirpath, dirs, files in os.walk(path):
        #ignore finished files
        if "finished" in dirs:
            dirs.remove("finished")
        for file in files:
            try:
                imgpath = os.path.join(dirpath, file)
                im = Image.open(imgpath)
                alpha = im.split()[-1]
                if not im.mode == 'RGB':
                    print("convert to png…" + imgpath)
                    rgb_im = im.convert('RGB')
                    rgb_im.putalpha(alpha)
                    rgb_im.save(imgpath, "png")
                    # Rename the file from PNG to JPG
                    thisFile = imgpath
                    base = os.path.splitext(thisFile)[0]
                    os.rename(thisFile, base + ".png")
            except:
                pass
    print("\n所有图片修改为PNG\n")
