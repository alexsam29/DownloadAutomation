import logging
import time
from os import scandir, rename, makedirs
from os.path import join, exists, splitext
from shutil import move

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Directories. Replace with your preferred directories.
source_dir = "C:/Users/alex_/Downloads"
dest_dir_audio = "C:/Users/alex_/Downloads/Audio"
dest_dir_video = "C:/Users/alex_/Downloads/Video"
dest_dir_image = "C:/Users/alex_/Downloads/Images"
dest_dir_documents = "C:/Users/alex_/Downloads/Documents"

# Image, video, audio, and document extensions
image_exts = [
    ".jpg",
    ".jpeg",
    ".jpe",
    ".jif",
    ".jfif",
    ".jfi",
    ".png",
    ".gif",
    ".webp",
    ".tiff",
    ".tif",
    ".psd",
    ".raw",
    ".arw",
    ".cr2",
    ".nrw",
    ".k25",
    ".bmp",
    ".dib",
    ".heif",
    ".heic",
    ".ind",
    ".indd",
    ".indt",
    ".jp2",
    ".j2k",
    ".jpf",
    ".jpf",
    ".jpx",
    ".jpm",
    ".mj2",
    ".svg",
    ".svgz",
    ".ai",
    ".eps",
    ".ico",
]
video_exts = [
    ".webm",
    ".mpg",
    ".mp2",
    ".mpeg",
    ".mpe",
    ".mpv",
    ".ogg",
    ".mp4",
    ".mp4v",
    ".m4v",
    ".avi",
    ".wmv",
    ".mov",
    ".qt",
    ".flv",
    ".swf",
    ".avchd",
]
audio_exts = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
document_exts = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


class MoveHandler(FileSystemEventHandler):
    """A class that handles file movements based on their extensions."""

    def on_modified(self, event):
        """Event handler for file modification event.

        Args:
            event (FileSystemEvent): The event object.
        """
        with scandir(source_dir) as files:
            for file in files:
                name = file.name
                self.search_audio_files(file, name)
                self.search_video_files(file, name)
                self.search_image_files(file, name)
                self.search_document_files(file, name)

    def search_audio_files(self, file, name):
        """Searches for audio files and moves them to the destination directory.

        Args:
            file (DirEntry): The file object.
            name (str): The name of the file.
        """
        for audio_ext in audio_exts:
            if name.endswith(audio_ext) or name.endswith(audio_ext.upper()):
                move_file(dest_dir_audio, file, name)
                logging.info(
                    f"Audio file, {name} moved into folder path: {dest_dir_audio}"
                )

    def search_video_files(self, file, name):
        """Searches for video files and moves them to the destination directory.

        Args:
            file (DirEntry): The file object.
            name (str): The name of the file.
        """
        for video_ext in video_exts:
            if name.endswith(video_ext) or name.endswith(video_ext.upper()):
                move_file(dest_dir_video, file, name)
                logging.info(
                    f"Video file, {name} moved into folder path: {dest_dir_video}"
                )

    def search_image_files(self, file, name):
        """Searches for image files and moves them to the destination directory.

        Args:
            file (DirEntry): The file object.
            name (str): The name of the file.
        """
        for image_ext in image_exts:
            if name.endswith(image_ext) or name.endswith(image_ext.upper()):
                move_file(dest_dir_image, file, name)
                logging.info(
                    f"Image file, {name} moved into folder path: {dest_dir_image}"
                )

    def search_document_files(self, file, name):
        """Searches for document files and moves them to the destination directory.

        Args:
            file (DirEntry): The file object.
            name (str): The name of the file.
        """
        for document_ext in document_exts:
            if name.endswith(document_ext) or name.endswith(document_ext.upper()):
                move_file(dest_dir_documents, file, name)
                logging.info(
                    f"Document file, {name} moved into folder path: {dest_dir_documents}"
                )


def move_file(dest, file, name):
    """Moves a file to the specified destination directory.

    If a file with the same name already exists in the destination directory, a unique name is generated.

    Args:
        dest (str): The destination directory.
        file (DirEntry): The file object.
        name (str): The name of the file.
    """
    if not exists(dest):
        makedirs(dest)

    if exists(f"{dest}/{name}"):
        unique_name = create_unique(dest, name)
        prevName = join(dest, name)
        newName = join(dest, unique_name)
        rename(prevName, newName)
    move(file, dest)


def create_unique(dest, name):
    """Creates a unique name for a file by appending a number to the filename.

    Args:
        dest (str): The destination directory.
        name (str): The name of the file.

    Returns:
        str: The unique name for the file.
    """
    filename, ext = splitext(name)
    file_number = 1

    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(file_number)}){ext}"
        file_number += 1

    return name


# Monitors the source directory recursively for file movements
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    path = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
