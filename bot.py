import pyautogui as PA
import time

PA.PAUSE = 1.8
PA.FAILSAFE = True



def alert():
    PA.alert(text='Vou assumir o controle por favor não mexa em nada até terminar.\n Aviso quando terminar', 
             title='Alice', 
             button='OK')

def tocar_soundC():
    #abrir o chrome
    PA.press('winleft')
    time.sleep(0.3)
    PA.write('chrome')
    PA.press('enter')

    #entrar no soundcloud
    time.sleep(1)
    PA.write('https://soundcloud.com/you/likes')
    PA.press('enter')

    #dar play
    time.sleep(1.3)
    PA.press('space')

def abrir(comando):
    if ('bloco de notas' in comando) or ('bloco de nota' in comando) or ('notas' in comando):
        PA.press('winleft')
        PA.write('bloco de notas')
        PA.press('enter')
        return 'bloco de notas'
    elif 'ambiente de trabalho' in comando or 'cozinha' in comando:
        PA.hotkey('winleft', 'd')
        return 'ambiente de trabalho'
    elif 'app' in comando or 'aplicação' in comando:
        if 'primeira' in comando or '1' in comando:
            num = '1'
        elif 'segunda' in comando or '2' in comando:
            num = '2'
        elif 'terceira' in comando or '3' in comando:
            num = '3'
        elif 'quarta' in comando or '4' in comando:
            num = '4'
        elif 'quinta' in comando or '5' in comando:
            num = '5'
        elif 'sexta' in comando or '6' in comando:
            num = '6'
        elif 'setima' in comando or '7' in comando:
            num = '7'
        elif 'oitava' in comando or '8' in comando:
            num = '8'
        elif 'nona' in comando or '9' in comando:
            num = '9'
        elif 'decima' in comando or '10' in comando:
            num = '10'
        else:
            return 'pode repetir? não entendi'

        PA.hotkey('winleft', num)
        return 'abrindo app ' + num
    else:
        return 'não entendi'

def escrever(comando):
    if ('escrever' in comando):
        comando = comando.replace('escrever ','')
    elif('escreve' in comando):
        comando = comando.replace('escreve ','')
    elif ('escreva' in comando):
        comando = comando.replace('escreva ', '')

    #comando = comando.replace(comando[0],comando[0].upper())
    time.sleep(1)
    PA.write(comando)

def trocar():
    PA.hotkey('alt', 'tab')








