# ficheiro prinipal
import speech_recognition as sr
import pyttsx3
import fun

# criar reconhecedor e a voz do assistente
audio = sr.Recognizer()
mq = pyttsx3.init()

#mudar as propriedades da voz
voices = mq.getProperty('voices')
mq.setProperty("voice", voices[-1].id)

# abrir o mirofone para ouvir. Devolve o comando (dito pelo utilizador) sem o nome Alice
def abrir_mic():
    try:
        with sr.Microphone() as src:
            print('Ouvindo...')

            # define microfone como fonte de audio
            voz = audio.listen(src)

            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()

            if 'alice' in comando:
                comando = comando.replace('alice ', '')
    except:
        print('Erro no Microfone')

    return comando

#recebe o comando e deide a resposta
def alice_():
    comando = abrir_mic()
    print(comando)
    resposta = ""

    if 'horas' in comando:
        resposta = ('São ' + fun.horas())
    elif ('quem foi' in comando) or ('quem é' in comando) or ('você conhece' in comando) or ('o que é' in comando):
        resposta = fun.wiki(comando)
    #elif ('youtube' in comando):


    if(resposta != ""):
        print(resposta)
        mq.say(resposta)
        mq.runAndWait()
    else:
        print("")

alice_()

