import os
import pytest
from unittest.mock import patch
from downloads_organizer.delete_move import (
    delete_folder,
    get_all_folders,
    get_organized_folders,
    prompt_delete_folder,
    display_folder_contents,
)


def test_get_organized_folders():
    categories = {"Music": "mp3", "Documents": "docx"}
    expected_folders = {"Music", "Documents"}
    assert get_organized_folders(categories) == expected_folders


def test_get_all_folders(tmp_path):
    folders = {"folder1", "folder2", "folder3"}
    for folder in folders:
        os.mkdir(tmp_path / folder)

    assert get_all_folders(str(tmp_path)) == folders


def test_delete_folder_success(tmp_path):
    folder_path = tmp_path / "test_folder"
    os.mkdir(folder_path)
    delete_folder(str(folder_path))
    assert not os.path.exists(folder_path)


def test_prompt_delete_folder_yes():
    with patch("builtins.input", return_value="y"):
        assert prompt_delete_folder("test_folder")


def test_prompt_delete_folder_no():
    with patch("builtins.input", return_value="n"):
        assert not prompt_delete_folder("test_folder")


def test_prompt_delete_folder_default_no():
    with patch("builtins.input", return_value=""):
        assert not prompt_delete_folder("test_folder")


def test_display_folder_contents(tmp_path, capfd):
    folder = "test_folder"
    folder_path = tmp_path / folder
    folder_path.mkdir()
    (folder_path / "file1.txt").write_text("content")

    display_folder_contents(folder, str(folder_path))

    captured = capfd.readouterr()
    assert "Contents of 'test_folder':" in captured.out
    assert " - file1.txt" in captured.out
