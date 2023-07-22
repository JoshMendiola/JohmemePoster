import configparser
import shutil
from instagrapi import Client
import utils


def login_instagram():
    config = configparser.ConfigParser()
    config.read('config.ini')
    cli = Client()
    cli.login(config['instagram']['username'], config['instagram']['password'])
    return cli


def post_to_instagram(post_folder_path):
    sorted_memes = utils.get_sorted_memes(post_folder_path)
    print(sorted_memes)
    if len(sorted_memes) == 1:
        instagram_client.photo_upload(sorted_memes[0], utils.get_random_caption())
    else :
        instagram_client.album_upload(sorted_memes, utils.get_random_caption())


if __name__ == '__main__':
    instagram_client = login_instagram()
    post = utils.create_post("/Users/joshuamendiola/Documents/Johmemes/Memes/")
    if post is not None:
        post_to_instagram(post)
    # shutil.rmtree(post)


