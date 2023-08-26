from core import Utilities
# import pyautogui
import logging
FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT
)


class CoreWindowsOs:
    def __init__(self):
        self.name: str = "Windows"
        self.core_utilities: Utilities = Utilities()

    def get_name(self) -> str:
        return self.name

    def gui_capture_logs(self) -> None:
        """Capture the logs from the GUI and save them to a file.
        """
        logging.info("Capturing logs from the GUI")
        # self.core_utilities.create_output_directory()
