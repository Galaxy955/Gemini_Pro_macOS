# This file is the main process.

import google.generativeai as genai
import os
import subprocess
from time import localtime
from time import sleep
from init import Initiate

if __name__ == "__main__":
    # Initiate the environment.
    initiate = Initiate()
    count = 0
    state = initiate.init()
    while not state:
        count += 1
        state = initiate.init()
        if count > 3:
            raise FileExistsError("Initiating has failed over 5 times, please check your environment.")
    sleep(1)

    # Link to the Gemini Pro
    with open("userdata.conf") as f:
        GOOGLE_API_KEY = f.readline()
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    print("[System]: Loading model has completed.")

    # Start a dialogue with Gemini Pro
    sleep(1)
    print('[System] You will start a dialogue with Google Gemini. If you want to exit, please input "bye". All responses'
          ' will be saved in the responses.md.')
    # Open responses.md by Typora.
    try:
        subprocess.Popen(["open -a /Applications/Typora.app" + " " + os.getcwd() + "/responses.md"],
                         shell=True)
    except:
        print("[System]: Typora is not available in this Mac, please install Typora app to get the best experience.\n")
        print("[System]: All the information of next dialogues between you and Gemini Pro will be saved, you also can"
              "choose other apps which support for Markdown to display the responses from Gemini Pro.")
    while (True):
        question = input("[You]: ")
        if (question == "bye" or question == "Bye"):
            print("[Gemini Pro]: See you next time. Bye~")
            break
        now_you = str(localtime().tm_year) + "." + str(localtime().tm_mon) + "." + str(localtime().tm_mday) + \
                  " " + str(localtime().tm_hour) + ":" + str(localtime().tm_min) + ":" + str(localtime().tm_sec)
        try:
            response = model.generate_content(question)
        except:
            raise RuntimeError("Your Google API Key is invalid, please pass valid one.")
        for x in response.candidates:
            if str(x.finish_reason) == "FinishReason.STOP":
                # Get the response correctly.
                now_gemini = str(localtime().tm_year) + "." + str(localtime().tm_mon) + "." + str(localtime().tm_mday) + \
                      " " + str(localtime().tm_hour) + ":" + str(localtime().tm_min) + ":" + str(localtime().tm_sec)
                with open(os.getcwd() + "/responses.md", "a") as f:
                    f.writelines(["**You  **" + now_you + "\n\n", question + "\n\n", "**Gemini Pro**  " + now_gemini + "\n\n",
                                  x.content.parts[0].text + "\n\n" + "----\n\n"])
                print("[Gemini Pro]: " + x.content.parts[0].text + "\n\n")
            else:
                print("[Gemini Pro]: Sorry, I can't answer this question, please try another.")
                now_gemini = str(localtime().tm_year) + "." + str(localtime().tm_mon) + "." + str(localtime().tm_mday) + \
                             " " + str(localtime().tm_hour) + ":" + str(localtime().tm_min) + ":" + str(
                    localtime().tm_sec)
                with open(os.getcwd() + "/responses.md", "a") as f:
                    f.writelines(["**You  **" + now_you + "\n\n", question + "\n\n", "**Gemini Pro**  " + now_gemini + "\n\n",
                                  "Sorry, I can't answer this question, please try another." + "\n\n" + "----\n\n"])