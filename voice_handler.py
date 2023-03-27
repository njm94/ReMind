import speech_recognition as sr
import pyttsx3


def speech_to_text(pause_thresh=1, noise_dur=0.5):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = (pause_thresh)
    microphone = sr.Microphone()
	
	# adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=noise_dur)
        print("Listening...")
        audio = recognizer.listen(source)
	
	# set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    print(response["transcription"])
    return response
   

def text_to_speech(speech, voice_is_fem=1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_is_fem].id)
    engine.say(speech)
    engine.runAndWait()