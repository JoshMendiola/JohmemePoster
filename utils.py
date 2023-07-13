import os
import random
import glob

captions = [
    "MEOW !!!",
    "Cant stop wont stop",
    "I saw a cat today, it was nice :)",
    "God i love having a meme page"
]

def get_random_subfolder_path(parent_directory):
    subfolders = [folder.path for folder in os.scandir(parent_directory) if folder.is_dir()]
    if subfolders:
        return random.choice(subfolders)
    else:
        return None


def get_sorted_memes(directory):
    return sorted(glob.glob(os.path.join(directory, '*')))


def get_random_caption():
    return random.choice(captions)

