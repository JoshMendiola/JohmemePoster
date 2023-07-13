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
    folder_path = utils.get_random_subfolder_path()


if __name__ == '__main__':
    instagram_client = login_instagram()


