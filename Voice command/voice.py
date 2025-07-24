import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser
# import requests
import pyjokes


sp=pyttsx3.init()
sp.setProperty('rate', 150)  # Set speech rate
sp.setProperty('volume', 1)  # Set volume level (0.0 to

def speak(text):
    sp.say(text)
    sp.runAndWait()
    sp.stop()

def show_supported_commands():
    print("\n🗒️  Voice Assistant - Supported Commands:\n")
    commands_list = [
        "• open youtube",
        "• open google",
        "• open notepad",
        "• open calculator",
        "• open vscode",
        "• open chrome",
        "• open command prompt",
        "• open paint",
        "• open control panel",
        "• open camera",
        "• open downloads folder",
        "• time",
        "• date",
        "• joke",
        "• search" ,
        "• exit / stop",
        "• shutdown",
        "• restart ",
        "• make a note / take a note",
        "• open facebook",
        "• open instagram",
        "• news",
       
    ]
    for item in commands_list:
        print(item)
    print("\n🎙️  Speak a command after the assistant says 'How can I help you today?'\n")

def listen():
    sh=sr.Recognizer()
    with sr.Microphone() as source:  # ✅ correct usage

        print("Listening....")
        sh.pause_threshold = 1  # Set volume level (0.0 to 1.0)
        audio = sh.listen(source)
        try:
            print("Recognizing....")
            query = sh.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I did not understand that.")
            return ""
    return query.lower()



def commands(command):
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'open calculator' in command:
        speak("Opening Calculator")
        os.system("calc")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")    
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif 'open vscode' in command:
        speak("Opening Visual Studio Code")
        os.system("code")
    elif 'open chrome' in command:
        speak("Opening Google Chrome")
        os.system("chrome")
    elif 'open command prompt' in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif 'open paint' in command:
        speak("Opening Paint")
        os.system("mspaint")

    elif 'open control panel' in command:
        speak("Opening Control Panel")
        os.system("control")

    elif 'open camera' in command:
        speak("Opening Camera")
        os.system("start microsoft.windows.camera:")

    elif 'open downloads folder' in command:
        speak("Opening Downloads Folder")
        os.startfile(os.path.join(os.path.expanduser('~'), 'Downloads'))
    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")

    elif 'restart ' in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 1")

    elif 'news' in command:
        speak("Opening latest news")
        webbrowser.open("https://news.google.com")

    elif 'open facebook' in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif 'make a note' in command or 'take a note' in command:
        speak("What should I write?")
        note = listen()
        with open("notes.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note saved.")



    elif 'what is' in command or 'who is' in command:
        import wikipedia
        speak("Searching Wikipedia...")
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find anything on that.")



    elif 'search' in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Have a great day!")
        exit()
    
    else:
        speak("Sorry, I can't handle that command yet.")



def run_assistant():
    print("Voice Assistant is running...")
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        show_supported_commands()
        if command:
            commands(command)

# 8. 🟢 Entry point
if __name__ == "__main__":
    run_assistant()