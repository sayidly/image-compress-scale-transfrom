import os
import imageio

# get home path
from pathlib import Path
home = str(Path.home())
path = home + "/Desktop/tinypng/pngs"

images = []
for file_name in os.listdir(path):
    if file_name.endswith('.png'):
        file_path = os.path.join(path, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave(('%s/movie.gif' % path), images)
