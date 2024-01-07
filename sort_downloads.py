#!/usr/bin/env python

import os
import shutil

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")


def get_category(file_type):
    video_extensions = ["mp4", "mkv", "avi", "mov"]
    image_extensions = ["jpg", "jpeg", "png", "gif"]
    document_extensions = ["pdf", "doc", "docx", "txt"]
    application_extensions = ["dmg", "exe", "app"]

    if file_type in video_extensions:
        return "Videos"
    elif file_type in image_extensions:
        return "Images"
    elif file_type in document_extensions:
        return "Documents"
    elif file_type in application_extensions:
        return "Applications"
    else:
        return "Other"


def sort_files():
    for filename in os.listdir(DOWNLOADS_PATH):
        src_path = os.path.join(DOWNLOADS_PATH, filename)

        if os.path.isfile(src_path):
            file_type = filename.split(".")[-1].lower()
            category = get_category(file_type)

            dest_folder = os.path.join(DOWNLOADS_PATH, category)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            dest_path = os.path.join(dest_folder, filename)

            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")


if __name__ == "__main__":
    sort_files()