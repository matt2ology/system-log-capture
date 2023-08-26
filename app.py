from tkinter import messagebox  # import messagebox for the admin prompt
import tkinter  # import tkinter (tk) for the admin prompt
import ctypes  # import ctypes for the is_admin() function (Windows)
import os  # import os for the is_admin() function (Linux and Mac)
import sys  # import sys for the command line arguments
import cli  # import cli for the command line interface
import gui  # import gui for the graphical user interface


def is_admin() -> bool:
    """Check if the user is admin/root or not.
    This function is used to check if the user has the
    permission to run the program or not.

    Returns:
        bool: True if the user is admin/root, False otherwise.
    """
    if os.name == 'nt':  # check if the OS is Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception:
            pass
    elif os.name == 'posix':  # if the OS is Linux or Mac
        return os.getuid() == 0  # check if the user is root (0) or not
    return False


def show_admin_prompt() -> None:
    """Show the admin prompt to the user.
    This function is used to show the admin prompt to the user
    if the user is not admin/root.
    """
    root: tkinter.Tk = tkinter.Tk()  # create a tkinter (tk) root window
    root.withdraw()  # hide the root window of tkinter (tk)
    messagebox.showerror(
        "Admin Privileges Required",
        "You need to run this program as admin/root."
    )
    root.destroy()
    sys.exit(1)  # exit the program with exit code 1 (error code)


def main() -> None:
    """The main function of the program.
    This function is used to run the program.
    """
    if not is_admin():  # check if the user is admin/root or not
        show_admin_prompt()  # show the admin prompt to the user

    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        cli.main()
    else:
        gui.main()


if __name__ == "__main__":
    main()
