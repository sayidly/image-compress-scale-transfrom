# Using Python to compress, scale and transform image

```
-h 	 help;
-c 	 compress the image;
-t 	 transform image from png to jpg;
-s 	 scale image;
```

## Setup

```
pip install -r requirements.txt
```

## Usage

use `-s` `-c` `-t` argument as you wish

```
python main.py -s -c -t
```

## 附录(pipenv)：python – 在Virtualenvs中的破坏引用

错误如下：

```
dyld: Library not loaded: @executable_path/../.Python
  Referenced from: /Users/[user]/.virtualenvs/modclass/bin/python
  Reason: image not found
Trace/BPT trap: 5
```

当您使用Homebrew升级Python，然后运行brew cleanup时，virtualenv中的符号链接指向不再存在的路径(因为Homebrew会删除它们)。

解决方案是删除virtualenv中的符号链接，然后重新创建它们：

```
find ~/.virtualenvs/my-virtual-env/ -type l -delete
virtualenv ~/.virtualenvs/my-virtual-env
```

like

```
workon tinypng
cdvirtualenv
find . -type l -delete
virtualenv .
```
