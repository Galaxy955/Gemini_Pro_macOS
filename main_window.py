# This is the main window of the application.

import tkinter as tk
import os
import mistune
import google.generativeai as genai
from tkinter import ttk
from tkinter import messagebox
from tkhtmlview import HTMLLabel
from register import Register

class Main_Window():
    def __init__(self):
        self.file_path = os.getcwd()
        # Read the Google API Key.
        with open(self.file_path + "/userdata.conf") as f:
            GOOGLE_API_KEY = f.readline()
        # Initiate the model.
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            self.model = genai.GenerativeModel("gemini-pro")
        except:
            messagebox.showerror(title="Error", message="Load the model failed, please try again.")
        self.main_window = tk.Tk()
        # Get the width and height of the screen.
        screen_width, screen_height = self.main_window.maxsize()
        width, height = (int((screen_width - 500) / 2), int((screen_height - 490) / 2))
        # Set the size and the position of the window.
        self.main_window.geometry(f"500x490+{width}+{height}")
        self.main_window.resizable(width=True, height=False)
        self.main_window.title("Gemini Pro")

        # responses label.
        self.responses_label = HTMLLabel(self.main_window)
        self.responses_label.pack(fill=tk.X)

        # Entry.
        self.entry = tk.Text(self.main_window, height=10)
        self.entry.pack(fill="x")
        self.entry.configure(takefocus=True)
        self.main_window.bind(sequence="<KeyPress-i>", func=self.KeyBoard_FocusSet)
        self.entry.focus_set()

        # "Send" button.
        buttons_frame = ttk.Frame(self.main_window)
        ttk.Button(buttons_frame, text="Register", command=self.Call_Register).grid(row=0, column=0, padx=10)
        button_send = ttk.Button(buttons_frame, text="Send", command=self.Send)
        button_send.grid(row=0, column=1)
        self.main_window.bind(sequence="<Return>", func=self.KeyBoard_Send)
        buttons_frame.pack(padx=10, anchor=tk.E)

        self.main_window.mainloop()

    def Call_Register(self):
        Register(self.file_path)

    def Send(self):
        # if not os.path.exists(self.file_path + "/busy.state"):
        # Get the question entered by user.
        question = self.entry.get(index1="1.0", index2=tk.END)
        # If the entry is empty, it will get this content: (I don't know why.)
        if question == """

""":
            question = "Hello, Gemini!"
        self.entry.delete(index1="1.0", index2=tk.END)
        # Send the question to Gemini Pro
        # Send the question to Gemini Pro and get the response.
        response = self.model.generate_content(question)
        # Parse the response.
        self.Parse_Response(question, response.text)

    def KeyBoard_Send(self, event):
        self.Send()

    def KeyBoard_FocusSet(self, event):
        self.entry.focus_set()

    def Parse_Response(self, question, response):
        # Write the response to responses.md
        with open(self.file_path + "/responses.md", "a") as f:
            f.write("<h4 style='color:#0277BD'>You: </h4>\n")
            f.write(question + "\n")
            f.write("<h4 style='color:#0277BD'>Gemini Pro: </h4>\n")
            f.write(response + "\n")
        # Convert the Markdown response to HTML response.
        with open(self.file_path + "/responses.md") as f:
            responses = f.readlines()
        with open(self.file_path + "/responses.html", "w") as f:
            for x in responses:
                f.write(mistune.html(x))
        with open(self.file_path + "/responses.html") as f:
            responses_html = f.readlines()
            # print(responses_html)
        results_html = ""
        for result_html in responses_html:
            results_html += result_html
        self.responses_label.set_html(results_html)
        self.responses_label.yview_scroll(number=2000, what="units")
        # Set the busy signal = 0.
        self.busy = 0

# Test module.
# if __name__ == "__main__":
#     Main_Window()