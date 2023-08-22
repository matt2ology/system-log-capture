"""
This file contains the core classes and functions of the project.
"""

from glob import glob
import os
import platform


class Utilities:
    def __init__(self):
        self.name = "Core"

    def get_desktop_path(self) -> str:
        """Gets the path to the Desktop directory regardless
        of the OS (Windows, Linux, Mac). On windows, the path the path to Desktop
        might be under OneDrive
        Returns:
            str: The path to the Desktop directory.
        """
        # list of paths to the Desktop directory (Windows, Linux, Mac)
        list_of_desktop_paths: list = glob(
            os.path.expanduser("~//*Desktop//"),
            recursive=True
        )
        return os.path.normpath(
            list_of_desktop_paths[0] if len(list_of_desktop_paths) == 1
            else os.path.join(os.path.expanduser("~"), "Desktop")
        )

    def get_os(self) -> str:
        """
        Gets the OS that the program is running on.

        Returns:
            str: The OS that the program is running on. If the OS is not
                recognized, then return "Unknown OS".
        """
        system = platform.system().lower()  # get the OS that the program is running on

        os_mapping: dict = {
            'linux': 'Linux',
            'darwin': 'MacOS',
            'windows': 'Windows',
        }  # maps the OS to the OS name that we want to display to the user

        return os_mapping.get(system, 'Unknown OS')

    def normalize_path(self, new_directory: str) -> str:
        """Set the new directory path to the normalized path of the new directory.
        Args:
            new_directory (str): The new directory to set.
        """
        return os.path.normpath(new_directory)


class WindowsOs:
    def __init__(self):
        self.name = "Windows"

    def get_name(self):
        return self.name


class LinuxOs:
    def __init__(self):
        self.name = "Linux"

    def get_name(self):
        return self.name
