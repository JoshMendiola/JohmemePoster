import configparser
from random import random

from instagrapi import Client
import utils


def login_instagram():
    config = configparser.ConfigParser()
    config.read('config.ini')
    cli = Client()
    cli.login(config['instagram']['username'], config['instagram']['password'])
    return cli


def post_meme_to_instagram():
    random_meme_folder_path = utils.get_random_subfolder_path('/Users/joshuamendiola/Documents/Johmemes/')
    sorted_memes = utils.get_sorted_memes(random_meme_folder_path)
    print(sorted_memes)
    if len(sorted_memes) == 1:
        instagram_client.photo_upload(sorted_memes[0], utils.get_random_caption())
    else :
        instagram_client.album_upload(sorted_memes, utils.get_random_caption())


if __name__ == '__main__':
    instagram_client = login_instagram()
    post_meme_to_instagram()


