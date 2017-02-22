# -*-coding:utf-8-*-
"""Speech file for the media understanding 2017 project.

File name: speech.py
Author: Media Understanding 2017
Date created: 22/2/2017
Date last modified: 22/2/2017
Python Version: 3.4
"""
import speech_recognition as sr


def wait_for_voice():
    """Wait for voice."""
    # obtain audio from the microphone perhaps this should be changed for pepper
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for audio input")
        audio = r.listen(source)
    print("sending audio to google")
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key,
        # use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Found text: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google \
               Speech Recognition service; {0}".format(e))