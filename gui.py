from core import Utilities as core_utilities
from core_linux_os import CoreLinuxOs
from core_windows_os import CoreWindowsOs
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog
from tkinter import Frame
from tkinter import Label
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import Tk


class GUI:
    """
    Class that creates the GUI for the application and handles the user input.
    """

    def __init__(self, main_window: Tk) -> None:
        """Constructor of the GUI class.
        self: GUI
        main_window: Tk object (root) - root is the main window of the GUI.
        """
        self.default_directory: StringVar = StringVar(
            value=core_utilities().get_desktop_path()
        )

        main_window.title("System Log Capture")
        main_window.resizable(False, False)  # disable resizing the window
        main_window.iconphoto(False, PhotoImage(file="icon.png"))

        self.frame = Frame(
            main_window,
            bg="white",
            cursor="arrow"
        )
        self.frame.grid(row=0, column=0)

        # Where the magic happens: create the GUI elements (widgets) of the app
        self._create_app_h1_header()
        self._create_prompt_for_output_dir_label()
        self._create_output_dir_entry()
        self._create_browse_button()
        self._create_capture_button()
        self._create_reset_directory_path_button()

    def _create_app_h1_header(self) -> None:
        """Create the h1 header of the app.
        self: GUI
        """
        app_h1_header = Label(
            self.frame,
            text="System Log Capture",
            font=("helvetica", 24),
            bg="white"
        )
        app_h1_header.grid(row=0, column=0, columnspan=7, pady=10)

    def _create_prompt_for_output_dir_label(self) -> None:
        """Create the prompt for the output directory label.
        self: GUI
        """
        prompt_for_output_dir_label = Label(
            self.frame,
            text="Select the output directory:",
            font=("helvetica", 12, "bold"),
            bg="white"
        )
        prompt_for_output_dir_label.grid(row=1, column=0, pady=10)

    def _create_output_dir_entry(self) -> None:
        """Create the output directory entry.
        self: GUI
        frame: Frame object - the frame in which the entry will be created.
        """
        output_dir_entry = Entry(
            self.frame,
            bg="white",
            borderwidth=2,
            fg="black",
            font=("helvetica", 12),
            textvariable=self.default_directory,
            width=30,
        )
        output_dir_entry.grid(row=1, column=2, columnspan=2, pady=10)

    def _create_browse_button(self) -> None:
        """Create the browse button.
        self: GUI
        """
        browse_button = Button(
            self.frame,
            text="Browse",
            font=("helvetica", 12),
            bg="white",
            cursor="hand1",
            command=self._browse_button_clicked
        )
        browse_button.grid(row=1, column=5, pady=10)

    def _browse_button_clicked(self) -> None:
        """This function is called when the browse button is clicked.
        self: GUI
        """
        # open the file dialog
        output_dir: str = core_utilities().normalize_path(
            filedialog.askdirectory(
                title="Select the output directory"
            )
        )
        # if the user selected a directory, then update the output directory
        # entry with the selected directory
        if output_dir:
            self.default_directory.set(value=output_dir)

    def _create_reset_directory_path_button(self) -> None:
        """Create the reset directory path button. This button resets the
        output directory path to the default directory path.
        """
        reset_directory_path_button = Button(
            self.frame,
            text="Reset Path",
            font=("helvetica", 12),
            bg="pink",
            fg="black",
            activebackground="red",
            activeforeground="white",
            cursor="hand1",
            command=self._reset_directory_path_button_clicked
        )
        reset_directory_path_button.grid(row=1, column=6, pady=10, padx=10)

    def _reset_directory_path_button_clicked(self) -> None:
        """This function is called when the reset directory
        path button is clicked.
        self: GUI
        """
        self.default_directory.set(value=core_utilities().get_desktop_path())

    def _create_capture_button(self) -> None:
        """Create the capture button and is centered in the frame.
        self: GUI
        """
        capture_button = Button(
            self.frame,
            text="Capture",
            font=("helvetica", 16),
            bg="light green",
            width=20,
            activebackground="green",
            activeforeground="white",
            cursor="hand2",
            # TODO: command=self._capture_button_clicked
        )
        capture_button.grid(row=2, column=0, columnspan=7, pady=10)

    def _capture_button_clicked(self) -> None:
        """This function is called when the capture button is clicked.
        Given the operating system, the function will call the appropriate
        self: GUI
        """
        if core_utilities().get_os() == "Windows":
            CoreWindowsOs().capture_logs()
        elif core_utilities().get_os() == ("Linux" or "MacOS"):
            CoreLinuxOs().capture_logs()

def main() -> None:
    """The main function of the program.
    This function is used to run the program.
    """
    main_window = Tk()
    GUI(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
