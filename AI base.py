import pyttsx3 #this sould be installed by typing pip install pyttsx3
import datetime
import speech_recognition as sr#this should also installed librarry name speechreco...tion
import wikipedia#this also
import webbrowser
import os
import pywhatkit
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening Sir!")
    speak(" Your Virtual Assistant is online ! How can i help you !")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        r.energy_threshold = 100
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"Used Said:{query}\n")
    except Exception as e:
        speak("I am sorry !please Say that again ...")
        print("I am sorry !please Say that again ...")
        return "None" 
    return query
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        #logic for exicuting task based on query
        if 'wikipedia' in query:
            print("searching in wikipdeia...")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'thank you' in query:
            speak("My pleasure sir! But its my Job to assist you")
        elif 'quit' in query:
            speak("Nice to work with you Sir!Call me anytime when you need! have a nice day")
            exit(0)
        elif 'exit' in query:
            speak("Sir I am tired now. I need a break. Call me anytime you need")
            exit(0)
        elif 'open google' in query:
            speak("Sir,what would you like to search on google")
            query=takecommand().lower()
            if 'search' in query:
                query=query.replace('search',"")
                if 'on google' in query:
                query=query.replace('on google',"")
                pywhatkit.search(query)
                results=wikipedia.summary(query,sentences=2)
                speak("According to web..")
                speak(results)
            elif 'on google' in query:
                query=query.replace('on google',"")
                pywhatkit.search(query)
                results=wikipedia.summary(query,sentences=2)
                speak("According to web..")
                speak(results)               
            elif 'open google'in query:
                webbrowser.open('google.com')
                speak('opening google for you...')            
            else:
                pywhatkit.search(query)
                results=wikipedia.summary(query,sentences=2)
                speak("According to web..")
                speak(results)                                          
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'C:\\Users\\Lenovo\\Desktop\\kaushik\\Aa'
            song=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%I:%M:%A")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open bluestack' in query:
            bspath="C:\\Program Files\\BlueStacks\\Bluestacks.exe"
            os.startfile(bspath)
        elif 'open physics wallah app' in query:
            bspath="C:\\Users\\Lenovo\\Desktop\\Physics Wallah.lnk"
            os.startfile(bspath)
        elif 'open physics wala app' in query:
            bspath="C:\\Users\\Lenovo\\Desktop\\Physics Wallah.lnk"
            os.startfile(bspath)
        elif 'how are you' in query:
            speak("its very cold outside but It doesnt affect me much! I hope you are good")
            print("its very cold outside but It doesnt affect me much! I hope you are good")
        elif 'on google' in query:
            query=query.replace('on google',"")
            if "search" in query:
                query=query.replace('search',"")
                pywhatkit.search(query)
                results=wikipedia.summary(query,sentences=3)
                speak(results)
            else:
                pywhatkit.search(query)
                results=wikipedia.summary(query,sentences=3)
                speak(results)
        elif 'on youtube' in query:
            speak("Sir! what's the title for the video which you wanna play on youtube!")
            query=takecommand().lower()
            if query!='none':
                speak("I found this latest on youtube")
                pywhatkit.playonyt(query) 
        elif 'remember that' in query:
            query=query.replace('remember that',"")
            query=query.replace('jarvis',"")
            speak('you tell me remember that'+query)
            remember=open("C:\\Users\\Lenovo\\Desktop\\AI\\rmmbr.dat","w")
            remember.write(query)
            remember.close()
        elif 'did you remember something' in query:
            remember=open('C:\\Users\\Lenovo\\Desktop\\AI\\rmmbr.dat','r')
            sen=remember.read()
            print(sen)
            speak('You told me to remember that'+sen)           
            remember.close()
        elif 'you need a break' in query:
            speak("as you wish sir! call me when you need.")
            exit(0)
        elif 'shut down my pc'in query:
            speak('Sir! are you sure to shutdown this pc?')
            t=takecommand().lower()
            if 'yes' in t:
                speak('As you wish sir,pc is scheduled for shut down in 2 minutes')
                pywhatkit.shutdown(time=125)
            else:
                speak('According to your response,shut down procces is being terminated')
                continue
        elif 'cancel shutdown' in query:
            speak('Are you sure you wanna terminate scheduled shut down')
            t=takecommand().lower()
            if 'yes' in t:
                speak('OK sir!the scheduled shutdown is being canceled')
                pywhatkit.cancel_shutdown()
            else:
                speak('According to your response,shut down procces is being contiuned')
        elif 'turn off my pc' in query:
            speak('OK sir! pc is shutting down in 3.       2.       1.')
            pywhatkit.shutdown(time=1)
        elif 'open your code' in query:
            speak('you are trying to access protected file please tell me the correct password....')
            passw='open binary'
            t=takecommand().lower()
            if t==passw:
                speak('opening my code file')
                os.startfile('D:\Youtube material\plz dont touch\AI base.py')
            else:
                speak('sorry the entered password is incorrect so i cant open my code file')
        

        


            
        

            

            








            
              
