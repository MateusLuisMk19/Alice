""" import pyautogui as PA
import time

PA.alert('Alice vai assumir o controle por favor não mexa em nada até terminar')
PA.PAUSE = 0.5
PA.FAILSAFE = True


PA.hotkey('winleft',"1") """
import pyttsx3

engine = pyttsx3.init()
""" voices = engine.getProperty('voices')

print(voices[0]) """
# for voice in voices:
# print(voice)
engine.setProperty('voice', b'pt' )
engine.say('Olha ela, cara.')
engine.runAndWait()