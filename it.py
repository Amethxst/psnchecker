import webbrowser
import colorama
from colorama import Back, Fore, Style, init
colorama.init(autoreset=True)





traduzioni = {
    "key_not_found":"File {color_key}Key.txt{color_reset} non trovato. Sto creando il file..",
    "enter_valid_npsso": "Inserisci il codice npsso valido: ",
    "npsso_correct": "Codice {color_key}VALIDO{color_reset}",
    "npsso_incorrect":"Codice npsso{color_key} ERRATO{color_reset}. Scrivi un {color_key2} nuovo codice{color_reset2}",
    "npsso_created_successfully":"Key.txt creato e codice inserito correttamente",
    "npsso_expired":"Codice npsso{color_key} scaduto o errato{color_reset}.",
    "enter_npsso_valid":"Inserisci il codice npsso valido: ",
    "reading_error": "Errore durante la lettura del file Key.txt: {error_message}",
    "exit":"Premi un tasto per uscire: ",
    "invalid_input": "INPUT ERRATO. RIPROVA",
    "id_non_trovato": "ID INESISTENTE. CERCA ANCORA",
    "random":"ERRORE RANDOM",
    "npsso_correct2": "Codice {color_key} VALIDO{color_reset}"
}



def benvenuto():
    print(f"Tool by {Fore.CYAN}@yAmethxst{Fore.RESET}")
    print(f"API wrapper by{Fore.RED}'isFakeAccount'{Fore.RESET}(github)")
    print()
    API = input("Vuoi visualizzare le API? [y/n]: ")
    if API == "y":
        webbrowser.open("https://github.com/isFakeAccount/psnawp")
        print()
        print(f"{Back.WHITE}                                  ")
        print()
    else:
        print()
        print(f"{Back.WHITE}                                  ")
        print()