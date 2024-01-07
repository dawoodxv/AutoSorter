#!/usr/bin/env python

import os
import shutil
import time
import rumps
import threading
from threading import Timer

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")


class AutoOrganizerApp(rumps.App):
    def __init__(self):
        super(AutoOrganizerApp, self).__init__("Auto Organizer")
        self.menu = ["Toggle Auto Organizer"]
        self.timer = None  # Timer instance

    @rumps.clicked("Toggle Auto Organizer")
    def toggle_auto_organizer(self, sender):
        sender.state = not sender.state  # Toggle state immediately
        if sender.state:
            rumps.alert("Auto Organizer is now ON",
                        "Organizing files in the background.")
            # Set the timer to delay the start of auto organizer
            self.timer = Timer(1, self.run_auto_organizer)
            self.timer.start()
        else:
            rumps.alert("Auto Organizer is now OFF",
                        "Files will not be automatically organized.")
            self.stop_auto_organizer()

    def get_category(self, file_type):
        # Add or modify file extensions and categories as needed
        video_extensions = ["mp4", "mkv", "avi", "mov"]
        image_extensions = ["jpg", "jpeg", "png", "gif"]
        document_extensions = ["pdf", "doc", "docx", "txt"]
        application_extensions = ["dmg", "exe", "app"]

        if file_type.lower() in video_extensions:
            return "Videos"
        elif file_type.lower() in image_extensions:
            return "Images"
        elif file_type.lower() in document_extensions:
            return "Documents"
        elif file_type.lower() in application_extensions:
            return "Applications"
        else:
            return "Other"

    def organize_files(self):
        while getattr(self, "auto_organizer_on", False):
            for filename in os.listdir(DOWNLOADS_PATH):
                if not filename.startswith("."):  # Ignore hidden files
                    src_path = os.path.join(DOWNLOADS_PATH, filename)

                    if os.path.isfile(src_path):
                        file_type = filename.split(".")[-1]
                        category = self.get_category(file_type)

                        dest_folder = os.path.join(DOWNLOADS_PATH, category)

                        if not os.path.exists(dest_folder):
                            os.makedirs(dest_folder)

                        dest_path = os.path.join(dest_folder, filename)

                        shutil.move(src_path, dest_path)
                        print(f"Moved {filename} to {dest_folder}")

            time.sleep(1)

    def run_auto_organizer(self):
        self.auto_organizer_on = True
        self.auto_organizer_thread = threading.Thread(
            target=self.organize_files)
        self.auto_organizer_thread.start()

    def stop_auto_organizer(self):
        self.auto_organizer_on = False
        if self.timer and self.timer.is_alive():
            self.timer.cancel()  # Cancel the timer
        if hasattr(self, "auto_organizer_thread") and self.auto_organizer_thread.is_alive():
            self.auto_organizer_thread.join()
            print("Auto Organizer stopped.")


if __name__ == "__main__":
    app = AutoOrganizerApp()
    app.run()
