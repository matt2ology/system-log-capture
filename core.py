"""
This file contains the core classes and functions of the project.
"""

from glob import glob
import datetime
import os
import platform
import logging
FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT
)


class Utilities:
    def __init__(self):
        self.name = "Core"
        self.log_folder_name: str = "captured_logs"

    def get_desktop_path(self) -> str:
        """Gets the path to the Desktop directory regardless
        of the OS (Windows, Linux, Mac). On windows, the path the path to
        Desktop might be under OneDrive
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
        system: str = platform.system().lower()

        os_mapping: dict = {
            'linux': 'Linux',
            'darwin': 'MacOS',
            'windows': 'Windows',
        }  # maps the OS to the OS name that we want to display to the user

        return os_mapping.get(system, 'Unknown OS')

    def normalize_path(self, new_directory: str) -> str:
        """Set the new directory path to the normalized path
        of the new directory.
        Args:
            new_directory (str): The new directory to set.
        """
        return os.path.normpath(new_directory)

    def generate_timestamp_YYYY_MM_DD_T_MM(self) -> str:
        """Generate a timestamp in the format of YYYYMMDDTHHMM

        Example:
            Year Month Day Time Hour Minute Second (e.g 20210101T120000)
        Returns:
            str: The timestamp.
        """
        return datetime.datetime.now().strftime("%Y%m%dT%H%M")

    def generate_path_to_output_directory_folder(self) -> str:
        """
        Generate the path to the output directory folder.
        Example:
            captured_logs_20210101T120000
        """
        timestamp: str = self.generate_timestamp_YYYY_MM_DD_T_MM()
        folder_name: str = f"{self.log_folder_name}_{timestamp}"
        path: str = os.path.join(self.get_desktop_path(), folder_name)
        logging.info(f"Path to output directory folder: {path}")
        return path

    def create_output_directory_folder(self) -> None:
        """Create the output directory folder if it does not exist.
        Returns:
            str: The path to the output directory folder.
        """
        # create the output directory folder if it does not exist
        if not os.path.exists(
            self.generate_path_to_output_directory_folder()
        ):
            logging.info(
                f"Creating output directory folder: "
                f"{self.generate_path_to_output_directory_folder()}"
            )
            os.makedirs(self.generate_path_to_output_directory_folder())
        else:
            logging.info(
                f"Output directory folder already exists: "
                f"{self.generate_path_to_output_directory_folder()}"
            )
