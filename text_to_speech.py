import pyttsx3

engine = pyttsx3.init()
engine.say(speech["transcription"])
engine.runAndWait()