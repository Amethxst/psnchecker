import json
import os
import seleziona_lingua
import curses
import sys
import webbrowser

import colorama
from colorama import Back, Fore, Style, init
colorama.init(autoreset=True)

from it import traduzioni as it_traduzioni, benvenuto as benvenuto_it
from en import traduzioni as en_traduzioni, benvenuto as benvenuto_en
from fr import traduzioni as fr_traduzioni, benvenuto as benvenuto_fr
from es import traduzioni as es_traduzioni, benvenuto as benvenuto_es

from psnawp_api import PSNAWP
from psnawp_api.core.psnawp_exceptions import (
   PSNAWPNotFound,
   PSNAWPForbidden,
   PSNAWPBadRequest,
   PSNAWPIllegalArgumentError,
   PSNAWPException,
   PSNAWPAuthenticationError,
   PSNAWPNotAllowed,
   PSNAWPServerError,
   PSNAWPUnauthorized,
)


def set_terminal_title(title):
    if sys.platform.startswith('win32'):
        # Windows
        print(f"\033]0;{title}\a", end='', flush=True)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        # Linux e MacOS
        print(f"\033]2;{title}\a", end='', flush=True)

set_terminal_title('PSN CHECKER 1.0')



file_lingua = 'lng.json'

valid_languages = ['Italiano', 'English', 'Français', 'Español']

try:
    with open(file_lingua, 'r') as f:
        lingua_selezionata = json.load(f)['lingua']

    if lingua_selezionata not in valid_languages:
        raise ValueError('Lingua non valida')

except (FileNotFoundError, ValueError):
    lingua_selezionata = curses.wrapper(seleziona_lingua.seleziona_lingua)
    with open(file_lingua, 'w') as f:
        json.dump({'lingua': lingua_selezionata}, f)

if lingua_selezionata == 'Italiano':
    traduzioni = it_traduzioni
    benvenuto = benvenuto_it
elif lingua_selezionata == 'English':
    traduzioni = en_traduzioni
    benvenuto = benvenuto_en
elif lingua_selezionata == 'Français':
    traduzioni = fr_traduzioni
    benvenuto = benvenuto_fr
elif lingua_selezionata == 'Español':
    traduzioni = es_traduzioni
    benvenuto = benvenuto_es

benvenuto()





if not os.path.isfile("key.txt"):
    print(traduzioni["key_not_found"].format(color_key=Fore.YELLOW,color_reset=Fore.RESET)) #GLI DICO DI STAMPARE DA TRADUZIONI, PRESENTI NEI FILE .JSON, LA CHIAVE "key_not_found". SPECIFICO POI IL FORMATO DI COLOR_KEY E COLOR_RESET (SEMPRE SCRITTI NEI FILE .JSON)

    #SE KEY.TXT NON È PRESENTE, CREA KEY.TXT E TI FA INSERIRE CODICE NPSSO VALIDO. SE SBAGLI, RIPETE
    while True:
        npsso = input(traduzioni["enter_valid_npsso"])
        print()
        try:
            psnawp = PSNAWP(npsso)
            client = psnawp.me()
            print(traduzioni["npsso_correct"].format(color_key=Fore.GREEN,color_reset=Fore.RESET))
            print()
            break
        except PSNAWPAuthenticationError:
            print(traduzioni["npsso_incorrect"].format(color_key=Fore.RED,color_reset=Fore.RESET,color_key2=Fore.YELLOW,color_reset2=Fore.RESET))
            print()
        
    with open("key.txt", "w") as f:
        f.write(npsso)
        print(traduzioni["npsso_created_successfully"])
        print()
        print(f"{Back.WHITE}                                  ")
        print()


try:
    with open('key.txt', 'r') as file:
        npsso = file.read().strip()

        psnawp = PSNAWP(npsso)
        client = psnawp.me()


#SE CODICE NPSSO È SCADUTO/ERRATO, TI FA REINSERE IL CODICE
except PSNAWPAuthenticationError:
    print(traduzioni["npsso_expired"].format(color_key=Fore.RED,color_reset=Fore.RESET))
    print()
    while True:
        npsso = input(traduzioni["enter_npsso_valid"].format(color_key=Fore.GREEN, color_reset=Fore.RESET))
        print()
        try:
            psnawp = PSNAWP(npsso)
            client = psnawp.me()
            print(traduzioni["npsso_correct2"].format(color_key=Fore.GREEN,color_reset=Fore.RESET))
            print()
            break
        except PSNAWPAuthenticationError:
            print(traduzioni["npsso_incorrect"])

    with open("key.txt", "w") as f:
        f.write(npsso)
        print(traduzioni["npsso_created_successfully"])
        print()
        print(f"{Back.WHITE}                                  ")
        print()

except Exception as e:
    print(traduzioni["reading_error"].format(error_message=str(e)))
    print()
    input("Premere un tasto per uscire.. ")
    sys.exit()


for i in range(0,1000):
   while True:
       try:
          
      
           #SETUP ONLINE ID
           idonline=input("ID PSN: ")
           print()    
           idonline_obj = psnawp.user(online_id=idonline)  
           idonline_normalized = idonline_obj.online_id

           if idonline_normalized.lower() == idonline.lower():
               print("Online ID: " + idonline_normalized)
           else:
               print(f"Online ID: {idonline_normalized} ({Fore.YELLOW}NEW{Style.RESET_ALL})")
           
           #SETUP ACCOUNT ID
           print("Account ID: "+(idonline_obj.account_id))


           

           #SETUP HEX
           codicehex = idonline_obj.account_id                             #faccio chiamare la str OG come voglio
           hex1=int(codicehex)                                             #creo variabile 'hex1' che è int del codicehex
           hexfinale = hex(hex1)                                           #creo variabile 'hexfinale' che converte in hex la variabile hex1

           if len(hexfinale)==16:
               print("HEX: "+"00"+(hexfinale[2:])) 
           elif len(hexfinale)==17:
               print("HEX: "+"0"+(hexfinale[2:]))
           elif len(hexfinale)==18:
               print("HEX: "+(hexfinale[2:])) 

         #SETUP ENDIAN
           byte_array = bytearray.fromhex(hexfinale[2:])
           byte_array.reverse()
           output_hex = ''.join(format(x, '02x') for x in byte_array)
           print("Endian:", output_hex)

          #SETUP PLUS
           testplus = idonline_obj.profile()

           if (testplus.get('isPlus')) == True:
               print("Plus: Sì")
           else:
               print("Plus: No")





           #SETUP BIO DA COMPLETARE CON DIZIONARIO
           #print(idonline_obj.profile())


           print()
           print(f"{Back.WHITE}                                  ")
           print()






           #SETUP ECCEZIONI


       except PSNAWPIllegalArgumentError:
           print(traduzioni['invalid_input'])
           print()
           print(f"{Back.WHITE}                                  ")
           print()




       except PSNAWPNotFound:
           print(traduzioni["id_non_trovato"]) #se l'ID non esiste stampa print; RISOLVERE == SE l'ID <=2 DEVE SCRIVERE "IMPOSSIBILE"
           print()
           print(f"{Back.WHITE}                                  ")
           print()




       except PSNAWPException:
           print(traduzioni["random"])
           print()
           print(f"{Back.WHITE}                                  ")
           print()