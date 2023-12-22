"""
This module contains utility functions for file and folder operations.

It includes functions for creating directories, moving files and folders,
and checking file sizes. These functions are used to help organize files
in a filesystem by moving them into categorized directories and handling
large files differently if needed.
"""

import os
import shutil


def create_directory(path: str) -> None:
    """
    Create a directory at the specified path if it does not exist.

    Args:
        path (str): The path where the directory will be created.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def move_file(file_path: str, folder: str, dry_run: bool) -> None:
    """
    Move a file to a specified folder.

    Args:
        file_path (str): The full path of the file to be moved.
        folder (str): The target folder to move the file to.
        dry_run (bool): If True, simulate the move without executing it.
    """
    if dry_run:
        print(f"Would move to {folder}: {os.path.basename(file_path)}")
    else:
        shutil.move(file_path, folder)
        print(f"Moved to {folder}: {os.path.basename(file_path)}")


def check_file_size(file_path: str, size_threshold: int) -> bool:
    """
    Check if the size of a given file exceeds a specified threshold.

    Args:
        file_path (str): The full path of the file to check.
        size_threshold (int): The size threshold in bytes.

    Returns:
        bool: True if the file size is greater than the threshold, False otherwise.
    """
    return os.path.getsize(file_path) > size_threshold


def move_folder_to_category(source_folder: str, target_folder: str) -> None:
    """
    Move a folder to a target directory.

    Args:
        source_folder (str): The source folder path to move.
        target_folder (str): The target directory path to move the folder to.
    """
    try:
        shutil.move(source_folder, target_folder)
        print(f"Moved '{os.path.basename(source_folder)}' to '{target_folder}'.")
    except Exception as e:
        print(f"Error moving '{os.path.basename(source_folder)}': {e}")
