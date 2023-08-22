from core import Utilities as core_utilities
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

        frame = Frame(
            main_window,
            width=350,
            height=300,
            bg="white",
            cursor="arrow"
        )
        frame.pack()

        # Where the magic happens - create the GUI elements (widgets) of the app
        self._create_app_h1_header(frame)
        self._create_prompt_for_output_dir_label(frame)
        self._create_output_dir_entry(frame)
        self._create_browse_button(frame)

    def _create_app_h1_header(self, frame: Frame) -> None:
        """Create the h1 header of the app.
        self: GUI
        frame: Frame object - the frame in which the h1 header will be created.
        """
        app_h1_header = Label(
            frame,
            text="System Log Capture",
            font=("Arial", 20),
            bg="white"
        )
        app_h1_header.pack(pady=10)

    def _create_prompt_for_output_dir_label(self, frame: Frame) -> None:
        """Create the prompt for the output directory label.
        self: GUI
        frame: Frame object - the frame in which the label will be created.
        """
        prompt_for_output_dir_label = Label(
            frame,
            text="Select the output directory:",
            font=("Arial", 12),
            bg="white"
        )
        prompt_for_output_dir_label.pack(pady=10, side="left")

    def _create_output_dir_entry(self, frame: Frame) -> None:
        """Create the output directory entry.
        self: GUI
        frame: Frame object - the frame in which the entry will be created.
        """
        output_dir_entry = Entry(
            frame,
            bg="white",
            borderwidth=2,
            fg="black",
            font=("Arial", 12),
            textvariable=self.default_directory,
            width=30,
        )
        output_dir_entry.pack(pady=10, side="left")

    def _create_browse_button(self, frame: Frame) -> None:
        """Create the browse button.
        self: GUI
        frame: Frame object - the frame in which the button will be created.
        """
        browse_button = Button(
            frame,
            text="Browse",
            font=("Arial", 12),
            bg="white",
            command=self._browse_button_clicked
        )
        browse_button.pack(pady=10, side="left")

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


def main() -> None:
    """The main function of the program.
    This function is used to run the program.
    """
    main_window = Tk()
    GUI(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
