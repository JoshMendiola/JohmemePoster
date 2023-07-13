import os
from random import random


def get_random_subfolder_path(parent_directory):
    subfolders = [folder.path for folder in os.scandir(parent_directory) if folder.is_dir()]
    if subfolders:
        return random.choice(subfolders)
    else:
        return None