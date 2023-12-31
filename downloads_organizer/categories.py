"""Module for organizing files into categories based on their extensions.

This module contains a dictionary 'file_organization' that maps categories
like Archives, Documents, Images, etc., to a list of associated file extensions.
This can be used to organize files in a filesystem into corresponding folders
based on their file types.
"""
file_organization = {
    "Archives": [".zip", ".tar.gz", ".tgz"],
    "Documents": [".xlsx", ".docx", ".doc", ".xls", ".ppt", ".pptx", ".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ai", ".heic"],
    "Videos": [".mp4", ".mov", ".avi", ".wmv", ".mkv"],
    "Models": [".onnx", ".pth", ".tflite", ".pb", ".trt"],
    "Data": [".json", ".yaml", ".csv", ".xml", ".txt", ".log"],
    "Books": [".mobi", ".epub"],
    "Code": [
        ".py",
        ".ipynb",
        ".c",
        ".cpp",
        ".java",
        ".js",
        ".html",
        ".css",
        ".sql",
        ".sh",
        ".whl",
        ".hpp",
    ],
    "3D": [".step", ".stl", ".f3z", ".obj", ".3ds"],
    "Audio": [".wav", ".mp3", ".ogg", ".aac", ".flac", ".m4a"],
}
