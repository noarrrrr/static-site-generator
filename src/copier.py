import os
import shutil

def copier(start, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    return looper(start, destination)

def looper(start, destination):
    for i in os.listdir(start):
        if os.path.isfile(f"{start}/{i}"):
            shutil.copy(f"{start}/{i}", destination)
        else:
            os.mkdir(f"{destination}/{i}")
            looper(f"{start}/{i}", f"{destination}/{i}")