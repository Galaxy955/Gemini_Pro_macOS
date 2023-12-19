# The core of the application.

import os
from register import Register
from main_window import Main_Window

class Main():
    def __init__(self):
        file_path = os.getcwd()
        # Check whether the userdata.conf exists.
        self.check(file_path)
        # Call the main window.
        Main_Window()

    def check(self, file_path):
        """
        This function will check the userdata.conf.
        :param file_path: The project path.
        :return: True: userdata.conf has existed. False: userdata.conf doesn't exist.
        """
        # Check whether the userdata.conf exists.
        if os.path.exists(file_path + "/userdata.conf"):
            # If responses.md has existed, delete it.
            if os.path.exists(file_path + "/responses.md"):
                os.system("rm -rf " + file_path + "/responses.md")
            if os.path.exists(file_path + "/responses.html"):
                os.system("rm -rf " + file_path + "/responses.html")
        else:
            # userdata.conf doesn't exist. Call the register function.
            Register(file_path)


# Test module
if __name__ == "__main__":
    Main()