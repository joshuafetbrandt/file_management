


import shutil
import pathlib

path = pathlib.Path.cwd() / 'Archive Data'
path1 = path / '2020-03'
# path1.rmdir()
shutil.rmtree(path1, ignore_errors = True)