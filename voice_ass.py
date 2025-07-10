import pyttsx3
import speech_recognition as sr
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def wish_user():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    """Listen for voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Adjusts for pauses in speech
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return "none"
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return "none"
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return "none"
    return command.lower()

# Main program logic
if __name__ == "__main__":
    wish_user()
    while True:
        command = take_command()
        if command == "none":
            continue
        elif "time" in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")
