
import pytest
import os
from core import Utilities
import platform


class TestCoreUtilities:

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Setup the test class.
        """
        self.core = Utilities()
        # get username
        self.username = os.getlogin()
        self.desktop_path: str = os.path.normpath(
            os.path.join("C:\\Users", self.username, "Desktop"))

    def test_get_desktop_path_windows(self) -> None:
        """Test the get_desktop_path method. This method should return the path
        to the Desktop directory. The path to the Desktop directory is different
        on Windows and Linux.
        """
        assert self.core.get_desktop_path() == self.desktop_path

    #TODO: Add test for Linux and Mac (test_get_desktop_path_linux): get_desktop_path -> /home/<username>/Desktop

    def test_get_os_windows(self, monkeypatch):
        """Test the get_os method. This method should return the OS that the
        program is running on.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Windows')
        os_result = self.core.get_os()
        assert os_result == 'Windows'

    def test_get_os_linux(self, monkeypatch):
        """Test the get_os method. This method should return the OS that the
        program is running on - Linux.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Linux')
        os_result = self.core.get_os()
        assert os_result == 'Linux'

    def test_get_os_mac(self, monkeypatch):
        """Test the get_os method. This method should return the OS that the
        program is running on - MacOS.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Darwin')
        os_result = self.core.get_os()
        assert os_result == 'MacOS'

    def test_get_os_unknown(self, monkeypatch):
        """
        Test the get_os method. This method should return the OS that the
        program is running on - Unknown OS (not Windows, Linux, or MacOS).
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Unknown')
        os_result = self.core.get_os()
        assert os_result == 'Unknown OS'
