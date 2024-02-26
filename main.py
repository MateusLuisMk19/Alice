# ficheiro prinipal
# carregar variaveis de ambiente

import time
import fun
import cvoice as vc

mode = ["","cvoice"]

time.sleep(3)
match fun.alice_():
    case "cvoice":
        vc.cvoice()
 
