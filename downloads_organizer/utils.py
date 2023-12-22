import os
import shutil


def create_directory(path: str) -> None:
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def move_file(file_path: str, folder: str, dry_run: bool) -> None:
    """Move a file to a specified folder."""
    if dry_run:
        print(f"Would move to {folder}: {os.path.basename(file_path)}")
    else:
        shutil.move(file_path, folder)
        print(f"Moved to {folder}: {os.path.basename(file_path)}")


def check_file_size(file_path: str, size_threshold: int) -> bool:
    """Check if a file exceeds a certain size threshold."""
    return os.path.getsize(file_path) > size_threshold


def move_folder_to_category(source_folder, target_folder):
    """Move a folder to a target directory."""
    try:
        shutil.move(source_folder, target_folder)
        print(f"Moved '{os.path.basename(source_folder)}' to '{target_folder}'.")
    except Exception as e:
        print(f"Error moving '{os.path.basename(source_folder)}': {e}")
