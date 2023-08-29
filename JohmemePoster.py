import configparser
import shutil
import sys
import os
from instagrapi import Client
import utils


def login_instagram():
    # Determine if the script is running as a bundled executable or normally
    if getattr(sys, 'frozen', False):
        current_path = sys._MEIPASS  # running as a bundled executable
    else:
        current_path = os.path.dirname(__file__)  # running normally

    config_file_path = os.path.join(current_path, 'config.ini')

    # Add error-handling to debug more easily
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


def post_to_instagram(instagram_client, post_folder_path):
    sorted_memes = utils.get_sorted_memes(post_folder_path)
    print(sorted_memes)
    if len(sorted_memes) == 1:
        instagram_client.photo_upload(sorted_memes[0], utils.get_random_caption("/Users/joshuamendiola"
                                                                                "/PycharmProjects/JohmemePoster/captions.json"))
    else:
        instagram_client.album_upload(sorted_memes, utils.get_random_caption("/Users/joshuamendiola/PycharmProjects"
                                                                             "/JohmemePoster/captions.json"))


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
