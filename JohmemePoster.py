import configparser
import shutil
import sys
import os
from instagrapi import Client
import utils


# logins to instagram using the credentials in the config file
def login_instagram():
    # checks where the config file is stored in case of running as application
    if getattr(sys, 'frozen', False):
        current_path = sys._MEIPASS
    else:
        current_path = os.path.dirname(__file__)  # running normally

    config_file_path = os.path.join(current_path, 'config.ini')

    # logs in
    try:
        config = configparser.ConfigParser()
        config.read(config_file_path)
        cli = Client()
        cli.login(config['instagram']['username'], config['instagram']['password'])
        return cli
    except KeyError:
        print(f"KeyError: Check if 'instagram' section and keys are present in {config_file_path}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


# takes the posts organized in the post folder and sends them up to the api
def post_to_instagram(instagram_client, post_folder_path):
    sorted_memes = utils.get_sorted_memes(post_folder_path)
    print(sorted_memes)
    if len(sorted_memes) == 1:
        instagram_client.photo_upload(sorted_memes[0], utils.get_random_caption("/Users/joshuamendiola"
                                                                                "/PycharmProjects/JohmemePoster/captions.json"))
    else:
        instagram_client.album_upload(sorted_memes, utils.get_random_caption("/Users/joshuamendiola/PycharmProjects"
                                                                             "/JohmemePoster/captions.json"))
    shutil.rmtree(post_folder_path)


def main():
    try:
        instagram_client = login_instagram()
        post = utils.create_post("/Users/joshuamendiola/Documents/Johmemes/Memes/")
        if post is not None:
            post_to_instagram(instagram_client, post)
        shutil.rmtree(post)
    except Exception as e:
        print(f"An error occurred in main: {e}")
        raise


def lambda_handler(event, context):
    main()


if __name__ == '__main__':
    main()
