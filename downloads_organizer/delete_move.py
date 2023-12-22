import os

from .categories import file_organization
import shutil


def prompt_for_deletion(downloads_path: str):
    downloads_path = os.path.expanduser(downloads_path)
    organized_folders = get_organized_folders(file_organization)
    all_folders = get_all_folders(downloads_path)
    unorganized_folders = all_folders - organized_folders

    for folder in unorganized_folders:
        clear_screen()
        handle_unorganized_folder(folder, downloads_path, organized_folders)


def get_organized_folders(file_organization: dict) -> set:
    """Return a set of folder names that are organized."""
    return set(file_organization.keys())


def get_all_folders(path: str) -> set:
    """Return a set of all folder names in the given path."""
    return {d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))}


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def handle_unorganized_folder(folder: str, downloads_path: str, organized_folders: set):
    """Handle the deletion or reorganization of an unorganized folder."""
    folder_path = os.path.join(downloads_path, folder)
    display_folder_contents(folder, folder_path)
    if prompt_delete_folder(folder):
        delete_folder(folder_path)
    else:
        handle_folder_reorganization(
            downloads_path, folder, folder_path, organized_folders
        )


def display_folder_contents(folder: str, folder_path: str):
    """Print the contents of the given folder."""
    print(f"Contents of '{folder}':")
    for item in os.listdir(folder_path):
        print(f" - {item}")


def prompt_delete_folder(folder: str) -> bool:
    """Prompt the user to delete the folder and return their decision."""
    response = (
        input(
            f"Found unorganized folder '{folder}'. Would you like to delete it? [y/N]: "
        )
        or "n"
    )
    return response.lower() == "y"


def delete_folder(folder_path: str):
    """Delete the folder at the given path."""
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted '{os.path.basename(folder_path)}'.")
    except Exception as e:
        print(f"Error deleting '{os.path.basename(folder_path)}': {e}")


def handle_folder_reorganization(
    downloads_path: str, folder: str, folder_path: str, organized_folders: set
):
    """Prompt the user to reorganize the folder into a category."""
    print(f"Skipping '{folder}'.")
    category_mapping = {category[0].lower(): category for category in organized_folders}
    print("Select a category to move to (use the first letter) or press Enter to skip:")
    for letter, category in category_mapping.items():
        print(f"{letter.upper()}: {category}")

    category_input = input("Enter the letter of the category: ").lower()
    chosen_category = category_mapping.get(category_input)

    if chosen_category:
        move_folder_to_category(
            folder_path, os.path.join(downloads_path, chosen_category)
        )
    else:
        print(f"No action taken for '{folder}'.")


def move_folder_to_category(source_folder, target_folder):
    """Move a folder to a target directory."""
    try:
        shutil.move(source_folder, target_folder)
        print(f"Moved '{os.path.basename(source_folder)}' to '{target_folder}'.")
    except Exception as e:
        print(f"Error moving '{os.path.basename(source_folder)}': {e}")
