import os

import fire

from .categories import file_organization
from .delete_move import prompt_for_deletion
from .utils import check_file_size, create_directory, move_file


def organize_file(
    file: str,
    downloads_path: str,
    folder_path: str,
    large_files: list,
    size_threshold: int,
    dry_run: bool,
) -> None:
    """Organize a single file based on its type and size."""
    full_file_path = os.path.join(downloads_path, file)
    if os.path.isfile(full_file_path) and check_file_size(
        full_file_path, size_threshold
    ):
        large_files.append((file, os.path.getsize(full_file_path)))
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
    dry_run (bool): If True, the script will simulate the organization without moving files.
    """
    downloads_path = os.path.expanduser(downloads_path)
    # Convert all extensions in the dictionary to lowercase
    for category in file_organization:
        file_organization[category] = [
            ext.lower() for ext in file_organization[category]
        ]

    # Size threshold in bytes (10MB)
    size_threshold = 10 * 1024 * 1024

    large_files = []

    for folder, extensions in file_organization.items():
        folder_path = os.path.join(downloads_path, folder)
        create_directory(folder_path)
        for file in os.listdir(downloads_path):
            if any(file.lower().endswith(ext) for ext in extensions):
                organize_file(
                    file,
                    downloads_path,
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
        prompt_for_deletion(downloads_path)


def main():
    fire.Fire(organize_downloads)
