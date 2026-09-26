import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing Jarvis, your personal assistant.")

    while True:
        # Listen for the wake word "hello" and obtain audio from the microphone.
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'hello'...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=10, phrase_time_limit=5)
            word=r.recognize_google(audio)
            print("You said: " + word)
            if "hello" in word.lower():
                speak("Hello! How can I assist you today?")
                print("Listening for your command...")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=10, phrase_time_limit=5)
                command = r.recognize_google(audio)
                print("You said: " + command)

                if "open YouTube" in command:
                    speak("Opening YouTube.")
                    webbrowser.open("https://www.youtube.com")
                elif "open Google" in command:
                    speak("Opening Google.")
                    webbrowser.open("https://www.google.com")
                elif "open Facebook" in command:
                    speak("Opening Facebook.")
                    webbrowser.open("https://www.facebook.com")
                elif "open Instagram" in command:
                    speak("Opening Instagram.")
                    webbrowser.open("https://www.instagram.com")
                elif "open Twitter" in command:
                    speak("Opening Twitter.")
                    webbrowser.open("https://www.twitter.com")
                elif "open LinkedIn" in command:
                    speak("Opening LinkedIn.")
                    webbrowser.open("https://www.linkedin.com")
                else:
                    speak("Sorry, I didn't understand that command.")
        except sr.WaitTimeoutError:
            print("No speech detected. Say 'hello' near the microphone and try again.")
        except Exception as e:
            print("Error; {0}".format(e))