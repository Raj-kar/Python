import speech_recognition as sr

AUDIO_FILE = ("raj_voice.wav")

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# try:
#     print(r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Wait !")
# except sr.RequestError:
#     print("Request error !")