# encoding: utf-8

import tinify
import os

tinify.key = 'CfZhVWCHvclrzsrg8f8Tv3LWrPS3hkbq'
#path = input("请输入包含图片的文件夹：")
#path = "/Users/sayidhe/Desktop/tinypng"       # 图片路径

def compress(path):
    for dirpath, dirs, files in os.walk(path):
        #ignore finished files
        if "finished" in dirs:
            dirs.remove("finished")
        for file in files:
            try:
                imgpath = os.path.join(dirpath, file)
                print("compressing …" + imgpath)
                tinify.from_file(imgpath).to_file(imgpath)
            except:
                pass
    print("\n所有图片压缩成功\n")

