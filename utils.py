import json
import os
import random
import glob
import time
import shutil


# creates a combined folder of 3 memes to be together in a "post"
def create_post(memes_directory):

    # grabs the subfolders within the memes folder
    memes_in_folder = [folder.path for folder in os.scandir(memes_directory) if folder.is_dir()]
    if not memes_in_folder:
        return None

    # creates the folder
    current_timestamp = time.time()
    new_post_directory_path = f'/Users/joshuamendiola/Documents/Johmemes/Posts/{current_timestamp}'
    os.makedirs(new_post_directory_path, exist_ok=True)

    # moves three memes in the post folder
    for i in range(3):
        if not memes_in_folder:
            break
        selected_meme = random.choice(memes_in_folder)
        memes_in_folder.remove(selected_meme)
        files = glob.glob(os.path.join(selected_meme, '*'))  # Get all files in the selected folder
        for f in files:
            shutil.move(f, new_post_directory_path)
        shutil.rmtree(selected_meme)

    return new_post_directory_path


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

