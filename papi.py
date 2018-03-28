from gtts import gTTS
import os


def aud(mytext):
    mytext =mytext[9::]
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    a=myobj.save("welcome.mp3")


