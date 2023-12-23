import pytest
import os
from downloads_organizer.utils import (
    create_directory,
    move_file,
    check_file_size,
    move_folder_to_category,
)


def test_create_new_directory(tmp_path):
    dir_path = tmp_path / "new_directory"
    create_directory(str(dir_path))
    assert os.path.isdir(dir_path)


def test_create_existing_directory(tmp_path):
    dir_path = tmp_path / "existing_directory"
    os.mkdir(dir_path)
    create_directory(str(dir_path))  # Should not raise an exception
    assert os.path.isdir(dir_path)


def test_move_file_success(tmp_path):
    src_file = tmp_path / "test_file.txt"
    src_file.write_text("Test content")
    dest_folder = tmp_path / "dest"
    os.mkdir(dest_folder)
    move_file(str(src_file), str(dest_folder), False)
    assert not src_file.exists()
    assert (dest_folder / "test_file.txt").exists()


def test_move_file_dry_run(tmp_path):
    src_file = tmp_path / "test_file.txt"
    src_file.write_text("Test content")
    dest_folder = tmp_path / "dest"
    os.mkdir(dest_folder)
    move_file(str(src_file), str(dest_folder), True)
    assert src_file.exists()  # File should still exist at the source location


def test_file_larger_than_threshold(tmp_path):
    file_path = tmp_path / "large_file.txt"
    file_path.write_text("a" * 100)  # Create a file with 100 bytes
    assert check_file_size(str(file_path), 50)


def test_file_smaller_than_threshold(tmp_path):
    file_path = tmp_path / "small_file.txt"
    file_path.write_text("a" * 10)  # Create a file with 10 bytes
    assert not check_file_size(str(file_path), 50)


def test_move_folder_success(tmp_path):
    source_folder = tmp_path / "source"
    source_folder.mkdir()
    target_folder = tmp_path / "target"
    target_folder.mkdir()
    move_folder_to_category(str(source_folder), str(target_folder))
    assert not source_folder.exists()
    assert (target_folder / "source").exists()
