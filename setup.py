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
    entry_points="""
        [console_scripts]
        downloads-organizer=downloads_organizer.organizer:main
    """,
)
