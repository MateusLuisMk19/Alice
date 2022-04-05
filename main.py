# ficheiro prinipal
import speech_recognition as sr
import pyautogui as Aut
import pyttsx3
import fun
import bot
import time

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
            txt = 'Ouvindo'
            print(txt, '...')
            mq.say('i')
            mq.runAndWait()

            # define microfone como fonte de audio
            voz = audio.listen(src)

            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()

            if 'alice' in comando:
                comando = comando.replace('alice ', '')
            return comando + '.'
    except:
        print('Erro no Microfone')
        #txt = 'erro de captação'
        #mq.say(txt)
        #mq.runAndWait()
        time.sleep(3)
        alice_()

#recebe o comando e deide a resposta
def alice_():
    while True:
        comando = abrir_mic()
        if comando == '.' or comando == 'stop.' or comando == 'para.' or comando == 'parou.':
            exit()

        print(comando)
        resposta = ""

        if 'horas' in comando:
            resposta = ('São ' + fun.horas())
        elif ('dia' in comando) and ('hoje' in comando):
            resposta = ('Hoje é ' + fun.dia())
        elif ('quem foi' in comando) or ('quem é' in comando) or ('você conhece' in comando) or ('o que é' in comando):
            resposta = fun.wiki(comando)
        elif ('toca' in comando) and ('música' in comando):
            resp = 'Ok. Vou assumir o controle do computador, por favor não mexa em nada até eu terminar'
            resposta = 'Terminei'
            mq.say(resp)
            mq.runAndWait()
            bot.tocar_soundC()
        elif ('abrir' in comando) or ('abra' in comando):
            resp = 'Aguarde'
            mq.say(resp)
            mq.runAndWait()

            re = bot.abrir(comando)
            if 'não' in re or 'app' in re:
                resposta = re
            else:
                resposta = re + " aberto"

        if ('escrever' in comando) or ('escreve' in comando):
            bot.escrever(comando)

        if ('troca.' in comando) or ('trocar.' in comando):
            bot.trocar()

        if ('muda para.' in comando) or ('mudar para.' in comando):
            Aut.keyDown('alt')

            mq.say('para?...')
            mq.runAndWait()

            com = abrir_mic()
            valor = int(com.replace('.', ''))

            for x in range(valor):
                Aut.press('tab')

            Aut.keyUp('alt')

        if(resposta != ""):
            print(resposta)
            mq.say(resposta)
            mq.runAndWait()
        else:
            print("")

time.sleep(10)
alice_()

