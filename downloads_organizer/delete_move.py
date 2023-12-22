"""Module for managing and organizing files in a directory.

This module provides functionality to prompt for deletion or reorganization
of unorganized folders within a given directory path. It utilizes a predefined
category mapping from the `file_organization` module to classify folders.
"""

import os
import shutil
from .categories import file_organization as category_map


def prompt_for_deletion(downloads_path: str):
    """
    Prompt for deletion or reorganization of unorganized folders.

    Args:
        downloads_path (str): Path to the downloads directory.
    """
    expanded_downloads_path = os.path.expanduser(downloads_path)
    organized_folders = get_organized_folders(category_map)
    all_folders = get_all_folders(expanded_downloads_path)
    unorganized_folders = all_folders - organized_folders

    for folder in unorganized_folders:
        clear_screen()
        handle_unorganized_folder(folder, expanded_downloads_path, organized_folders)


def get_organized_folders(categories: dict) -> set:
    """
    Return a set of folder names that are organized.

    Args:
        categories (dict): A dictionary mapping file types to folder names.

    Returns:
        set: A set of folder names.
    """
    return set(categories.keys())


def get_all_folders(path: str) -> set:
    """
    Return a set of all folder names in the given path.

    Args:
        path (str): Directory path to list folders from.

    Returns:
        set: A set of folder names.
    """
    return {d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))}


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def handle_unorganized_folder(folder: str, downloads_path: str, organized_folders: set):
    """
    Handle the deletion or reorganization of an unorganized folder.

    Args:
        folder (str): The folder name to handle.
        downloads_path (str): Path to the downloads directory.
        organized_folders (set): Set of organized folder names.
    """
    folder_path = os.path.join(downloads_path, folder)
    display_folder_contents(folder, folder_path)
    if prompt_delete_folder(folder):
        delete_folder(folder_path)
    else:
        handle_folder_reorganization(folder_path, organized_folders)


def display_folder_contents(folder: str, folder_path: str):
    """
    Print the contents of the given folder.

    Args:
        folder (str): The folder name.
        folder_path (str): Full path of the folder.
    """
    print(f"Contents of '{folder}':")
    for item in os.listdir(folder_path):
        print(f" - {item}")


def prompt_delete_folder(folder: str) -> bool:
    """
    Prompt the user to delete the folder and return their decision.

    Args:
        folder (str): The folder name to potentially delete.

    Returns:
        bool: True if the user decides to delete, False otherwise.
    """
    response = (
        input(
            f"Found unorganized folder '{folder}'. Would you like to delete it? [y/N]: "
        )
        or "n"
    )
    return response.lower() == "y"


def delete_folder(folder_path: str):
    """
    Delete the folder at the given path.

    Args:
        folder_path (str): Full path of the folder to delete.
    """
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted '{os.path.basename(folder_path)}'.")
    except Exception as e:
        print(f"Error deleting '{os.path.basename(folder_path)}': {e}")


def handle_folder_reorganization(folder_path: str, organized_folders: set):
    """
    Prompt the user to reorganize the folder into a category.

    Args:
        folder_path (str): Full path of the folder to reorganize.
        organized_folders (set): Set of organized folder names.
    """
    folder = os.path.basename(folder_path)
    print(f"Skipping '{folder}'.")
    category_mapping = {category[0].lower(): category for category in organized_folders}
    print("Select a category to move to (use the first letter) or press Enter to skip:")
    for letter, category in category_mapping.items():
        print(f"{letter.upper()}: {category}")

    category_input = input("Enter the letter of the category: ").lower()
    chosen_category = category_mapping.get(category_input)

    if chosen_category:
        target_folder = os.path.join(os.path.dirname(folder_path), chosen_category)
        move_folder_to_category(folder_path, target_folder)
    else:
        print(f"No action taken for '{folder}'.")


def move_folder_to_category(source_folder: str, target_folder: str):
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
