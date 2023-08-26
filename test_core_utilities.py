import getpass
from core import Utilities
from unittest.mock import Mock
import os
import platform
import pytest


class TestCoreUtilities:

    # This fixture will be used by all tests in this class
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Setup the test class.
        """
        self.core: Utilities = Utilities()
        # getpass approach doesn't rely on the presence of a terminal session
        self.username: str = getpass.getuser()
        self.desktop_path: str = os.path.normpath(
            os.path.join("C:\\Users", self.username, "Desktop")
        )

    @pytest.mark.parametrize("num_paths", [0, 2])
    def test_get_desktop_path(
        self,
        monkeypatch: pytest.fixture,
        num_paths: int
    ) -> None:
        """Test the get_desktop_path method. This method should return the path
        to the Desktop directory regardless of the OS (Windows, Linux, Mac).
        On windows, the path the path to Desktop might be under OneDrive or it
        might not be.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function. That is, you can mock the
            return value of glob.glob() to return a list of paths to the
            Desktop directory. If the list is empty, then the method should
            return the path to the Desktop directory under OneDrive. If the
            list has more than one path, then the method should return the
            path to the Desktop directory under the user's home directory.

            num_paths (int): The number of paths to return from glob.glob(). 
            If num_paths is 0, then the method should return the path to the
            Desktop directory under OneDrive. If num_paths is greater than 1,
            then the method should return the path to the Desktop directory
            under the user's home directory.
        """
        mock_glob: Mock = Mock(return_value=[self.desktop_path] * num_paths)
        monkeypatch.setattr("core.glob", mock_glob)

        expected_path: str = (
            self.desktop_path if num_paths == 1 else os.path.join(
                os.path.expanduser("~"), "Desktop")
        )
        assert self.core.get_desktop_path() == expected_path

    def test_normalize_path(self) -> None:
        """Test the normalize_path method. This method should return the
        normalized path of the new directory.
        """
        new_directory: str = os.path.join(self.desktop_path, "test")
        normalized_path: str = self.core.normalize_path(new_directory)
        assert normalized_path == new_directory

    def test_get_os_windows(self, monkeypatch: pytest.fixture) -> None:
        """Test the get_os method. This method should return the OS that the
        program is running on.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Windows')
        os_result: str = self.core.get_os()
        assert os_result == 'Windows'

    def test_get_os_linux(self, monkeypatch: pytest.fixture) -> None:
        """Test the get_os method. This method should return the OS that the
        program is running on - Linux.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Linux')
        os_result: str = self.core.get_os()
        assert os_result == 'Linux'

    def test_get_os_mac(self, monkeypatch: pytest.fixture) -> None:
        """Test the get_os method. This method should return the OS that the
        program is running on - MacOS.

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Darwin')
        os_result: str = self.core.get_os()
        assert os_result == 'MacOS'

    def test_get_os_unknown(self, monkeypatch: pytest.fixture) -> None:
        """
        Test the get_os method. This method should return the OS that the
        program is running on - Unknown OS (not Windows, Linux, or MacOS).

        Args:
            monkeypatch (pytest.fixture): A pytest fixture that allows you to
            mock the return value of a function. That is, you can mock the
            return value of platform.system() to return 'Unknown'. This will
            cause the get_os method to return 'Unknown OS'.
        """
        monkeypatch.setattr(platform, 'system', lambda: 'Unknown')
        os_result: str = self.core.get_os()
        assert os_result == 'Unknown OS'
