
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour) 
  if hour>=0 and hour<12:
    speak("good morning!")
  elif hour>=12 and hour<18:
    speak("good afternoon!")
  else:
    speak("good evening!") 

  speak("hey cutie! i am Natasha. how may i help you?")  

def takeCommand():
  #it takes microphone iputy from user and returns string
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said : {query}\n")

  except Exception as e:
    #print(e)
    print("say that again please...")
    return "None" 
  return query



if __name__ == "__main__":
  wishMe()
  while True:
    query = takeCommand().lower()

   #logic for executing tasks
    if 'wikipedia' in query:
     speak('Searching wikipedia...')
     query = query.replace("wikipedia", "")
     results = wikipedia.summary(query, sentences=1)
     speak("according to wikipedia")
     print(results)
     speak(results)

    elif 'open youtube' in query: 
      webbrowser.open("youtube.com")

    elif 'open google' in query: 
      webbrowser.open("google.com")

    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"the time is {strTime}")

    elif 'exit' in query or 'quit' in query:
      speak("Thanks for giving me your time")
      exit()

    elif 'joke' in query:
      speak(pyjokes.get_joke())

    elif 'how are you' in query:
      speak("I am fine, Thank you")
      speak("How are you, Sir")
 
    elif 'fine' in query or "good" in query:
      speak("It's good to know that your fine")

    elif "who i am" in query:
      speak("If you talk then definitely your human.")

    elif 'is love' in query:
      speak("It is 7th sense that destroy all other senses")
 


    




    
