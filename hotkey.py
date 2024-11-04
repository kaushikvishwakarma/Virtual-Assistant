import os 
import speech_recognition as sr
import datetime
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        r.energy_threshold=50
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"Used Said:{query}")
    except Exception as e:
        return "None" 
    return query.lower()
while True:
    query=takecommand()
    if 'wake up jarvis'in query:
        os.startfile('C:\\Users\\Lenovo\\Desktop\\AI\\AI base.py')
    elif 'jarvis wake up'in query:
        os.startfile('C:\\Users\\Lenovo\\Desktop\\AI\\AI base.py')
    elif 'jarvis i need you' in query:
        os.startfile('C:\\Users\\Lenovo\\Desktop\\AI\\AI base.py')
    elif 'online a'in query:
        os.startfile('C:\\Users\\Lenovo\\Desktop\\AI\\AI base.py')
    else:
        print('jarvis is sleeping right now... just say"wake up jarvis"to wake it up ')
        strTime=datetime.datetime.now().strftime("%I:%M:%S:%A")
        print(strTime)

