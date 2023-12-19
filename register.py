# The function of this file is registering the Google API Key for the first time.

import tkinter as tk
import os

class Register():
    def __init__(self, file_path):
        # UI of the registry function.
        self.registry_window = tk.Tk()
        # Get the width and height of the screen.
        screen_width, screen_height = self.registry_window.maxsize()
        width, height = (int((screen_width-250)/2), int((screen_height-90)/2))
        # Set the size and the position of the window.
        self.registry_window.geometry(f"250x90+{width}+{height}")
        self.registry_window.resizable(width=False, height=False)
        self.registry_window.title("Registry Window")

        # Modules in the window.
        tk.Label(self.registry_window, text="Enter your Google API Key:").pack()
        self.Google_API_Key_Entry = tk.Entry(self.registry_window)
        self.Google_API_Key_Entry.pack()
        tk.Button(self.registry_window, text="Commit", command=lambda: self.button_commit_clicked(file_path)).pack()

        self.registry_window.mainloop()

    # Click the "commit" button.
    def button_commit_clicked(self, file_path):
        # Get the content of the entry.
        Google_API_Key = self.Google_API_Key_Entry.get()
        self.Google_API_Key_Entry.delete(0, tk.END)
        # Write the Google API Key to userdata.conf.
        with open(file_path + "/userdata.conf", "w") as f:
            f.write(Google_API_Key)
        # Check whether the userdata.conf has created successfully.
        if os.path.exists(file_path + "/userdata.conf"):
            with open(file_path + "/userdata.conf") as f:
                userdata = f.readline()
                if userdata == Google_API_Key:
                    self.Google_API_Key_Entry.insert(0, "Registry has been completed.")
                    self.registry_window.destroy()
                else:
                    self.Google_API_Key_Entry.insert(0, "Register failed, please try again.")

# Test module.
# if __name__ == "__main__":
#     file_path = os.getcwd()
#     register = Register(file_path)