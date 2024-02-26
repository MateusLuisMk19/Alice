import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import time
import pyautogui as pg
import bot


# criar reconhecedor e a voz do assistente
audio = sr.Recognizer()
mq = pyttsx3.init()

#mudar as propriedades da voz
voices = mq.getProperty('voices')
# mq.setProperty("voice", voices[-1].id)
err = 0

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
                comando = comando.replace('alice', '')
            return comando + '.'
    except sr.RequestError as error:
        print('Erro no Microfone', format(error))

        #txt = 'erro de captação'
        #mq.say(txt)
        #mq.runAndWait()
        global err  
        err = err+1
        if err == 3:
            return "stop."  
        
        time.sleep(1)
    except sr.UnknownValueError:
        print("Não entendi o que disse")
        time.sleep(1)

        
#recebe o comando e deide a resposta
def alice_(mode=""):
    if mode == "cvoice":
        return "cvoice"
    
    def isCondition(comand,to):
        result = False
        out = ["stop.","para.","parou."]
        control = ["control mode.","voice control mode.",
                   "modo controle de voz.","modo voz.","modo de voz.",
                   "modo control de voz."]

        match to:
            case "out":
                for o in out:
                    if comand == o:
                        result = True
            case "control":
                for c in control:
                    if comand == c:
                        result = True
        return result

    while True:
        comando = abrir_mic()
        if isCondition(comando,"out"):
            exit()

        if isCondition(comando,"control"):
            return "cvoice"

        print(comando)
        resposta = ""

        if 'horas' in comando:
            resposta = ('São ' + horas())
        elif ('dia' in comando) and ('hoje' in comando):
            resposta = ('Hoje é ' + dia())
        elif ('quem foi' in comando) or ('quem é' in comando) or ('você conhece' in comando) or ('o que é' in comando):
            resposta = wiki(comando)
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
            pg.keyDown('alt')

            mq.say('para?...')
            mq.runAndWait()

            com = abrir_mic()
            valor = int(com.replace('.', ''))

            for x in range(valor):
                pg.press('tab')

            pg.keyUp('alt')

        if(resposta != ""):
            print(resposta)
            mq.say(resposta)
            mq.runAndWait()
        else:
            print("")


#Aux ------------------------------------------------------------
def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    return hora

def dia():
    dia_sem = datetime.datetime.now().strftime("%A")
    match dia_sem:
        case "Monday":
            d_s = "Segunda-feira"
        case "Tuesday":
            d_s = "Terça-feira"
        case "Wednesday":
            d_s = "Quarta-feira"
        case "Thursday":
            d_s = "Quinta-feira"
        case "Friday":
            d_s = "Sexta-feira"
        case "Saturday":
            d_s = "Sábado"
        case "Sunday":
            d_s = "Domingo"

    mes = datetime.datetime.now().strftime("%B")
    match mes:
        case "January":
            ms = "Janeiro"
        case "February":
            ms = "Fevereiro"
        case "March":
            ms = "Março"
        case "April":
            ms = "Abril"
        case "May":
            ms = "Maio"
        case "June":
            ms = "Junho"
        case "July":
            ms = "Julho"
        case "August":
            ms = "Agosto"
        case "September":
            ms = "Setembro"
        case "October":
            ms = "Outubro"
        case "November":
            ms = "Novembro"
        case "December":
            ms = "Dezembro"


    dia = datetime.datetime.now().strftime("%d")
    if dia[0] == "0":
        dia = dia.replace("0","")

    ano = datetime.datetime.now().strftime("%Y")

    hoje = d_s + ". " + dia + " de " + ms + " de " + ano
    return hoje

def wiki(comando):
    if 'quem foi' in comando:
        comando = comando.replace('quem foi ', '')
    elif 'quem é' in comando:
        comando = comando.replace('quem é ', '')
    elif 'você conhece' in comando:
        comando = comando.replace('você conhece ', '')
    elif 'o que é' in comando:
        comando = comando.replace('o que é ', '')

    wikipedia.set_lang('pt')
    comando = wikipedia.summary(comando, 1)
    return comando
