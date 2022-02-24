# ficheiro prinipal

import speech_recognition as sr
import pyttsx3
import datetime

# # criar reconhecedor
# r = sr.Recognizer()

# # abrir o mirofone para ouvir
# with sr.Microphone() as src:
#     while True:
#         audio = r.listen(src) #define microfone como fonte de audio

#         print(r.recognize_google(audio, language='pt'))

# criar reconhecedor
audio = sr.Recognizer()
mq = pyttsx3.init()


voices = mq.getProperty('voices')
mq.setProperty("voice", voices[-1].id)


# # abrir o mirofone para ouvir
def exec_cmd():

    try:
        with sr.Microphone() as src:
            print('Ouvindo...')
            voz = audio.listen(src)  # define microfone como fonte de audio
            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()
            if 'alice' in comando:
                comando = comando.replace('alice', '')

    except:
        print('Erro no Microfone')

    return comando

def cmd_voz_user(): 
    comando = exec_cmd()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        print(hora)
        mq.say('São ' + hora)
        mq.runAndWait()

cmd_voz_user()