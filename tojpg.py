from PIL import Image
import os, sys

def tojpg(path):
    for dirpath, dirs, files in os.walk(path):
        #ignore finished files
        if "finished" in dirs:
            dirs.remove("finished")
        for file in files:
            try:
                imgpath = os.path.join(dirpath, file)
                im = Image.open(imgpath)
                if not im.mode == 'RGB':
                    print("Convert to jpg …" + imgpath)
                    rgb_im = im.convert('RGB')
                    rgb_im.save(imgpath, "jpeg")
                    # Rename the file from PNG to JPG
                    thisFile = imgpath
                    base = os.path.splitext(thisFile)[0]
                    os.rename(thisFile, base + ".jpg")
            except:
                pass
    print("\n所有图片修改为JPG\n")
