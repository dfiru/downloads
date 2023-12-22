"""
Setup script for the 'downloads_organizer' package.

This script is used to install and distribute the 'downloads_organizer' package,
which provides tools for organizing files in the downloads folder.
"""

from setuptools import setup, find_packages

setup(
    name="downloads_organizer",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fire",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "downloads-organizer=downloads_organizer.organizer:main",
        ]
    },
    # Optional metadata
    author="Daniel Firu",
    description="A tool to organize files in the downloads folder",
    url="https://github.com/dfiru/downloads_organizer",
)
