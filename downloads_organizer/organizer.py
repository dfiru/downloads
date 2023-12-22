"""Module for organizing files in the downloads directory.

This module provides functionality to organize files in a specified
downloads directory into categories based on file types and sizes. It uses
the `file_organization` mapping from the `categories` module to classify
files and moves them to corresponding folders. It also includes functionality
to report on large files and optionally delete unorganized folders.
"""

import os
import fire

from .categories import file_organization
from .delete_move import prompt_for_deletion
from .utils import check_file_size, create_directory, move_file


def organize_file(
    file_name: str,
    downloads_path: str,
    folder_path: str,
    large_files: list,
    size_threshold: int,
    dry_run: bool,
) -> None:
    """
    Organize a single file based on its type and size.

    Args:
        file_name (str): Name of the file to be organized.
        downloads_path (str): Path to the downloads directory.
        folder_path (str): Destination folder path for the file.
        large_files (list): List to append large files to.
        size_threshold (int): File size threshold to classify as large.
        dry_run (bool): If True, simulate organization without moving files.
    """
    full_file_path = os.path.join(downloads_path, file_name)
    if os.path.isfile(full_file_path) and check_file_size(
        full_file_path, size_threshold
    ):
        large_files.append((file_name, os.path.getsize(full_file_path)))
    if os.path.isfile(full_file_path):
        move_file(full_file_path, folder_path, dry_run)


def organize_downloads(
    downloads_path: str = "~/Downloads/",
    dry_run: bool = False,
    delete_folders: bool = True,
) -> None:
    """
    Organize files in the downloads folder into categories.

    Args:
        downloads_path (str): Path to the downloads folder.
        dry_run (bool): If True, simulate organization without moving files.
        delete_folders (bool): If True, prompt for deletion of unorganized folders.
    """
    expanded_downloads_path = os.path.expanduser(downloads_path)
    # Convert all extensions in the dictionary to lowercase
    for category in file_organization:
        file_organization[category] = [
            ext.lower() for ext in file_organization[category]
        ]

    # Size threshold in bytes (10MB)
    size_threshold = 10 * 1024 * 1024

    large_files = []

    for folder, extensions in file_organization.items():
        folder_path = os.path.join(expanded_downloads_path, folder)
        create_directory(folder_path)
        for file in os.listdir(expanded_downloads_path):
            if any(file.lower().endswith(ext) for ext in extensions):
                organize_file(
                    file,
                    expanded_downloads_path,
                    folder_path,
                    large_files,
                    size_threshold,
                    dry_run,
                )

    large_files.sort(key=lambda x: x[1], reverse=True)

    print("Large Files Report (Files over 10MB):")
    for file, size in large_files:
        print(f"{file}: {size / (1024 * 1024):.2f} MB")

    if dry_run:
        print("Dry run complete. No files were moved.")
    else:
        print("File organization complete.")

    if delete_folders:
        prompt_for_deletion(expanded_downloads_path)


def main():
    """
    Main function to be called when the script is executed.

    Uses Google's Python Fire library to provide a command-line interface.
    """
    fire.Fire(organize_downloads)
