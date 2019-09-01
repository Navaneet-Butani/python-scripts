#for running this on your system follow below steps

#you have to install module like SpeechRecognition(with "pip install SpeechRecognition"), PyAudio(with "pip install PyAudio") etc. 
#(If you are getting errors while installing python modules then install Anaconda then install with "conda install ...")

#import speech_recognition module before it you have to download it with the "pip install SpeechRecognition" in your terminal/cmd
import speech_recognition as sr

r = sr.Recognizer() 

# Open the file for writing(appending) the content, what you speak...
f = open('Text_file.txt','a')


with sr.Microphone() as source:
    print("Speak Anything : ")
    audio = r.listen(source)    # This is for listening from Microphone

    try:
        text = r.recognize_google(audio)    
        print("You said : "+text)   # To write speech on the consol
        f.write(text)   # To write speech on the file.
        f.write("\n")   # To append new text on new line in file
        f.close()   # To close the file after writing
    except:
        print("Sorry could not recognize your voice!")  # Providing error message for any exceptions