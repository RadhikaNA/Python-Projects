import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)
        return command

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None

def run_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if command:
            if "hello" in command:
                speak("Hello! How can I help you today?")

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")

            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")

            elif "good night" in command:
                speak("Good night! Sleep well.")
                break

            elif "search" in command:
                speak("What would you like me to search for?")
                search_query = listen()
                if search_query:
                    url = f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)
                    speak(f"Here are the search results for {search_query}")

            elif "exit" in command or "stop" in command:
                speak("bye")
                break

            else:
                speak("I'm sorry. I didn't understand that command.")

if __name__ == "__main__":
    run_assistant()
