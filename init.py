# This file will initiate the Google API Key and return the state.

import os

class Initiate:
    # Detect whether the content of userdata.conf is legal.
    def detect_content(self, path):
        """
        This function will detect the content of userdata.conf roughly.
        :param path: the absolute path of userdata.conf.
        :return: True: the content of the userdata.conf is legal. False: the content is illegal.
        """
        with open(path) as f:
            content = f.readline()
        if content == "":
            file_address = os.getcwd() # Get the relative path of this project.
            os.remove(file_address + "/userdata.conf")
            return False
        else:
            return True

    def init(self):
        # Check whether the userdata.conf file exists.
        file_address = os.getcwd() # Get the relative path of this project.
        # Create a responses.md file to save raw responses.
        with open(file_address + "/responses.md", "w") as f:
            f.writelines("----\n\n")
        if os.path.exists(file_address + "/userdata.conf"):
            # The userdata.conf file has existed.
            if self.detect_content(file_address + "/userdata.conf"):
                print("[System]: Initiation is completed.")
                return True
            else:
                print("[System]: Initiation is failed, please try again.")
                return False
        else:
            # The userdata.conf file is not existed.
            # Create the userdata.conf
            api_key = input("[System]: You should input your Google API Key for the first time:\n")
            with open(file_address + "/userdata.conf", "w") as f:
                f.write(api_key)
            if self.detect_content(file_address + "/userdata.conf"):
                print("[System]: Initiation is completed.")
                return True
            else:
                print("[System]: Initiation is failed, please try again.")
                return False