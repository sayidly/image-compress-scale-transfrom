import pyheif
import os, sys
from PIL import Image
import whatimage

def heictojpg(path):
    for dirpath, dirs, files in os.walk(path):
        #ignore finished files
        if "finished" in dirs:
            dirs.remove("finished")
        for file in files:
            try:
                if file.endswith('.HEIC') or file.endswith(".heic"):
                    imgpath = os.path.join(dirpath, file)
                    print(imgpath)
                    i = pyheif.read_heif(imgpath)
                    # Extract metadata etc
                    for metadata in i.metadata or []:
                        if metadata['type']=='Exif':
                            print("It's HEIC file")
                            # do whatever

                    # Convert to other file format like jpeg
                    pi = Image.frombytes(
                           mode=i.mode, size=i.size, data=i.data)
                    pi.save(imgpath, "jpeg")
                    # Rename the file
                    thisFile=imgpath
                    base = os.path.splitext(thisFile)[0]
                    os.rename(thisFile, base + ".jpg")
            except:
                pass
    print("\n所有HEIC图片修改为JPG\n")
