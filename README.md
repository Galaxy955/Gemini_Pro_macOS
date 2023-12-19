# Gemini Pro for macOS

This is a simple Python application powered by Google Gemini Pro API. You can have a conversation with Google Gemini Pro on your Mac through this app.

<img src="./res/Gemini_logo.jpg" style="zoom: 40%;" >

## Some prepares before using

### Google API Key

You should have your own Google API Key before using. The app will ask your Google API Key for the first time. **Your Google API Key will only be saved on your own device.**

<img src="/Users/lyx/Downloads/Gemini_Pro_macOS/res/register_google_api_key.png" alt="image-20231219213400456" style="zoom:50%;" />

#### How to get your own Google API Key?

1. Open the website provided by Google: [ai.google.dev]("https://ai.google.dev/")
2. Clike the "Get API Key in Google AI Studio".
   <img src="./res/get_api_key_button.png" style="zoom: 33%;" >

3. Get and copy your own Google API Key.
   <img src="./res/get_api_key.jpg">

### Necessary packages

- tkinter
- mistune
- google-generativeai

You can install these necessary packages by using **"pip install <package_names>"** or **"pip install -r requirements.txt"**.

## Quick Start

### Start the application by Python

```zsh
cd <Project_Path>
python main.py
```

### Demo

<img src="./res/Gemini_Pro_Demo.gif">
