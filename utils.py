import json
import os
import random
import glob
import time
import shutil


def create_post(parent_directory):
    subfolders = [folder.path for folder in os.scandir(parent_directory) if folder.is_dir()]
    if not subfolders:
        return None
    current_timestamp = time.time()
    directory_path = f'/Users/joshuamendiola/Documents/Johmemes/Posts/{current_timestamp}'
    os.makedirs(directory_path, exist_ok=True)

    for i in range(3):
        if not subfolders:
            break
        selected_meme = random.choice(subfolders)
        subfolders.remove(selected_meme)
        files = glob.glob(os.path.join(selected_meme, '*'))  # Get all files in the selected folder
        for f in files:
            shutil.move(f, directory_path)

    return directory_path


def get_random_subfolder_path(parent_directory):
    subfolders = [folder.path for folder in os.scandir(parent_directory) if folder.is_dir()]
    if subfolders:
        return random.choice(subfolders)
    else:
        return None


def get_sorted_memes(directory):
    return sorted(glob.glob(os.path.join(directory, '*')))


def get_random_caption(file_path):
    with open(file_path, 'r') as f:
        captions = json.load(f)

    if len(captions) == 0:
        return None

    random_caption = random.choice(captions)
    captions.remove(random_caption)

    with open(file_path, 'w') as f:
        json.dump(captions, f)

    return random_caption

