from time import sleep
import speech_recognition as sr 
import keyboard  
import Marvin

recognizer = sr.Recognizer()


BOT_NAMES = ['amaterasu', 'Amaterasu','Assistente','amateras','mattress','computador']
STOP_COMMAND = 'computador pare'

listening = True 

def activate_assistant():
  global listening
  print("Estou ouvindo...")
  Marvin.listen()
  listening = True

def record_audio():
    global listening
    with sr.Microphone() as source:
        while listening:
            audio = recognizer.listen(source, None, 3)
            voice_data = ''

            try:
                voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
                print(">>", voice_data)
                if STOP_COMMAND in voice_data:
                    listening = False  # Parar a escuta temporariamente
                    break
                elif any(bot_name_variation in voice_data for bot_name_variation in BOT_NAMES):
                    activate_assistant()
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('Serviço offline')

while True:
    record_audio()
    while not listening:
        sleep(0.05)
        with sr.Microphone() as source:  # Definindo a variável source novamente
            audio = recognizer.listen(source, None, 3)
            voice_data = ''
            try:
                voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
                print(">>", voice_data)
                if any(bot_name_variation in voice_data for bot_name_variation in BOT_NAMES):
                    activate_assistant()
                    break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('Serviço offline')
# if keyboard.is_pressed('ctrl+alt+m'):
#    Marvin.listen()
