import pyautogui as pg
import time
from fun import abrir_mic, alice_

#comand = ["k.","h.","f.","stop."]

def cvoice():
    #n=0
    while True:
        print(" ### Voice Mode ### ")
        comand = abrir_mic()
        #print(comand.__len__())
        if isFinish(comand):
          alice_()
        elif(comand):
            if comand.__len__() == 2:
                time.sleep(1)
                pg.press(comand.replace('.',''))
            else:
                print(comand) 
        else:
            time.sleep(1)
            # breakf
        #n=n+1

def isFinish(comand):
    result = False
    op = ["voice control out.","sair do modo control.","sair do modo controle.","terminar controle.","terminar control."]
    
    for i in op:
        if comand == i:
            result = True

    return result 
