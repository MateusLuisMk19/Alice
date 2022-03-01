import datetime
import wikipedia

def horas():
    hora = datetime.datetime.now().strftime('%H:%M')
    return hora

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
